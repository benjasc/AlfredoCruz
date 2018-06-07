import json
from django.conf.urls import url, include
from anuario.models import cliente, instrumento,tipoInversion,fondo,bindex,saldoMensual
from rest_framework.decorators import api_view
from django.http import HttpResponse

@api_view(['GET','POST'])
def apiSaldoMensual(request,id=None):
	if request.method == 'GET':
		if id is not None:
			try:
				lista=[]
				query = saldoMensual.objects.values('id','saldoCierre','anio','mes','cliente__nombre','tipoInversion__nombre').get(pk=id)
				lista.append({
					'id':query['id'],
                    'monto':query['saldoCierre'],
                    'anio':query['anio'],
                    'mes':query['mes'],
                    'cliente':query['cliente__nombre'],
                    'tipoInversion':query['tipoInversion__nombre'],
					})

			except saldoMensual.DoesNotExist:
				lista = {"mensaje":"No existen datos"}

		else:
			try:
				lista=[]
				query = saldoMensual.objects.all().values('id','saldoCierre','anio','mes','cliente__nombre','tipoInversion__nombre')
				if query.count()>0:
					for x in query:
						lista.append({
							'id':x['id'],
                            'monto':x['saldoCierre'],
                            'anio':x['anio'],
                            'mes':x['mes'],
                            'cliente':x['cliente__nombre'],
                            'tipoInversion':x['tipoInversion__nombre'],
							})
				else:
					lista = {"mensaje":"No existen datos"}
			except saldoMensual.DoesNotExist:
				pass

		return HttpResponse(json.dumps(lista,indent=4),content_type="application/json")

	elif request.method == 'POST':
		flag = True
		mensaje = ""

		anio= request.data['anio']
		mes= request.data['mes']
		saldoCierre=request.data['saldoCierre']

		cli= request.data['cliente']
		tipoinversion = request.data['tipoInversion']


		if anio=='' or mes=='' or cli=='' or tipoinversion=='' or saldoCierre =='':
			mensaje = {"mensaje":"Debes completar todos los campos"}
		else:
			try:
				c = cliente.objects.get(nombre=cli)
			except cliente.DoesNotExist:
				flag = False

			try:
				if flag==True:
					ti = tipoInversion.objects.get(nombre=tipoinversion)
			except tipoInversion.DoesNotExist:
				flag = False

			try:
				if flag==True:
					salmen=saldoMensual(anio=anio,mes=mes,saldoCierre=saldoCierre,tipoInversion=ti,cliente=c)
					salmen.save()
					mensaje = {"mensaje":"Datos guardados con exito"}

				else:
					mensaje = {"mensaje":"error en los datos"}
			except:
				mensaje = {"mensaje":"error en los datos2"}
		return HttpResponse(json.dumps(mensaje,indent=4),content_type="application/json")
