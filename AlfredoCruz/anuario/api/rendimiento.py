import json
from django.conf.urls import url, include
from anuario.models import rendimiento
from rest_framework.decorators import api_view
from django.http import HttpResponse

@api_view(['GET','POST','PUT'])
def apiRendimiento(request,id=None):
	if request.method == 'GET':
		if id is not None:
			try:
				query =rendimiento.objects.values('id','estado').get(pk=id)

			except rendimiento.DoesNotExist:
				query = {"mensaje":"No existen datos"}

		else:
			try:
				query = rendimiento.objects.all()
				if query.count()<1:
					query = {"mensaje":"No existen datos"}
				else:
					query = list(rendimiento.objects.all().values('id','estado'))

			except rendimiento.DoesNotExist:
				pass


		return HttpResponse(json.dumps(query,indent=4),content_type="application/json")

	elif request.method == 'POST':

		mensaje = ""

		rendimiento_id = request.data['rendimiento_id']
		estado= request.data['estado']

		if rendimiento_id=='' or estado=='':
			mensaje = {"mensaje":"Debes completar todos los campos"}
		else:
			try:
				query =rendimiento.objects.filter(pk=rendimiento_id,estado=estado)
				if query.count()>0:
					mensaje = {"mensaje":"El cliente que intentas crear ya existe"}
				else:
					ren = rendimiento(id=rendimiento_id,estado=estado)
					ren.save()
					mensaje = {"mensaje":"Datos guardados con exito"}
			except rendimiento.DoesNotExist:
				mensaje = {"mensaje":"error en los datos"}

		return HttpResponse(json.dumps(mensaje,indent=4),content_type="application/json")
