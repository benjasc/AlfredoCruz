from anuario.models import cliente, movimiento, saldoActualizado,saldoMensual, instrumento
from rest_framework import serializers
from django.db.models import Sum, Q,Count,Case, CharField, Value, When, F, IntegerField
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import HttpResponse
import json
import datetime
import time
import calendar

@api_view(['GET'])
def patrimonioConsolidado(request, id, date):
	ls = date.split('-')
	date = ls[2]+'-' +ls[1]+'-'+ls[0]

	donBoolean = id.isdigit()

	if donBoolean == True:
		query = saldoActualizado.objects.filter(cliente=id, fecha=date ).values('cliente__nombre', 'monto', 'tipoInversion__nombre').order_by('tipoInversion')
		return HttpResponse(json.dumps(list(query),indent=4),content_type="application/json")
	else:
		return HttpResponse(json.dumps("El Cliente id " +id+ " ingresado no tiene movimientos registrados o no existe"), content_type= "application/json")


@api_view(['GET'])
def evolucionPatrimonio(request,cliente_id,fecha=None):
    if fecha == None:
        fecha = datetime.datetime.now()
    else:
        fecha= datetime.datetime.strptime(fecha,'%d-%m-%Y')

    anio_actual = fecha.year
    mes_actual = fecha.month
    anio_anterior = fecha.year-1

    total = saldoMensual.objects.values('cliente__nombre','tipoInversion__nombre','anio','mes','saldoCierre').filter(cliente=cliente_id).filter(Q(tipoInversion=1)|Q(tipoInversion=2))
    total = total.filter(Q(anio=anio_actual,mes__lte=mes_actual) | (Q(anio=anio_anterior,mes__gte=mes_actual)) )#cota inferior
    list = []
    for x in total:
        list.append({
        'Cliente':x['cliente__nombre'],
        'Tipo_inversion':x['tipoInversion__nombre'],
        'Anio':x['anio'],
        'Mes':x['mes'],
        'Saldo_cierre':x['saldoCierre'],
        })

    return HttpResponse(json.dumps(list,indent=4),content_type="application/json")



@api_view(['GET'])
def totalesConsolidados(request,cliente_id,fecha=None):

    if fecha == None:
        fecha = datetime.datetime.now()
    else:
        fecha= datetime.datetime.strptime(fecha,'%d-%m-%Y')

    print(fecha)
    anio_actual = fecha.year
    mes_actual = fecha.month

    query = saldoMensual.objects.values('saldoCierre','cliente__nombre','tipoInversion__nombre','anio','mes')
    query =	query.filter(cliente=cliente_id)
    query = query.filter(anio=anio_actual,mes=mes_actual)

    list=[]
    montoTotal=0
    for x in query:
	    montoTotal += x['saldoCierre']

    for y in query:
	    list.append({
        'Cliente':y['cliente__nombre'],
        'Tipo_inversion':y['tipoInversion__nombre'],
        'Anio':y['anio'],
        'Mes':y['mes'],
	    'Monto':y['saldoCierre'],
        'Porcentaje':round(((y['saldoCierre']*100)/montoTotal), 2),
        })

    return HttpResponse(json.dumps(list,indent=4),content_type="application/json")


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
	#return HttpResponse(json.dumps(list(query),indent=4),content_type="application/json")

def cartolasConsolidadas(request, id):
	fecha_actual = datetime.date.today()
	#obtener fondos, tipoInversion y agrupados por branding
	querySet = movimiento.objects.filter(cliente=id
								).filter(fecha__year=fecha_actual.year,fecha__month=fecha_actual.month
								).values('monto','bindex','tipoInversion__nombre','tipoMovimiento','fecha')
	lista = []

	for s in querySet:
		#print(s)
		try:
			totalAporte=0
			totalRetiro=0
			if s['tipoMovimiento']==3:
				totalRetiro = s['monto']
			else:
				totalAporte = s['monto']
			i = instrumento.objects.get(pk=s['bindex'])
			flag = False
			for x in lista:
				if x['Administradora'] == i.branding.nombre and x['Tipo_inversion'] == s['tipoInversion__nombre']:
					x['Saldo_actual'] += s['monto']
					flag = True

			if flag == False:
				#[i.branding.nombre,s['monto'], s['tipoInversion__nombre'],i.fondo.nombre_legal,totalAporte,totalRetiro]
				lista.append({
				'Administradora' : i.branding.nombre,
				'Saldo_actual'   : s['monto'],
				'Tipo_inversion': s['tipoInversion__nombre'],
				'Fondo'	 		 : i.fondo.nombre_legal,
				'Total_aporte'	 : totalAporte,
				'Total_retiro'	 : totalRetiro,
				})

		except instrumento.DoesNotExist:
			pass

	lista.sort(key=lambda l:l['Administradora'])

	aux =lista[0]['Administradora']
	suma = 0
	for l in range(len(lista)):
		print(lista[l]['Administradora'])
		if(lista[l]['Administradora'] == aux):
			suma += lista[l]['Saldo_actual']
		else:
			aux= lista[l]['Administradora']
			#lista.append([ str(lista[l-1]['Administradora']) + " - TOTAL", suma, ''])
			lista.append({
			'Administradora' : lista[l-1]['Administradora'],
			'Total'   : suma,
			})
			suma = 0
			suma += lista[l]['Saldo_actual']

	lista.sort(key=lambda l:l['Administradora'])

	return HttpResponse(json.dumps(lista, indent=4), content_type= "application/json")
