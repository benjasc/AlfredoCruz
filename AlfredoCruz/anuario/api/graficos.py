from anuario.models import cliente, movimiento, saldoActualizado
from rest_framework import serializers
from django.db.models import Sum, Q,Count
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import HttpResponse
import json
import datetime


@api_view(['GET'])

def evolucionPatrimonio(request,cliente_id):
    query = list(saldoActualizado.objects.values('cliente').filter(cliente=cliente_id))
    return HttpResponse(json.dumps(x,indent=4),content_type="application/json")
