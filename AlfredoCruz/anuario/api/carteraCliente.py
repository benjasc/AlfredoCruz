import json
from django.conf.urls import url, include
from anuario.models import carteraCliente, cliente, instrumento,tipoInversion,fondo,bindex
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http import HttpResponse

@api_view(['GET','POST','PUT'])
def apiCarteraCliente(request,id=None):
	if request.method == 'GET':
		if id is not None:
			try:
				lista=[]
				query = carteraCliente.objects.values('id','monto','fecha','cliente__nombre','tipoInversion__nombre').get(pk=id)
				fecha = str(query['fecha'])
				lista.append({
					'id':query['id'],
                    'monto':query['monto'],
                    'fecha':fecha,
                    'cliente':query['cliente__nombre'],
                    'tipoInversion':query['tipoInversion__nombre'],
					})

			except carteraCliente.DoesNotExist:
				lista = {"mensaje":"No existen datos"}

		else:
			try:
				lista=[]
				query = carteraCliente.objects.all().values('id','monto','fecha','cliente__nombre','tipoInversion__nombre')
				if query.count()>0:
					for x in query:
						fecha = str(x['fecha'])
						lista.append({
							'id':x['id'],
		                    'monto':x['monto'],
		                    'fecha':fecha,
		                    'cliente':x['cliente__nombre'],
		                    'tipoInversion':x['tipoInversion__nombre'],
							})
				else:
					lista = {"mensaje":"No existen datos"}
			except carteraCliente.DoesNotExist:
				pass

		return HttpResponse(json.dumps(lista,indent=4),content_type="application/json")

	elif request.method == 'POST':
		flag = False
		mensaje = ""
		fecha= request.data['fecha']
		saldo= request.data['saldo']

		cli= request.data['cliente']
		tipoinversion = request.data['tipoInversion']

		nombre_fondo = request.data['fondo']
		clase_proveedor = request.data['clase_proveedor']

		if fecha=='' or saldo=='' or cli=='' or tipoinversion=='' or nombre_fondo =='' or clase_proveedor=='':
			mensaje = {"mensaje":"Debes completar todos los campos"}
		else:

			try:
				c = cliente.objects.get(nombre=cli)
				if c.count()>0:
					flag = True
				else:
					flag = False
			except cliente.DoesNotExist:
				c = None

			try:
				ti = tipoInversion.objects.get(nombre=tipoinversion)
				if ti.count()>0 and flag==True:


			except tipoInversion.DoesNotExist:
				ti = None

			try:
				f = fondo.objects.get(nombre=nombre_fondo)
			except fondo.DoesNotExist:
				f = None

			try:
				i = instrumento.objects.values('bindex').filter(fondo=f,clase_proveedor=clase_proveedor)
				b = bindex.objects.get(pk=i[0]['bindex'])
			except bindex.DoesNotExist:
				mensaje={"mensaje":"Datos incorrectos"}

			try:

				carteracli = carteraCliente(fecha=fecha,monto=saldo,cliente=c,tipoInversion=ti,bindex=b)
				carteracli.save()
				mensaje = {"mensaje":"Datos guardados con exito"}
			except:
				pass
		return HttpResponse(json.dumps(mensaje,indent=4),content_type="application/json")
