import json
from django.conf.urls import url, include
from anuario.models import tipoInstrumento
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http import HttpResponse

@api_view(['GET','POST'])
def apiTipoInstrumento(request,id=None):
	if request.method == 'GET':
		query = tipoInstrumento.objects.all().values('nombre')
		return Response(json.dumps(list(query),indent=4))
	elif request.method == 'POST':
		id = request.data['id']
		nombre = request.data['nombre']
		tipoinstrumento = tipoInstrumento(pk=id,nombre=nombre)
		tipoinstrumento.save()
		return Response({'mensaje':'Datos guardados con exito'})
