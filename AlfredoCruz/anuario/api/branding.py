import json
from django.conf.urls import url, include
from anuario.models import branding
from rest_framework.decorators import api_view
from django.http import HttpResponse

@api_view(['GET','POST','PUT'])
def apiBranding(request,id=None):
	if request.method == 'GET':
		if id is not None:
			try:
				query =branding.objects.values('id','nombre').get(pk=id)

			except branding.DoesNotExist:
				query = {"mensaje":"No existen datos"}

		else:
			try:
				query = branding.objects.all().values('id','nombre')
				if query.count()<1:
					query = {"mensaje":"No existen datos"}
				else:
					query = list(branding.objects.all().values('id','nombre'))

			except branding.DoesNotExist:
				pass


		return HttpResponse(json.dumps(query,indent=4),content_type="application/json")

	elif request.method == 'POST':

		mensaje = ""

		branding_id = request.data['branding_id']
		nombre= request.data['nombre']

		if branding_id=='' or nombre=='':
			mensaje = {"mensaje":"Debes completar todos los campos"}
		else:
			try:
				query =branding.objects.filter(pk=branding_id,nombre=nombre)
				if query.count()>0:
					mensaje = {"mensaje":"El cliente que intentas crear ya existe"}
				else:
					bra = branding(id=branding_id,nombre=nombre)
					bra.save()
					mensaje = {"mensaje":"Datos guardados con exito"}
			except bra.DoesNotExist:
				mensaje = {"mensaje":"error en los datos"}

		return HttpResponse(json.dumps(mensaje,indent=4),content_type="application/json")
