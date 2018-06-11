import json
from django.conf.urls import url, include
from anuario.models import instrumento,branding,fondo,tipoInstrumento,rendimiento,proveedor,frecuenciaDistribucion,bindex
from rest_framework.decorators import api_view
from django.http import HttpResponse

@api_view(['GET','POST','PUT'])
def apiInstrumento(request,id=None):
	if request.method == 'GET':
		if id is not None:
			try:
				lista=[]
				query = instrumento.objects.values('bindex','nombre','run_svs','clase_proveedor','operation_ready','branding__nombre','fondo__nombre','frecuenciaDistribucion__frecuencia','proveedor__nombre','rendimiento__estado','tipoInstrumento__nombre').get(pk=id)
				lista.append({
					'id':query['bindex'],
					'nombre':query['nombre'],
					'run_svs':query['run_svs'],
					'clase_proveedor':query['clase_proveedor'],
					'operation_ready':query['operation_ready'],
					'branding':query['branding__nombre'],
					'fondo':query['fondo__nombre'],
					'frecuenciaDistribucion':query['frecuenciaDistribucion__frecuencia'],
					'proveedor':query['proveedor__nombre'],
					'rendimiento':query['rendimiento__estado'],
					'tipoInstrumento':query['tipoInstrumento__nombre'],
					})
			except instrumento.DoesNotExist:
				query = {"mensaje":"No existen datos"}

		else:
			try:
				lista=[]
				query = instrumento.objects.all().values('bindex','nombre','run_svs','clase_proveedor','operation_ready','branding__nombre','fondo__nombre','frecuenciaDistribucion__frecuencia','proveedor__nombre','rendimiento__estado','tipoInstrumento__nombre')
				if query.count()>0:
					for x in query:
						lista.append({
							'id':x['bindex'],
							'nombre':x['nombre'],
							'run_svs':x['run_svs'],
							'clase_proveedor':x['clase_proveedor'],
							'operation_ready':x['operation_ready'],
							'branding':x['branding__nombre'],
							'fondo':x['fondo__nombre'],
							'frecuenciaDistribucion':x['frecuenciaDistribucion__frecuencia'],
							'proveedor':x['proveedor__nombre'],
							'rendimiento':x['rendimiento__estado'],
							'tipoInstrumento':x['tipoInstrumento__nombre'],
							})
				else:
					lista = {"mensaje":"No existen datos"}
			except instrumento.DoesNotExist:
				pass


		return HttpResponse(json.dumps(lista,indent=4),content_type="application/json")

	elif request.method == 'POST':
		flag = True
		mensaje = ""

		nombre= request.data['nombre']
		run_svs=request.data['run_svs']
		clase_proveedor= request.data['clase_proveedor']
		operation_ready= request.data['operation_ready']

		bra=request.data['branding']
		fon=request.data['fondo']
		fredis = request.data['frecuenciaDistribucion']
		pro = request.data['proveedor']
		ren = request.data['rendimiento']
		tipins = request.data['tipoInstrumento']



		if  run_svs=='' or clase_proveedor=='' or operation_ready=='' or bra ==''or fon ==''or fredis ==''or pro ==''or ren ==''or tipins =='':
			mensaje = {"mensaje":"Debes completar todos los campos"}
		else:
			try:
				f = fondo.objects.get(nombre=fon)
			except fondo.DoesNotExist:
				flag = False
				mensaje = {"mensaje":"error en los datos"}

			try:
				if flag==True:
					b = branding.objects.get(nombre=bra)
			except branding.DoesNotExist:
				flag = False
				mensaje = {"mensaje":"error en los datos"}

			try:
				if flag==True:
					fd = frecuenciaDistribucion.objects.get(frecuencia=fredis)
			except frecuenciaDistribucion.DoesNotExist:
				flag = False
				mensaje = {"mensaje":"error en los datos"}

			try:
				if flag==True:
					p = proveedor.objects.get(nombre=pro)
			except proveedor.DoesNotExist:
				flag = False
				mensaje = {"mensaje":"error en los datos"}

			try:
				if flag==True:
					r = rendimiento.objects.get(estado=ren)
			except rendimiento.DoesNotExist:
				flag = False
				mensaje = {"mensaje":"error en los datos"}

			try:
				if flag==True:
					ti = tipoInstrumento.objects.get(nombre=tipins)
			except tipoInstrumento.DoesNotExist:
				flag = False
				mensaje = {"mensaje":"error en los datos"}

			try:
				if flag==True:
					query = instrumento.objects.get(nombre=nombre,run_svs=run_svs,clase_proveedor=clase_proveedor,operation_ready=operation_ready,branding=b,fondo=f,frecuenciaDistribucion=fd,proveedor=p,rendimiento=r,tipoInstrumento=ti)
					if query.count()>0:
						mensaje = {"mensaje":"El cliente que intentas crear ya existe"}
			except instrumento.DoesNotExist:
				flag = False
				mensaje = {"mensaje":"error en los datos"}



		return HttpResponse(json.dumps(mensaje,indent=4),content_type="application/json")
