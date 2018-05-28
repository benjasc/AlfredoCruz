from anuario.models import cliente, movimiento, saldoActualizado,saldoMensual, instrumento
from rest_framework import serializers
from django.db.models import Sum, Q,Count,Case, CharField, Value, When, F, IntegerField
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import HttpResponse
from datetime import datetime, date, time, timedelta
import json
import calendar



def evolucionPatrimonio(request,id,fecha=None):
    if fecha == None:
        fecha = datetime.today().strftime("%d-%m-%Y")
        '''
        print(fecha)
    else:
        fecha= datetime.today().strftime("%d-%m-%Y")
 		'''   
    ls=fecha.split('-')
    #fecha = (ls[2]+'-' +ls[1]+'-'+ls[0])
 

    anio_actual = ls[2]
    mes_actual = ls[1]
    anio_anterior = int(ls[2])-1
    lista = ['evolucion Patrimonio']

    total = saldoMensual.objects.values('cliente__nombre','tipoInversion__nombre','anio','mes','saldoCierre').filter(cliente=id).filter(Q(tipoInversion=1)|Q(tipoInversion=2))
    total = total.filter(Q(anio=anio_actual,mes__lte=mes_actual) | (Q(anio=anio_anterior,mes__gte=mes_actual)) )#cota inferior
    for x in total:
        lista.append({
        'cliente':x['cliente__nombre'],
        'tipoInversion':x['tipoInversion__nombre'],
        'anio':x['anio'],
        'mes':x['mes'],
        'saldoCierre':x['saldoCierre'],
        })

    #return HttpResponse(json.dumps(lista,indent=4),content_type="application/json")
    return lista




def totalesConsolidados(request,id,fecha=None):
	if fecha == None:
		fecha = datetime.today().strftime("%d-%m-%Y")
	ls=fecha.split('-')
	anio_actual = ls[2]
	mes_actual = ls[1]
    
#    if fecha == None:
    #    fecha = datetime.datetime.now()

    #else:
        #fecha= datetime.datetime.strptime(fecha,'%d-%m-%Y')


#    anio_actual = fecha.year
    #mes_actual = fecha.month

	query = saldoMensual.objects.values('saldoCierre','cliente__nombre','tipoInversion__nombre','anio','mes')
	query =	query.filter(cliente=id)
	query = query.filter(anio=anio_actual,mes=mes_actual)

	lista=['totales Consolidados']
	montoTotal=0
	for x in query:
	    montoTotal += x['saldoCierre']

	for y in query:
	    lista.append({
        'cliente':y['cliente__nombre'],
        'tipoInversion':y['tipoInversion__nombre'],
        'anio':y['anio'],
        'mes':y['mes'],
	    'monto':y['saldoCierre'],
        'porcentaje':round(((y['saldoCierre']*100)/montoTotal), 2),
        })
	return lista
	#return HttpResponse(json.dumps(lista,indent=4),content_type="application/json")

def cartolasConsolidadas(request, id):

	#obtener fondos, tipoInversion y agrupados por branding
	
	#fecha = datetime.today().strftime("%Y-%m-%d")
	#print(fecha)

	querySet = movimiento.objects.filter(cliente=id).values('monto','bindex','tipoInversion__nombre','tipoMovimiento')
	lista = []

	for s in querySet:
		#print(s)

		try:
			monto=s['monto']
			aportes=0
			retiros=0
			i = instrumento.objects.get(pk=s['bindex'])

			if s['tipoMovimiento']==3:
				monto = monto*-1
				retiros=s['monto']
			elif s['tipoMovimiento']==2:
				aportes=s['monto']

			flag = False
			for x in lista:
				if x['administradora'] == i.branding.nombre and x['tipoInversion'] == s['tipoInversion__nombre']  and  x['fondo']== i.fondo.nombre_legal:
					x['saldoActual'] += monto
					x['totalAporte'] +=aportes
					x['totalRetiro'] +=retiros

					flag = True

			if flag == False:
				#[i.branding.nombre,s['monto'], s['tipoInversion__nombre'],i.fondo.nombre_legal,totalAporte,totalRetiro]
				lista.append({
				'administradora' : i.branding.nombre,
				'saldoActual'   : monto,
				'tipoInversion': s['tipoInversion__nombre'],
				'fondo'	 		 : i.fondo.nombre_legal,
				'totalAporte'	 : aportes,
				'totalRetiro'	 : retiros,
				})

		except instrumento.DoesNotExist:
			pass

	lista.sort(key=lambda l:l['administradora'])

	aux =lista[0]['administradora']
	suma = 0
	totalAportes=0
	totalRetiros=0
	for l in range(len(lista)+1):

		if(lista[l]['administradora'] == aux):
			suma += lista[l]['saldoActual']
			totalAportes+=lista[l]['totalAporte']
			totalRetiros+=lista[l]['totalRetiro']
		else:
			aux= lista[l]['administradora']
			#lista.append([ str(lista[l-1]['Administradora']) + " - TOTAL", suma, ''])
			lista.append({
			'administradora' : lista[l-1]['administradora'],
			'saldoActual'   : suma,
			'totalAporte'	 : totalAportes,
			'totalRetiro'	 : totalRetiros,
			})
			totalAportes=0
			totalAportes+=lista[l]['totalAporte']
			totalRetiros=0
			totalRetiros+=lista[l]['totalRetiro']
			suma = 0
			suma += lista[l]['saldoActual']

	lista.sort(key=lambda l:l['administradora'])
	#lista.insert(0,'cartolas Consolidadas')
	return lista
	#return HttpResponse(json.dumps(lista,indent=4),content_type="application/json")

