import json
from django.conf.urls import url, include
from anuario.models import frecuenciaDistribucion
from rest_framework.decorators import api_view
from django.http import HttpResponse

@api_view(['GET','POST','PUT'])
def apiFrecuenciaDistribucion(request,id=None):
	if request.method == 'GET':
		if id is not None:
			try:
				query = frecuenciaDistribucion.objects.values('id','frecuencia').get(pk=id)

			except frecuenciaDistribucion.DoesNotExist:
				query = {"mensaje":"No existen datos"}

		else:
			try:
				query = frecuenciaDistribucion.objects.all()
				if query.count()<1:
					query = {"mensaje":"No existen datos"}
				else:
					query = list(frecuenciaDistribucion.objects.all().values('id','frecuencia'))

			except frecuenciaDistribucion.DoesNotExist:
				pass


		return HttpResponse(json.dumps(query,indent=4),content_type="application/json")

	elif request.method == 'POST':

		mensaje = ""

		frecuencia= request.data['frecuencia']

		if frecuencia=='':
			mensaje = {"mensaje":"Debes completar todos los campos"}
		else:
			try:
				query = frecuenciaDistribucion.objects.filter(frecuencia=frecuencia)
				if query.count()>0:
					mensaje = {"mensaje":"El cliente que intentas crear ya existe"}
				else:
					fredis = frecuenciaDistribucion(frecuencia=frecuencia)
					fredis.save()
					mensaje = {"mensaje":"Datos guardados con exito"}
			except frecuenciaDistribucion.DoesNotExist:
				mensaje = {"mensaje":"error en los datos"}

		return HttpResponse(json.dumps(mensaje,indent=4),content_type="application/json")
