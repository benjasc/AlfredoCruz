import json
from django.conf.urls import url, include
from anuario.models import carteraCliente
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http import HttpResponse

@api_view(['GET','POST','PUT'])
def apiCarteraCliente(request,id=None):
	if request.method == 'GET':
		if id is not None:
			try:
				mensaje = ""
				lista=[]
				query = carteraCliente.objects.values('id','fecha','cliente__nombre','tipoInversion__nombre').filter(pk=id)
				for x in query:
					fecha = str(x['fecha'])
					lista.append({
						'id':x['id'],
	                    'monto':x['monto'],
	                    'fecha':fecha,
	                    'cliente':x['cliente__nombre'],
	                    'tipoInversion':x['tipoInversion__nombre'],  
						})
                
			except carteraCliente.DoesNotExist:
				query = {"mensaje":"No existen datos"}

		else:
			try:

				lista=[]
				query = carteraCliente.objects.values('id','fecha','cliente__nombre','tipoInversion__nombre').filter(pk=id)
				for x in query:
					fecha = str(x['fecha'])
					lista.append({
						'id':x['id'],
	                    'monto':x['monto'],
	                    'fecha':fecha,
	                    'cliente':x['cliente__nombre'],
	                    'tipoInversion':x['tipoInversion__nombre'],  
						})
			except carteraCliente.DoesNotExist:
				query = {"mensaje":"No existen datos"}

		return HttpResponse(json.dumps(query,indent=4),content_type="application/json")


                

