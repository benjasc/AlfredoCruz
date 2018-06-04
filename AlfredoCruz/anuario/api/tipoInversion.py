import json
from django.conf.urls import url, include
from anuario.models import tipoInversion
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http import HttpResponse

@api_view(['GET','POST'])
def apiTipoInversion(request,id=None):
	if request.method == 'GET':
		query = tipoInversion.objects.all().values('nombre')
		return Response(json.dumps(list(query),indent=4))
	elif request.method == 'POST':
		nombre = request.data['nombre']
		tipoinversion = tipoInversion(nombre=nombre)
		tipoinversion.save()
		return Response({'mensaje':'Datos guardados con exito'})
