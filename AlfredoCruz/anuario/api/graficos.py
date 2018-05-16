from anuario.models import cliente, movimiento, saldoActualizado,saldoMensual, instrumento
from rest_framework import serializers
from django.db.models import Sum, Q,Count
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


def cartolasConsolidadas(request, cliente_id):
	query = movimiento.objects.filter(cliente=cliente_id).values('tipoInversion__nombre', 'bindex').order_by('tipoInversion').annotate(wea=Sum('monto'))

	lista = list()
	for q in query:
		try:
			i = instrumento.objects.get(pk=q['bindex'])
			lista.append([i.tipoInstrumento.nombre, i.branding.nombre, q['wea'],q['tipoInversion__nombre']])
		except instrumento.DoesNotExist:
			pass

	return HttpResponse(json.dumps(list(lista),indent=4),content_type="application/json")
