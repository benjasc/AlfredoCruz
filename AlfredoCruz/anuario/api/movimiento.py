import json
from django.conf.urls import url, include
from anuario.models import movimiento, cliente, tipoMovimiento, tipoInstrumento, tipoInversion, bindex, instrumento, proveedor, fondo
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http import HttpResponse

@api_view(['GET','POST'])
def apiMovimiento(request,id=None):
    if request.method == 'GET':
        lista=[]
        if id is not None:
            query = movimiento.objects.filter(pk=id).values('id','monto','numero_cuotas','fecha','bindex_id','cliente__nombre','tipoInversion__nombre','tipoMovimiento__nombre')
            for x in query:
                fecha = str(x['fecha'])
                lista.append({
                    'id':x['id'],
                    'monto':x['monto'],
                    'numeroCuotas':x['numero_cuotas'],
                    'bindex_id':x['bindex_id'],
                    'fecha':fecha,
                    'cliente':x['cliente__nombre'],
                    'tipoInversion':x['tipoInversion__nombre'],
                    'tipoMovimiento':x['tipoMovimiento__nombre']

                })

        else:
            query = movimiento.objects.all().values('id','monto','numero_cuotas','fecha','bindex_id','cliente__nombre','tipoInversion__nombre','tipoMovimiento__nombre')
            for x in query:
                fecha = str(x['fecha'])
                lista.append({

                    'id':x['id'],
                    'monto':x['monto'],
                    'numeroCuotas':x['numero_cuotas'],
                    'bindex_id':x['bindex_id'],
                    'fecha':fecha,
                    'cliente':x['cliente__nombre'],
                    'tipoInversion':x['tipoInversion__nombre'],
                    'tipoMovimiento':x['tipoMovimiento__nombre']
                })

        return Response(json.dumps(lista,indent=4))

    elif request.method == 'POST':

        monto=request.data['monto']

        numero_cuotas=request.data['cuotas']
        fecha=request.data['fecha']

        #bindex
        proveedor2=request.data['proveedor']
        tipoinstrumento=request.data['tipoInstrumento']


        cli=request.data['cliente']
        tipoinversion=request.data['tipoInversion']
        tipomovimiento=request.data['tipoMovimiento']


        nombre_fondo=request.data['fondo']
        clase_proveedor=request.data['clase_proveedor']


        try:
            c = cliente.objects.get(nombre=cli)
        except cliente.DoesNotExist:
            c = None

        try:
            ti = tipoInversion.objects.get(nombre=tipoinversion)
        except tipoInversion.DoesNotExist:
            ti = None

        try:
            tm = tipoMovimiento.objects.get(nombre__iexact=tipomovimiento)
        except tipoMovimiento.DoesNotExist:
            tm = None


        try:
            tinstr = tipoInstrumento.objects.get(nombre=tipoinstrumento)
        except tipoInstrumento.DoesNotExist:
            tinstr = None
        try:
            prov = proveedor.objects.get(nombre=proveedor2)
        except proveedor.DoesNotExist:
            prov = None


        try:
            f = fondo.objects.get(nombre=nombre_fondo)

        except fondo.DoesNotExist:
            f = None



        try:
            i = instrumento.objects.values('bindex').filter(proveedor=prov, tipoInstrumento=tinstr, fondo=f, clase_proveedor=clase_proveedor)
            bindex_id = bindex.objects.get(pk=i[0]['bindex'])
        except instrumento.DoesNotExist:
            i = None
            bindex_id = None

        mov = movimiento(monto=monto,fecha=fecha,numero_cuotas=numero_cuotas,bindex=bindex_id,cliente=c,tipoMovimiento=tm,tipoInversion=ti)
        mov.save()
        return Response({'mensaje':'Datos guardados con exito'})
