import json
from django.conf.urls import url, include
from anuario.models import rentaFija,bindex,instrumento,fondo
from rest_framework.decorators import api_view
from django.http import HttpResponse

@api_view(['GET','POST','PUT'])
def apiRentaFija(request,id=None):
	if request.method == 'GET':
		if id is not None:
			try:
				lista=[]
				query =rentaFija.objects.values('bsed','bsem','bsmd','bsym','cred','crem','crmd','crym','portafolio_fecha').get(pk=id)
				lista.append({
					'bsed':query['bsed'],
					'bsem':query['bsem'],
					'bsmd':query['bsmd'],
					'bsym':query['bsym'],
					'cred':query['cred'],
					'crmd':query['crmd'],
					'crem':query['crem'],
					'crym':query['crym'],
					'portafolio_fecha':str(query['portafolio_fecha']),

					})
			except rentaFija.DoesNotExist:
				lista = {"mensaje":"No existen datos"}

		else:
			try:
				lista=[]
				query = rentaFija.objects.all().values('bsed','bsem','bsmd','bsym','cred','crem','crmd','crym','portafolio_fecha')
				if query.count()>0:
					for x in query:
						lista.append({
							'bsed':x['bsed'],
							'bsem':x['bsem'],
							'bsmd':x['bsmd'],
							'bsym':x['bsym'],
							'cred':x['cred'],
							'crem':x['crem'],
							'crmd':x['crmd'],
							'crym':x['crym'],
							'portafolio_fecha':str(x['portafolio_fecha']),
							})
				else:
					lista = {"mensaje":"No existen datos"}

			except rentaFija.DoesNotExist:
				pass


		return HttpResponse(json.dumps(lista,indent=4),content_type="application/json")

	elif request.method == 'POST':

		mensaje = ""
		flag=True

		bsed = request.data['bsed']
		bsem= request.data['bsem']
		bsmd=request.data['bsmd']
		bsym = request.data['bsym']
		cred = request.data['cred']
		crem= request.data['crem']
		crmd=request.data['crmd']
		crym = request.data['crym']
		portafolio_fecha=request.data['portafolio_fecha']


		nombre_fondo = request.data['fondo']
		clase_proveedor = request.data['clase_proveedor']

		if bsed=='' or bsem==''or bsmd==''or bsym==''or cred==''or crem==''or crmd==''or crym==''or portafolio_fecha=='':
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
					query = rentaFija.objects.filter(bindex=b,bsed=bsed,bsem=bsem,bsmd=bsmd,bsym=bsym,cred=cred,crem=crem,crmd=crmd,crym=crym,portafolio_fecha=portafolio_fecha)
					if query.count()>0:
						mensaje = {"mensaje":"El cliente que intentas crear ya existe"}
					else:
						b = bindex.objects.get(pk=i.bindex_id)
						renfij = rentaFija(bindex=b,bsed=bsed,bsem=bsem,bsmd=bsmd,bsym=bsym,cred=cred,crem=crem,crmd=crmd,crym=crym,portafolio_fecha=portafolio_fecha)
						renfij.save()
						mensaje = {"mensaje":"Datos guardados con exito"}
			except bindex.DoesNotExist:
				mensaje = {"mensaje":"error en los datos"}

		return HttpResponse(json.dumps(mensaje,indent=4),content_type="application/json")
