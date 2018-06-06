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
		fecha= request.data['fecha']
		monto= request.data['monto']

		cli= request.data['cliente']
		tipoinversion = request.data['tipoInversion']

		nombre_fondo = request.data['fondo']
		clase_proveedor = request.data['clase_proveedor']

		if fecha=='' or monto=='' or cli=='' or tipoinversion=='' or nombre_fondo =='' or clase_proveedor=='':
			mensaje = {"mensaje":"Debes completar todos los campos"}
		else:
			f = fondo.objects.filter(nombre=nombre_fondo)
			if f.count()>0:
				flag = True
			else:
				flag = False

			ti = tipoInversion.objects.filter(nombre=tipoinversion)
			if ti.count()>0 and flag ==True:
				flag = True
			else:
				flag = False

			c = cliente.objects.filter(nombre=cli)
			if c.count()>0 and flag ==True:
				flag = True
			else:
				flag = False

			if flag==True:
				inst = instrumento.objects.filter(fondo=f[0],clase_proveedor=clase_proveedor)
				if inst.count()>0:
					b =  bindex.objects.get(pk=inst[0].bindex_id)
					salact = saldoActualizado(monto=monto,fecha=fecha,cliente=c[0],tipoInversion=ti[0],bindex=b)
					salact.save()
					mensaje = {"mensaje":"Datos guardados con exito"}
				else:
					mensaje = {"mensaje":"error en los datos"}
			else:
				mensaje = {"mensaje":"error en los datos"}
		return HttpResponse(json.dumps(mensaje,indent=4),content_type="application/json")
