import json
from django.conf.urls import url, include
from anuario.models import fondo,categoria,moneda,domicilio
from rest_framework.decorators import api_view
from django.http import HttpResponse

@api_view(['GET','POST','PUT'])
def apiFondo(request,id=None):
	if request.method == 'GET':
		if id is not None:
			try:
				lista=[]
				query = fondo.objects.values('id','nombre','nombre_legal','fecha_inicio','categoria__nombre','moneda__nombre','domicilio__nombre').get(pk=id)
				fecha = str(query['fecha_inicio'])
				lista.append({
					'id':query['id'],
					'nombre':query['nombre'],
					'nombre_legal':query['nombre_legal'],
					'fecha_inicio':fecha,
					'categoria':query['categoria__nombre'],
					'moneda':query['moneda__nombre'],
					'domicilio':query['domicilio__nombre'],
					})
			except fondo.DoesNotExist:
				query = {"mensaje":"No existen datos"}

		else:
			try:
				lista=[]
				query = fondo.objects.all().values('id','nombre','nombre_legal','fecha_inicio','categoria__nombre','moneda__nombre','domicilio__nombre')
				if query.count()>0:
					for x in query:
						fecha = str(x['fecha_inicio'])
						lista.append({
							'id':x['id'],
							'nombre':x['nombre'],
							'nombre_legal':x['nombre_legal'],
							'fecha_inicio':fecha,
							'categoria':x['categoria__nombre'],
							'moneda':x['moneda__nombre'],
							'domicilio':x['domicilio__nombre'],
							})
				else:
					lista = {"mensaje":"No existen datos"}
			except fondo.DoesNotExist:
				pass


		return HttpResponse(json.dumps(lista,indent=4),content_type="application/json")

	elif request.method == 'POST':
		flag = True
		mensaje = ""

		fondo_id= request.data['fondo_id']
		nombre_fondo= request.data['nombre']
		nombre_legal=request.data['nombre_legal']
		fecha_inicio= request.data['fecha_inicio']

		cat_nombre= request.data['categoria']
		mon_nombre=request.data['moneda']
		dom_nombre=request.data['domicilio']


		if fondo_id=='' or nombre_fondo=='' or nombre_legal=='' or fecha_inicio=='' or cat_nombre ==''or mon_nombre ==''or dom_nombre =='':
			mensaje = {"mensaje":"Debes completar todos los campos"}
		else:
			try:
				c = categoria.objects.get(nombre=cat_nombre)
			except categoria.DoesNotExist:
				flag = False
				mensaje = {"mensaje":"error en los datos"}

			try:
				if flag==True:
					m = moneda.objects.get(nombre=mon_nombre)
			except moneda.DoesNotExist:
				flag = False
				mensaje = {"mensaje":"error en los datos"}

			try:
				if flag==True:
					d = domicilio.objects.get(nombre=dom_nombre)
			except domicilio.DoesNotExist:
				flag = False
				mensaje = {"mensaje":"error en los datos"}

			try:
				if flag==True:
					query = fondo.objects.filter(id=fondo_id,nombre=nombre_fondo,nombre_legal=nombre_legal,fecha_inicio=fecha_inicio,categoria=c,moneda=m,domicilio=d)
					if query.count()>0:
						mensaje = {"mensaje":"El cliente que intentas crear ya existe"}
					else:
						fon = fondo(id=fondo_id,nombre=nombre_fondo,nombre_legal=nombre_legal,fecha_inicio=fecha_inicio,categoria=c,moneda=m,domicilio=d)
						fon.save()
						mensaje = {"mensaje":"Datos guardados con exito"}
			except fondo.DoesNotExist:
				mensaje = {"mensaje":"error en los datos"}

		return HttpResponse(json.dumps(mensaje,indent=4),content_type="application/json")
