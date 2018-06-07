import json
from django.conf.urls import url, include
from anuario.models import asignacionActivo,fondo,instrumento,bindex
from rest_framework.decorators import api_view
from django.http import HttpResponse

@api_view(['GET','POST','PUT'])
def apiAsignacionActivo(request,id=None):
	if request.method == 'GET':
		if id is not None:
			try:
				lista=[]
				query = asignacionActivo.objects.values('red_bono','red_efectivo','red_convertible','red_preferida','red_acciones','red_otra','portafolio_fecha').get(pk=id)
				fecha = str(query['portafolio_fecha'])
				lista.append({
					'red_bono':query['red_bono'],
                    'red_efectivo':query['red_efectivo'],
                    'red_convertible':query['red_convertible'],
                    'red_preferida':query['red_preferida'],
                    'red_acciones':query['red_acciones'],
                    'red_otra':query['red_otra'],
					'portafolio_fecha':fecha,
					})
			except asignacionActivo.DoesNotExist:
				query = {"mensaje":"No existen datos"}

		else:
			try:
				lista=[]
				query = asignacionActivo.objects.all().values('red_bono','red_efectivo','red_convertible','red_preferida','red_acciones','red_otra','portafolio_fecha')
				if query.count()>0:
					for x in query:
						fecha = str(x['portafolio_fecha'])
						lista.append({
							'red_bono':x['red_bono'],
		                    'red_efectivo':x['red_efectivo'],
		                    'red_convertible':x['red_convertible'],
		                    'red_preferida':x['red_preferida'],
		                    'red_acciones':x['red_acciones'],
		                    'red_otra':x['red_otra'],
							'portafolio_fecha':fecha,
							})
				else:
					lista = {"mensaje":"No existen datos"}
			except asignacionActivo.DoesNotExist:
				pass


		return HttpResponse(json.dumps(lista,indent=4),content_type="application/json")

	elif request.method == 'POST':
		flag = True
		mensaje = ""

		red_bono= request.data['red_bono']
		red_efectivo= request.data['red_efectivo']
		red_convertible=request.data['red_convertible']
		red_preferida= request.data['red_preferida']
		red_acciones= request.data['red_acciones']
		red_otra=request.data['red_otra']
		portafolio_fecha=request.data['portafolio_fecha']

		nombre_fondo= request.data['fondo']
		clase_proveedor = request.data['clase_proveedor']

		if red_bono=='' or red_efectivo=='' or red_convertible=='' or red_preferida=='' or red_acciones ==''or red_otra ==''or portafolio_fecha ==''or nombre_fondo ==''or clase_proveedor =='':
			mensaje = {"mensaje":"Debes completar todos los campos"}
		else:
			try:
				f = fondo.objects.get(nombre=nombre_fondo)
			except fondo.DoesNotExist:
				flag = False
				mensaje = {"mensaje":"error en los datos"}

			try:
				if flag==True:
					i = instrumento.objects.get(fondo=f,clase_proveedor=clase_proveedor)
			except instrumento.DoesNotExist:
				flag = False
				mensaje = {"mensaje":"error en los datos"}

			try:
				if flag==True:
					b = bindex.objects.get(pk=i.bindex_id)
					query = asignacionActivo.objects.filter(bindex=b,red_bono=red_bono,red_efectivo=red_efectivo
					,red_convertible=red_convertible,red_preferida=red_preferida,red_acciones=red_acciones,red_otra=red_otra,portafolio_fecha=portafolio_fecha)
					if query.count()>0:
						mensaje = {"mensaje":"El cliente que intentas crear ya existe"}
					else:
						b = bindex.objects.get(pk=i.bindex_id)
						asiact = asignacionActivo(bindex=b,red_bono=red_bono,red_efectivo=red_efectivo
						,red_convertible=red_convertible,red_preferida=red_preferida,red_acciones=red_acciones,red_otra=red_otra,portafolio_fecha=portafolio_fecha)
						asiact.save()
						mensaje = {"mensaje":"Datos guardados con exito"}
			except bindex.DoesNotExist:
				mensaje = {"mensaje":"error en los datos"}

		return HttpResponse(json.dumps(mensaje,indent=4),content_type="application/json")
