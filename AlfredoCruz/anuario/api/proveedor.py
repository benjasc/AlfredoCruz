import json
from django.conf.urls import url, include
from anuario.models import proveedor
from rest_framework.decorators import api_view
from django.http import HttpResponse

@api_view(['GET','POST','PUT'])
def apiProveedor(request,id=None):
	if request.method == 'GET':
		if id is not None:
			try:
				query =proveedor.objects.values('id','nombre','datos').get(pk=id)

			except proveedor.DoesNotExist:
				query = {"mensaje":"No existen datos"}

		else:
			try:
				query = proveedor.objects.all()
				if query.count()<1:
					query = {"mensaje":"No existen datos"}
				else:
					query = list(proveedor.objects.all().values('id','nombre','datos'))

			except proveedor.DoesNotExist:
				pass


		return HttpResponse(json.dumps(query,indent=4),content_type="application/json")

	elif request.method == 'POST':

		mensaje = ""

		proveedor_id = request.data['proveedor_id']
		nombre= request.data['nombre']

		if proveedor_id=='' or nombre=='':
			mensaje = {"mensaje":"Debes completar todos los campos"}
		else:
			try:
				query =proveedor.objects.filter(pk=proveedor_id,nombre=nombre)
				if query.count()>0:
					mensaje = {"mensaje":"El cliente que intentas crear ya existe"}
				else:
					pro = proveedor(id=proveedor_id,nombre=nombre)
					pro.save()
					mensaje = {"mensaje":"Datos guardados con exito"}
			except proveedor.DoesNotExist:
				mensaje = {"mensaje":"error en los datos"}

		return HttpResponse(json.dumps(mensaje,indent=4),content_type="application/json")
