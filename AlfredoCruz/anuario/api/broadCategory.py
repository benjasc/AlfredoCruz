import json
from django.conf.urls import url, include
from anuario.models import broadCategory
from rest_framework.decorators import api_view
from django.http import HttpResponse

@api_view(['GET','POST','PUT'])
def apiBroadCategory(request,id=None):
	if request.method == 'GET':
		if id is not None:
			try:
				query =broadCategory.objects.values('id','nombre').get(pk=id)

			except broadCategory.DoesNotExist:
				query = {"mensaje":"No existen datos"}

		else:
			try:
				query = broadCategory.objects.all().values('id','nombre')
				if query.count()<1:
					query = {"mensaje":"No existen datos"}
				else:
					query = list(broadCategory.objects.all().values('id','nombre'))

			except broadCategory.DoesNotExist:
				pass


		return HttpResponse(json.dumps(query,indent=4),content_type="application/json")

	elif request.method == 'POST':

		mensaje = ""

		broadCategory_id = request.data['broadCategory_id']
		nombre= request.data['nombre']

		if broadCategory_id=='' or nombre=='':
			mensaje = {"mensaje":"Debes completar todos los campos"}
		else:
			try:
				query =broadCategory.objects.filter(pk=broadCategory_id,nombre=nombre)
				if query.count()>0:
					mensaje = {"mensaje":"El cliente que intentas crear ya existe"}
				else:
					brocat = broadCategory(id=broadCategory_id,nombre=nombre)
					brocat.save()
					mensaje = {"mensaje":"Datos guardados con exito"}
			except broadCategory.DoesNotExist:
				mensaje = {"mensaje":"error en los datos"}

		return HttpResponse(json.dumps(mensaje,indent=4),content_type="application/json")
