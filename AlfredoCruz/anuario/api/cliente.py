import json
from django.conf.urls import url, include
from anuario.models import cliente
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http import HttpResponse

@api_view(['GET','POST','PUT'])
def apiCliente(request,id=None):
	if request.method == 'GET':
		if id is not None:
			try:
				query = cliente.objects.values('id','nombre','Amaterno','Apaterno').get(pk=id)
				print(query)
			except cliente.DoesNotExist:
				query = {"mensaje":"No existen datos"}
		else:
			query = cliente.objects.all().values('id','nombre','Amaterno','Apaterno')

		return HttpResponse(json.dumps(query,indent=4),content_type="application/json")

	elif request.method == 'POST':
		idcli = request.data['idcliente']
		nombre = request.data['nombre']
		Apaterno = request.data['Apaterno']
		Amaterno = request.data['Amaterno']
		cli = cliente(id=idcli,Apaterno=Apaterno,Amaterno=Amaterno)
		cli.save()
		return Response({'mensaje':'Registro guardado con exito'})

	elif request.method == 'PUT':
		nombre = request.data['nombre']
		Apaterno = request.data['Apaterno']
		Amaterno = request.data['Amaterno']
		cli = cliente(id=id,nombre=nombre,Apaterno=Apaterno,Amaterno=Amaterno)
		cli.save()
		return Response({'mensaje':'Registro actualizado con exito'})
