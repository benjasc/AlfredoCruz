import json
from django.conf.urls import url, include
from anuario.models import domicilio
from rest_framework.decorators import api_view
from django.http import HttpResponse

@api_view(['GET','POST','PUT'])
def apiDomicilio(request,id=None):
	if request.method == 'GET':
		if id is not None:
			try:
				query = domicilio.objects.values('id','nombre').get(pk=id)

			except domicilio.DoesNotExist:
				query = {"mensaje":"No existen datos"}

		else:
			try:
				query = domicilio.objects.all()
				if query.count()<1:
					query = {"mensaje":"No existen datos"}
				else:
					query = list(domicilio.objects.all().values('id','nombre'))

			except domicilio.DoesNotExist:
				pass


		return HttpResponse(json.dumps(query,indent=4),content_type="application/json")

	elif request.method == 'POST':

		mensaje = ""

		domicilio_id = request.data['domicilio_id']
		nombre= request.data['nombre']

		if domicilio_id=='' or nombre=='':
			mensaje = {"mensaje":"Debes completar todos los campos"}
		else:
			try:
				query = domicilio.objects.filter(pk=domicilio_id,nombre=nombre)
				if query.count()>0:
					mensaje = {"mensaje":"El cliente que intentas crear ya existe"}
				else:
					dom = domicilio(id=domicilio_id,nombre=nombre)
					dom.save()
					mensaje = {"mensaje":"Datos guardados con exito"}
			except domicilio.DoesNotExist:
				mensaje = {"mensaje":"error en los datos"}

		return HttpResponse(json.dumps(mensaje,indent=4),content_type="application/json")
