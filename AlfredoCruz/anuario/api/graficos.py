from anuario.models import cliente, movimiento, saldoActualizado,saldoMensual, instrumento
from rest_framework import serializers
from django.db.models import Sum, Q,Count,Case, CharField, Value, When, F, IntegerField
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import HttpResponse
import json
from datetime import datetime, date, time, timedelta
import calendar



def evolucionPatrimonio(request,id,fecha=None):
    #if fecha == None:
        #fecha = datetime.datetime.now()
    #else:
        #fecha= datetime.datetime.strptime(fecha,'%d-%m-%Y')

    #anio_actual = fecha.year
    #mes_actual = fecha.month
    #anio_anterior = fecha.year-1

    total = saldoMensual.objects.values('cliente__nombre','tipoInversion__nombre','anio','mes','saldoCierre').filter(cliente=id).filter(Q(tipoInversion=1)|Q(tipoInversion=2))
    #total = total.filter(Q(anio=anio_actual,mes__lte=mes_actual) | (Q(anio=anio_anterior,mes__gte=mes_actual)) )#cota inferior
    list = []
    for x in total:
        list.append({
        'Cliente':x['cliente__nombre'],
        'Tipo_inversion':x['tipoInversion__nombre'],
        'Anio':x['anio'],
        'Mes':x['mes'],
        'Saldo_cierre':x['saldoCierre'],
        })

    #return HttpResponse(json.dumps(list,indent=4),content_type="application/json")
    return list




def totalesConsolidados(request,id,fecha=None):

#    if fecha == None:
    #    fecha = datetime.datetime.now()

    #else:
        #fecha= datetime.datetime.strptime(fecha,'%d-%m-%Y')


#    anio_actual = fecha.year
    #mes_actual = fecha.month

    query = saldoMensual.objects.values('saldoCierre','cliente__nombre','tipoInversion__nombre','anio','mes')
    query =	query.filter(cliente=id)
    #query = query.filter(anio=anio_actual,mes=mes_actual)

    listaa=[]
    montoTotal=0
    for x in query:
	    montoTotal += x['saldoCierre']

    for y in query:
	    listaa.append({
        'Cliente':y['cliente__nombre'],
        'Tipo_inversion':y['tipoInversion__nombre'],
        'Anio':y['anio'],
        'Mes':y['mes'],
	    'Monto':y['saldoCierre'],
        'Porcentaje':round(((y['saldoCierre']*100)/montoTotal), 2),
        })

    return listaa
    #return HttpResponse(json.dumps(list,indent=4),content_type="application/json")


'''

def saldoAct(request):

	query = movimiento.objects.values('tipoInversion','cliente','fecha'
	).annotate(suma=Sum(
					Case(
						When(tipoMovimiento=3
							,then=F('monto')*-1)
							,default=F('monto')
							,output_field=IntegerField()
						)
					)
	).order_by('cliente','fecha','tipoInversion')
		#print(str(x['fecha'])+' || '+str(x['cliente'])+' || '+str(x['tipoInversion'])+' || '+str(x['suma']))
	#return HttpResponse(json.dumps(list(query),indent=4),content_type="application/json")'''

def cartolasConsolidadas(request, id):

	#obtener fondos, tipoInversion y agrupados por branding
	querySet = movimiento.objects.filter(cliente=id).values('monto','bindex','tipoInversion__nombre','tipoMovimiento','fecha')
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
				print('vuelta')
				print(x)
				if x['Administradora'] == i.branding.nombre and x['Tipo_inversion'] == s['tipoInversion__nombre']  and  x['Fondo']== i.fondo.nombre_legal:
					x['Saldo_actual'] += monto
					x['Total_aporte'] +=aportes
					x['Total_retiro'] +=retiros

					flag = True

			if flag == False:
				#[i.branding.nombre,s['monto'], s['tipoInversion__nombre'],i.fondo.nombre_legal,totalAporte,totalRetiro]
				lista.append({
				'Administradora' : i.branding.nombre,
				'Saldo_actual'   : monto,
				'Tipo_inversion': s['tipoInversion__nombre'],
				'Fondo'	 		 : i.fondo.nombre_legal,
				'Total_aporte'	 : aportes,
				'Total_retiro'	 : retiros,
				})

		except instrumento.DoesNotExist:
			pass

	lista.sort(key=lambda l:l['Administradora'])

	aux =lista[0]['Administradora']
	suma = 0
	totalAportes=0
	totalRetiros=0
	for l in range(len(lista)+1):

		if(lista[l]['Administradora'] == aux):
			suma += lista[l]['Saldo_actual']
			totalAportes+=lista[l]['Total_aporte']
			totalRetiros+=lista[l]['Total_retiro']
		else:
			aux= lista[l]['Administradora']
			#lista.append([ str(lista[l-1]['Administradora']) + " - TOTAL", suma, ''])
			lista.append({
			'Administradora' : lista[l-1]['Administradora'],
			'Saldo_actual'   : suma,
			'Total_aporte'	 : totalAportes,
			'Total_retiro'	 : totalRetiros,
			})
			totalAportes=0
			totalAportes+=lista[l]['Total_aporte']
			totalRetiros=0
			totalRetiros+=lista[l]['Total_retiro']
			suma = 0
			suma += lista[l]['Saldo_actual']

	lista.sort(key=lambda l:l['Administradora'])
	return lista