def resumenFondo(request, id):

	lista = []
	querySet = movimiento.objects.filter(cliente=id)
	for s in querySet:
		try:
			i = instrumento.objects.get(pk=s.bindex)
			flag = False
			for x in lista:
				if x['nombreTipoInstrumento'] == i.tipoInstrumento.nombre:
					if s.tipoMovimiento_id==3:
						x['porcentaje'] -= s.monto
					else:
						x['porcentaje'] += s.monto
					flag = True
			if flag == False:
				#lista1.append([i.tipoInstrumento.nombre, s.monto])
				lista.append({'nombreTipoInstrumento': i.tipoInstrumento.nombre,'porcentaje': s.monto})

		except instrumento.DoesNotExist:
			pass

	aux = 0
	for l in lista:
		aux += l['porcentaje']
	for l in lista:
		l['porcentaje'] = l['porcentaje']*100/aux
	lista.insert(0,'resumen Fondo')
	return lista 

def resumenMoneda(request, id):
	querySet = movimiento.objects.filter(cliente=id)
	lista = []
	for s in querySet:
		try:
			i = instrumento.objects.get(pk=s.bindex)
			flag = False

			for x in lista:
				if x['moneda'] == i.fondo.moneda.nombre:
					if s.tipoMovimiento_id==3:
						x['porcentaje'] -= s.monto
					else:
						x['porcentaje'] += s.monto
					flag = True
			if flag == False:
				lista.append({'moneda':i.fondo.moneda.nombre,
				'porcentaje': s.monto})

		except instrumento.DoesNotExist:
			pass

	aux = 0
	for l in lista:
		aux += l['porcentaje']
	for l in lista:
		l['porcentaje'] = l['porcentaje']*100/aux

	lista.insert(0,'resumen Moneda')
	
	return lista

def resumenBranding(request, id):
	querySet = movimiento.objects.filter(cliente=id)
	lista = []

	for s in querySet:
		try:
			i = instrumento.objects.get(pk=s.bindex)
			flag = False
			for x in lista:
				if x['institucion'] == i.branding.nombre:
					if s.tipoMovimiento_id==3:
						x['porcentaje'] -= s.monto
					else:
						x['porcentaje'] += s.monto
					flag = True
			if flag == False:
				lista.append({'institucion':i.branding.nombre,
				'porcentaje': s.monto})

		except instrumento.DoesNotExist:
			pass

	aux = 0
	for l in lista:
		aux += l['porcentaje']
	for l in lista:
		l['porcentaje'] = l['porcentaje']*100/aux
	lista.insert(0,'resumen Instituciones')
	return lista

def patrimonioConsolidado(request, id, fecha=None):
	lista = ['patrimonio Consolidado']
	if fecha is None:
		fecha=datetime.today().strftime("%d-%m-%Y")
		
	ls = fecha.split('-')
	fecha = ls[2]+'-' +ls[1]+'-'+ls[0]
	
	query = saldoActualizado.objects.filter(cliente=id, fecha=fecha ).values('cliente__nombre', 'monto', 'tipoInversion__nombre').order_by('tipoInversion')
	for s in query:
		lista.append({
			'cliente':s['cliente__nombre'],
			'monto':s['monto'],
			'tipoInversion':s['tipoInversion__nombre'],
			})

	return lista
	#return HttpResponse(json.dumps(lista, indent=4), content_type="application/json")
def resumenCuentas(request, id, fecha=None):
	lista = ['resumen Cuentas']

	if fecha is None:
		fecha=datetime.today().strftime("%d-%m-%Y")
	ls = fecha.split('-')
	print(ls)
	qPresente = saldoMensual.objects.filter(cliente=id, anio=ls[2], mes=ls[1])

	for s in list(qPresente):
		#lista.append(s.tipoInversion.nombre+'  '+str(s.variacion())+' '+str(s.porcentaje_variacion()))
		lista.append({
			'tipoInversion':s.tipoInversion.nombre,
			'variacion':s.variacion(),
			'porcentaje':s.porcentaje_variacion(),
			})


	return lista
	#return HttpResponse(json.dumps(lista, indent=4), content_type="application/json")


def resumenCompletoDia(request, id):
	lista = ['resumenCompletoDia']
	
	hoy = date.today()
	qPresente = saldoActualizado.objects.filter(cliente=id, fecha=hoy)
	for s in qPresente:
		lista.append({
			'monto':s.monto,
			'variacion':s.variacionDia(),
			})
	return lista
	#return HttpResponse( json.dumps(lista))
	

def graficos(request,id,fecha=None):#en este metodo llamamos a todos los metodos con sus respectivos graficos
	a=patrimonioConsolidado(request, id, fecha=None)
	b=evolucionPatrimonio(request,id,fecha=None)
	c=resumenCuentas(request, id)
	d=totalesConsolidados(request, id,fecha=None)
	e=resumenCompletoDia(request, id)
	f=resumenFondo(request, id)
	g=resumenMoneda(request, id)
	h=resumenBranding(request, id)
	resumen=['resumenes', f,g,h]
	i=cartolasConsolidadas(request, id)
	x=[a,b,c,d,e,resumen,i]

	return HttpResponse(json.dumps(x,indent=4),content_type="application/json")
