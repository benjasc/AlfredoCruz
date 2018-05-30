import json
from django.conf.urls import url, include
from anuario.models import pais
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def apiPaises(request, id=None):
    if request.method=='GET':
        if id is not None:
            query = list(pais.objects.filter(pk=id).values('id','nombre','nombre_ing'))
        else:
            query = list(pais.objects.all().values('id','nombre','nombre_ing'))
        return Response({"paises":json.dumps(query,indent=4)})
