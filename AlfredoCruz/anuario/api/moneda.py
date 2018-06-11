import json
from django.conf.urls import url, include
from anuario.models import moneda
from rest_framework.decorators import api_view
from django.http import HttpResponse

@api_view(['GET','POST','PUT'])
def apiMoneda(request,id=None):
	if request.method == 'GET':
		if id is not None:
			try:
				query = moneda.objects.values('id','nombre').get(pk=id)

			except domicilio.DoesNotExist:
				query = {"mensaje":"No existen datos"}

		else:
			try:
				query = moneda.objects.all()
				if query.count()<1:
					query = {"mensaje":"No existen datos"}
				else:
					query = list(moneda.objects.all().values('id','nombre'))

			except moneda.DoesNotExist:
				pass


		return HttpResponse(json.dumps(query,indent=4),content_type="application/json")

	elif request.method == 'POST':

		mensaje = ""

		moneda_id = request.data['moneda_id']
		nombre= request.data['nombre']

		if moneda_id=='' or nombre=='':
			mensaje = {"mensaje":"Debes completar todos los campos"}
		else:
			try:
				query = moneda.objects.filter(pk=moneda_id,nombre=nombre)
				if query.count()>0:
					mensaje = {"mensaje":"El cliente que intentas crear ya existe"}
				else:
					mon = moneda(id=moneda_id,nombre=nombre)
					mon.save()
					mensaje = {"mensaje":"Datos guardados con exito"}
			except moneda.DoesNotExist:
				mensaje = {"mensaje":"error en los datos"}

		return HttpResponse(json.dumps(mensaje,indent=4),content_type="application/json")
