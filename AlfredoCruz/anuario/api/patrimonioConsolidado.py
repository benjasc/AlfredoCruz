from anuario.models import cliente, movimiento
from rest_framework import serializers
from django.db.models import Sum, Q,Count
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import HttpResponse
import json

@api_view(['GET'])

def grafico1(request,id):


    grafico2  = movimiento.objects.filter(cliente=2)
    for s in grafico2:
        print()
    #grafico = list(movimiento.objects.filter(cliente=id)
        #      .filter(Q(tipoMovimiento=1)|Q(tipoMovimiento=2))
        #      .order_by('tipoInversion')
        #      .annotate(Sum('monto'))
        #      .values('tipoMovimiento__nombre','tipoInversion__nombre','cliente__nombre','monto'))

    return HttpResponse(json.dumps(grafico,indent=4),content_type="application/json")
    

# def getFondo(request):
#     proveedor_id = request.GET['id']
#     instrumentos = instrumento.objects.values('fondo').filter(proveedor__id=proveedor_id).order_by('fondo__nombre').distinct()
#     fondos = fondo.objects.filter(pk__in=instrumentos)
#     data = serializers.serialize('json',fondos, fields=("id","nombre","tipoInstrumento"))
#     return HttpResponse(data, content_type="application/json")
#
# def getTipoInstrumento(request):
#     fondo_id = request.GET['id']
#     tipoInst = fondo.objects.select_related('tipoInstrumento').filter(id=fondo_id)
#     list = []
#     for row in tipoInst:
#         list.append({
#         'tipoInstrumento__id':row.tipoInstrumento.id,
#         'tipoInstrumento__estructura_legal':row.tipoInstrumento.estructura_legal,
#         'tipoInstrumento__estado_distribucion':row.tipoInstrumento.estado_distribucion,
#         })
#     data=json.dumps(list)
#     return HttpResponse(data, 'application/javascript')
#
# def getIdBindex(request):
#     id_proveedor = request.GET['id_proveedor']
#     id_fondo = request.GET['id_fondo']
#     id_tipoInstrumento = request.GET['id_tipoInstrumento']
#     idbindex = instrumento.objects.values('bindex').filter(proveedor__id=id_proveedor)
