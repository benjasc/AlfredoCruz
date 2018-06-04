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
			query = list(cliente.objects.all().values('id','nombre','Amaterno','Apaterno'))

		return HttpResponse(json.dumps(query,indent=4),content_type="application/json")

	elif request.method == 'POST':
		try:
			idcli = request.data['idcliente']
			nombre = request.data['nombre']
			Apaterno = request.data['Apaterno']
			Amaterno = request.data['Amaterno']
			mensaje = ""
			query = cliente.objects.filter(id=idcli)
			if idcli == '' or nombre=='' or Apaterno=='' or Amaterno=='':
				mensaje = {"mensaje":"Debes completar todos los campos"}

			elif query.count()>0 :
				mensaje = {"mensaje":"El cliente que intentas crear ya existe"}

			else:
				cli = cliente(id=idcli,nombre=nombre,Apaterno=Apaterno,Amaterno=Amaterno)
				cli.save()
				mensaje = {"mensaje":"Datos guardados exitosamente"}

		except:
			pass

		return HttpResponse(json.dumps(mensaje,indent=4),content_type="application/json")

	elif request.method == 'PUT':
		try:
			idcli = request.data['idcliente']
			nombre = request.data['nombre']
			Apaterno = request.data['Apaterno']
			Amaterno = request.data['Amaterno']
			mensaje = ""
			if idcli == '' or nombre=='' or Apaterno=='' or Amaterno=='':
				mensaje = {"mensaje":"Debes completar todos los campos"}

			else:
				cli = cliente(id=idcli,nombre=nombre,Apaterno=Apaterno,Amaterno=Amaterno)
				cli.save()
				mensaje = {"mensaje":"Datos actualizados exitosamente"}

		except:
			pass

		return HttpResponse(json.dumps(mensaje,indent=4),content_type="application/json")
