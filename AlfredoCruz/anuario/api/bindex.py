import json
from django.conf.urls import url, include
from anuario.models import asignacionActivo,fondo,instrumento,bindex
from rest_framework.decorators import api_view
from django.http import HttpResponse

@api_view(['GET','POST','PUT'])
def apiBindex(request,id=None):
	if request.method == 'GET':
		if id is not None:
			try:
				query = bindex.objects.values('id','morningstar_id').get(pk=id)

			except bindex.DoesNotExist:
				query = {"mensaje":"No existen datos"}

		else:
			try:
				query = bindex.objects.all().values('id','morningstar_id')
				if query.count()<1:
					query = {"mensaje":"No existen datos"}
				else:
					query = list(bindex.objects.all().values('id','morningstar_id'))

			except bindex.DoesNotExist:
				pass


		return HttpResponse(json.dumps(query,indent=4),content_type="application/json")

	elif request.method == 'POST':

		mensaje = ""

		bindex_id = request.data['bindex_id']
		morningstar_id= request.data['morningstar_id']

		if bindex_id=='' or morningstar_id=='':
			mensaje = {"mensaje":"Debes completar todos los campos"}
		else:
			try:
				query = bindex.objects.filter(pk=bindex_id,morningstar_id=morningstar_id)
				if query.count()>0:
					mensaje = {"mensaje":"El cliente que intentas crear ya existe"}
				else:
					bdx = bindex(id=bindex_id,morningstar_id=morningstar_id)
					bdx.save()
					mensaje = {"mensaje":"Datos guardados con exito"}
			except bindex.DoesNotExist:
				mensaje = {"mensaje":"error en los datos"}

		return HttpResponse(json.dumps(mensaje,indent=4),content_type="application/json")