def resumenFondo(request, id):
	querySet1 = movimiento.objects.filter(cliente=id)
	lista1 = []
	for s in querySet1:
		try:
			i = instrumento.objects.get(pk=s.bindex)
			flag = False

			for x in lista1:
				if x[0] == i.tipoInstrumento.nombre:
					if s.tipoMovimiento_id==3:
						x[1] -= s.monto
					else:
						x[1] += s.monto
					flag = True
			if flag == False:
				lista1.append([i.tipoInstrumento.nombre, s.monto])

		except instrumento.DoesNotExist:
			pass

	aux = 0
	for l in lista1:
		aux += l[1]
	for l in lista1:
		l[1] = l[1]*100/aux

	return lista1

def resumenMoneda(request, id):
	querySet = movimiento.objects.filter(cliente=id)
	lista = []
	for s in querySet:
		try:
			i = instrumento.objects.get(pk=s.bindex)
			flag = False

			for x in lista:
				if x[0] == i.fondo.moneda.nombre:
					if s.tipoMovimiento_id==3:
						x[1] -= s.monto
					else:
						x[1] += s.monto
					flag = True
			if flag == False:
				lista.append([i.fondo.moneda.nombre, s.monto])

		except instrumento.DoesNotExist:
			pass

	aux = 0
	for l in lista:
		aux += l[1]
	for l in lista:
		l[1] = l[1]*100/aux

	return lista

def resumenBranding(request, id):
	querySet = movimiento.objects.filter(cliente=id)
	lista = []

	for s in querySet:
		try:
			i = instrumento.objects.get(pk=s.bindex)
			flag = False
			for x in lista:
				if x[0] == i.branding.nombre:
					if s.tipoMovimiento_id==3:
						x[1] -= s.monto
					else:
						x[1] += s.monto
					flag = True
			if flag == False:
				lista.append([i.branding.nombre, s.monto])

		except instrumento.DoesNotExist:
			pass

	aux = 0
	for l in lista:
		aux += l[1]
	for l in lista:
		l[1] = l[1]*100/aux

	return lista

def patrimonioConsolidado(request, id, fecha=None):
	if fecha is None:
		fecha=datetime.today().strftime("%d-%m-%Y")

	ls = fecha.split('-')
	fecha = ls[2]+'-' +ls[1]+'-'+ls[0]
	donBoolean = id.isdigit()
	query = saldoActualizado.objects.filter(cliente=id, fecha=fecha ).values('cliente__nombre', 'monto', 'tipoInversion__nombre').order_by('tipoInversion')
	return list(query)

def resumenCuentas(request, id):
	formato1 = "%m-%Y"
	hoy = datetime.today()
	hoy = hoy.strftime(formato1)
	ls = str(hoy)
	hoy = hoy.split('-')
	ls = ls.split('-')
	mes = int(ls[0])-1
	anio = int(ls[1])

	if mes==0 :
		mes = 12
		anio = anio-1

	qPresente = saldoMensual.objects.filter(cliente=id, anio=ls[1], mes=ls[0])#.values('cliente__nombre', 'saldoCierre','mes' , 'tipoInversion__nombre').order_by('tipoInversion')
	tot = []

	for p in list(qPresente):
		tot.append(p.tipoInversion.nombre+'  '+str(p.variacion())+' '+str( p.porcentaje_variacion()))

	return list(tot)

def graficos(request,id):#en este metodo llamamos a todos los metodos con sus respectivos graficos
	a=cartolasConsolidadas(request, id)
	b=totalesConsolidados(request, id,fecha=None)
	c=evolucionPatrimonio(request,id,fecha=None)
	d=resumenFondo(request, id)
	e=resumenMoneda(request, id)
	f=resumenBranding(request, id)
	resumen=[d,e,f]
	g=patrimonioConsolidado(request, id, fecha=None)
	h=resumenCuentas(request, id)
	x=[a,b,c,resumen,g,h]


	return HttpResponse(json.dumps(x,indent=4),content_type="application/json")
