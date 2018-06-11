import json
from django.conf.urls import url, include
from anuario.models import sector,bindex,instrumento,fondo
from rest_framework.decorators import api_view
from django.http import HttpResponse

@api_view(['GET','POST','PUT'])
def apiSector(request,id=None):
	if request.method == 'GET':
		if id is not None:
			try:
				lista=[]
				query =sector.objects.values('materiales_basicos','servicio_comunicacion','ciclico_consumidor'
				,'defensa_consumidor','energia','servicios_financieros','cuidado_salud','acciones_industriales','bienes_raices'
				,'tecnologia','utilidades','portafolio_fecha').get(pk=id)
				lista.append({
					'materiales_basicos':query['materiales_basicos'],
					'servicio_comunicacion':query['servicio_comunicacion'],
					'ciclico_consumidor':query['ciclico_consumidor'],
					'defensa_consumidor':query['defensa_consumidor'],
					'energia':query['energia'],
					'servicios_financieros':query['servicios_financieros'],
					'cuidado_salud':query['cuidado_salud'],
					'acciones_industriales':query['acciones_industriales'],
					'bienes_raices':query['bienes_raices'],
					'tecnologia':query['tecnologia'],
					'utilidades':query['utilidades'],
					'portafolio_fecha':str(query['portafolio_fecha']),
					})
			except sector.DoesNotExist:
				lista = {"mensaje":"No existen datos"}

		else:
			try:
				lista=[]
				query = sector.objects.values('materiales_basicos','servicio_comunicacion','ciclico_consumidor'
				,'defensa_consumidor','energia','servicios_financieros','cuidado_salud','acciones_industriales','bienes_raices'
				,'tecnologia','utilidades','portafolio_fecha')
				if query.count()>0:
					for x in query:
						lista.append({
							'materiales_basicos':x['materiales_basicos'],
							'servicio_comunicacion':x['servicio_comunicacion'],
							'ciclico_consumidor':x['ciclico_consumidor'],
							'defensa_consumidor':x['defensa_consumidor'],
							'energia':x['energia'],
							'servicios_financieros':x['servicios_financieros'],
							'cuidado_salud':x['cuidado_salud'],
							'acciones_industriales':x['acciones_industriales'],
							'bienes_raices':x['bienes_raices'],
							'tecnologia':x['tecnologia'],
							'utilidades':x['utilidades'],
							'portafolio_fecha':str(x['portafolio_fecha']),
							})
				else:
					lista = {"mensaje":"No existen datos"}

			except sector.DoesNotExist:
				pass


		return HttpResponse(json.dumps(lista,indent=4),content_type="application/json")

	elif request.method == 'POST':

		mensaje = ""
		flag=True

		materiales_basicos = request.data['materiales_basicos']
		servicio_comunicacion= request.data['servicio_comunicacion']
		ciclico_consumidor=request.data['ciclico_consumidor']
		defensa_consumidor = request.data['defensa_consumidor']
		energia = request.data['energia']
		servicios_financieros = request.data['servicios_financieros']
		cuidado_salud= request.data['cuidado_salud']
		acciones_industriales=request.data['acciones_industriales']
		bienes_raices = request.data['bienes_raices']
		tecnologia = request.data['tecnologia']
		utilidades = request.data['utilidades']
		portafolio_fecha= request.data['portafolio_fecha']


		nombre_fondo = request.data['fondo']
		clase_proveedor = request.data['clase_proveedor']


		try:
			f = fondo.objects.get(nombre=nombre_fondo)
		except fondo.DoesNotExist:
			flag = False
			mensaje = {"mensaje":"error en los datos"}

		try:
			if flag==True:
				i = instrumento.objects.get(fondo=f,clase_proveedor=clase_proveedor)
		except instrumento.DoesNotExist:
			flag = False
			mensaje = {"mensaje":"error en los datos"}


		try:
			if flag==True:
				b = bindex.objects.get(pk=i.bindex_id)
				query = sector.objects.filter(bindex=b,materiales_basicos=materiales_basicos,servicio_comunicacion=servicio_comunicacion,ciclico_consumidor=ciclico_consumidor,defensa_consumidor=defensa_consumidor,energia=energia
				,servicios_financieros=servicios_financieros,cuidado_salud=cuidado_salud,acciones_industriales=acciones_industriales,bienes_raices=bienes_raices,tecnologia=tecnologia,utilidades=utilidades,portafolio_fecha=portafolio_fecha)
				if query.count()>0:
					mensaje = {"mensaje":"El cliente que intentas crear ya existe"}
				else:
					b = bindex.objects.get(pk=i.bindex_id)
					sec = sector(bindex=b,materiales_basicos=materiales_basicos,servicio_comunicacion=servicio_comunicacion,ciclico_consumidor=ciclico_consumidor,defensa_consumidor=defensa_consumidor,energia=energia
					,servicios_financieros=servicios_financieros,cuidado_salud=cuidado_salud,acciones_industriales=acciones_industriales,bienes_raices=bienes_raices,tecnologia=tecnologia,utilidades=utilidades,portafolio_fecha=portafolio_fecha)
					sec.save()
					mensaje = {"mensaje":"Datos guardados con exito"}
		except bindex.DoesNotExist:
			mensaje = {"mensaje":"error en los datos"}

		return HttpResponse(json.dumps(mensaje,indent=4),content_type="application/json")
