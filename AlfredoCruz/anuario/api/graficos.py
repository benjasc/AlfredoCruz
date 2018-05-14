from anuario.models import cliente, movimiento, saldoActualizado,saldoMensual
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
def evolucionPatrimonio(request,cliente_id):
    total = saldoMensual.objects.values('cliente__nombre','tipoInversion__nombre','anio','mes','saldoCierre').filter(cliente=cliente_id).filter(Q(tipoInversion=1)|Q(tipoInversion=2))
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
def resumenCuentas(request, cliente_id):
	fecha_actual = datetime.datetime.now()
	año_actual = fecha_actual.year
	mes_actual = fecha_actual.month
	año_anterior = fecha_actual.year-1
	mes_anterior = fecha_actual.month-1

	if condition:
		


	#query1 = saldoMensual.objects.filter(cliente=cliente_id, anio=ls[1],mes=[0]).values('saldoCierre','tipoInversion__nombre').order_by('tipoInversion')
	#query2 = saldoMensual.objects.filter(cliente=cliente_id, anio=ls[1],mes=[0]).values('saldoCierre','tipoInversion__nombre').order_by('tipoInversion')


	return HttpResponse(json.dumps(list(query1),indent=4), content_type= "application/json")
