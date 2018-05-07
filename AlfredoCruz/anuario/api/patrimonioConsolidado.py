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
    #return Response(json.dumps(grafico))
