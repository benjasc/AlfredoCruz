import json
from django.conf.urls import url, include
from anuario.models import tipoMovimiento
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http import HttpResponse

@api_view(['GET','POST'])
def apiTipoMovimiento(request,id=None):
	if request.method == 'GET':
		query = tipoMovimiento.objects.all().values('nombre')
		return Response(json.dumps(list(query),indent=4))
	elif request.method == 'POST':
		nombre = request.data['nombre']
		tipomovimiento = tipoMovimiento(nombre=nombre)
		tipomovimiento.save()
		return Response({'mensaje':'Datos guardados con exito'})
