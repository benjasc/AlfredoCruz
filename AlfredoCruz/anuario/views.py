from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext
from AlfredoCruz.forms import LoginForm, ModalForm
from django.contrib.auth import authenticate, login
from django.core import serializers
from .models import fondo, instrumento, tipoInstrumento, proveedor,bindex,tipoInversion,cliente,movimiento,tipoMovimiento
import json
from django.http import JsonResponse
# Create your views here.

def login(request):

    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username,password=password)
            if user is not None:
                if user.is_active:
                    return HttpResponseRedirect( "perfil/")
                elif user.is_superuser:
                    return HttpResponseRedirect("index/")
                elif user.is_staff:
                    return HttpResponseRedirect("su/")
            else:
                return render(request,"login.html")
        else:
            return render(request,"login.html")
    else:
        return render(request,"login.html")
def perfil(request):
    return render(request,"index_user.html")

def index(request):
    form = ModalForm()
    contexto = {'form':form}
    return render(request,'index.html',contexto)

def SaldoInicial(request):
    return render(request,"SaldoInicial.html")

def tipoMovimiento(request):
    return render(request,"tipoMovimiento.html")

#def tipoInversion(request):
#    return render(request,"tipoInversion.html")

def Instrumento(request):
    return render(request,"Instrumento.html")

def getProveedor(request):
    id_tipoInstrumento = request.GET['id']
    instrumentos = instrumento.objects.values('proveedor').filter(tipoInstrumento__id = id_tipoInstrumento)
    proveedores = proveedor.objects.filter(pk__in=instrumentos)
    data = serializers.serialize('json',proveedores, fields=("id","datos"))
    return HttpResponse(data, content_type="application/json")

def getFondos(request):
    id_proveedor = request.GET['id']
    id_tipoInstrumento = request.GET['id_tipoInstrumento']
    instrumentos = instrumento.objects.values('fondo').filter(proveedor__id = id_proveedor).filter(tipoInstrumento__id = id_tipoInstrumento)
    fondos = fondo.objects.filter(pk__in=instrumentos)
    data = serializers.serialize('json',fondos, fields=("id","nombre"))
    return HttpResponse(data, content_type="application/json")

def guardarSaldo(request):
    id_tipoInstrumento = request.GET['id_tipoInstrumento']
    id_proveedor = request.GET['id_proveedor']
    id_fondo = request.GET['id_fondo']
    instrumentos = instrumento.objects.values('bindex').filter(proveedor__id = id_proveedor).filter(tipoInstrumento__id = id_tipoInstrumento).filter(fondo__id = id_fondo)
    bindex_id = bindex.objects.get(pk=instrumentos[0]['bindex'])
    cliente_id = cliente.objects.get(pk=request.GET['id_cliente'])
    tipoInversion_id = tipoInversion.objects.get(pk=request.GET['id_tipoInversion'])
    tipoMovimiento_id = tipoInversion.objects.get(pk=request.GET['id_tipoInversion'])
    monto = request.GET['monto']
    movimientoInicial = movimiento(bindex=bindex_id, cliente=cliente_id, tipoInversion=tipoInversion_id,saldo=monto)
    movimientoInicial.save()
    return HttpResponse("ok")
