from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from AlfredoCruz.forms import LoginForm, ModalForm, ModalForm2, formCliente, formPais, formDomicilio, formTipoInstrumento, formFrecuenciaDistribucion, formTipoInversion, formTipoMovimiento, formBindex, formAsignacionActivo
from django.contrib.auth import authenticate, login
from django.core import serializers
from .models import fondo, instrumento, tipoInstrumento, proveedor,bindex,tipoInversion,cliente,movimiento,tipoMovimiento, branding, broadCategory, pais, domicilio, moneda, frecuenciaDistribucion, rendimiento, asignacionActivo, carteraCliente, categoria, reporte_anual_cuota, sector, saldoMensual, saldoActualizado

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
    form2 = ModalForm2()
    contexto = {'form':form,'form2':form2}
    return render(request,'index.html',contexto)

def SaldoInicial(request):
    return render(request,"SaldoInicial.html")

#def tipoMovimiento(request):
    #return render(request,"tipoMovimiento.html")

#def tipoInversion(request):
#    return render(request,"tipoInversion.html")

def Instrumento(request):
    return render(request,"Instrumento.html")
#----------------SaldoInicial
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
    tipoMovimiento_id = tipoMovimiento.objects.get(pk=request.GET['id_tipoMovimiento'])
    monto = request.GET['monto']
    fecha = request.GET['fecha']
    movimientoInicial = movimiento(bindex=bindex_id,numero_cuotas=0,tipoMovimiento=tipoMovimiento_id, cliente=cliente_id, tipoInversion=tipoInversion_id,monto=monto,fecha=fecha)
    movimientoInicial.save()
    return HttpResponse("ok")
#----------------FinSaldoInicial


#----------------losCrud
def getCliente(request):
    cli = cliente.objects.all()
    url = ''
    filter_Nom = request.GET.get('filter_Nom')
    filter_Apa = request.GET.get('filter_Apa')
    filter_Ama = request.GET.get('filter_Ama')
    resp = request.GET.get('resp')
    page = request.GET.get('page')

    if filter_Nom != None and filter_Nom != '' and filter_Nom != 'None':
            cli = cli.filter(nombre__icontains=filter_Nom)
            url += 'filter_Nom=' + filter_Nom + '&'
    if filter_Apa != None and filter_Apa != '' and filter_Apa != 'None':
            cli = cli.filter(Apaterno__icontains=filter_Apa)
            url += 'filter_Apa=' + filter_Apa + '&'
    if filter_Ama != None and filter_Ama != '' and filter_Ama != 'None':
            cli = cli.filter(Amaterno__icontains=filter_Ama)
            url += 'filter_Ama=' + filter_Ama + '&'

    if page is None:
       page = 1

    count = cli.count()
    paginator = Paginator(cli, 15)
    cli = cli[(15 * (int(page) - 1)): 15 * (int(page) - 1) + 15]

    try:
        lista=paginator.page(page)
    except PageNotAnInteger:
        lista=paginator.page(1)
    except EmptyPage:
        lista=paginator.page(paginator.num_pages)

    filtros = {'page': page, 'filter_Nom': filter_Nom, 'filter_Apa':filter_Apa, 'filter_Ama': filter_Ama, 'resp' : resp}
    context = {"cliente": cli, 'url': url, 'lista': lista}
    merged_dict = dict(list(filtros.items()) + list(context.items()))
    return render(request, "cliente/lista.html", merged_dict)

def editarCliente(request, id=None):
    if request.method == 'GET':
        if id != None:
            cli = cliente.objects.get(pk=id)
            form = formCliente(initial ={ 'nombre' : cli.nombre, 'apellido_paterno' : cli.Apaterno, 'apellido_materno': cli.Amaterno})

        else:
            form = formCliente()

        persona = {'form': form}
        return render(request, "cliente/editar.html", persona)

    if request.method == 'POST':
        if id!= None:
            try:
                cli = cliente.objects.get(pk=id)

                nombre = request.POST['nombre']
                apat = request.POST['apellido_paterno']
                amat = request.POST['apellido_materno']

                cli.nombre = nombre
                cli.Apaterno = apat
                cli.Amaterno = amat
                cli.save()
                return HttpResponseRedirect("/cliente/?resp=1")




            except cliente.DoesNotExist:
                pass
                return HttpResponseRedirect("/cliente/?resp=2")
        else:
            nombre = request.POST['nombre']
            apat = request.POST['apellido_paterno']
            amat = request.POST['apellido_materno']

            cli = cliente(nombre=nombre, Apaterno=apat, Amaterno=amat).save()
            return HttpResponseRedirect("/cliente")

def getBindex(request):
    dato = bindex.objects.all()
    url = ''
    filter_Nom = request.GET.get('filter_Nom')
    page = request.GET.get('page')

    if filter_Nom != None and filter_Nom != '' and filter_Nom != 'None':
            dato = dato.filter(morningstar_id__icontains=filter_Nom)
            url += 'filter_Nom=' + filter_Nom + '&'

    if page is None:
       page = 1

    count = dato.count()
    paginator = Paginator(dato, 15)
    dato = dato[(15 * (int(page) - 1)): 15 * (int(page) - 1) + 15]

    try:
        lista=paginator.page(page)
    except PageNotAnInteger:
        lista=paginator.page(1)
    except EmptyPage:
        lista=paginator.page(paginator.num_pages)

    filtros = {'page': page, 'filter_Nom': filter_Nom}
    context = {"bindex": dato, 'url': url, 'lista': lista}
    merged_dict = dict(list(filtros.items()) + list(context.items()))
    return render(request, "bindex/lista.html", merged_dict)

def editarBindex(request, id=None):
    if request.method == 'GET':
        if id != None:
            dato = bindex.objects.get(pk=id)
            form = formBindex(initial ={ 'nombre' : dato.morningstar_id})

        else:
            form = formBindex()

        formulario = {'form': form}
        return render(request, "bindex/editar.html", formulario)

    if request.method == 'POST':
        if id!=None:
            try:
                #query set
                dato = bindex.objects.get(pk=id)

                #datos entrantes
                nombre = request.POST['nombre']

                #salvar datos
                dato.morningstar_id = nombre
                dato.save()

                return HttpResponseRedirect("/bindex/?resp=1")

            except dato.DoesNotExist:
                pass
                return HttpResponseRedirect("/bindex/?resp=2")
        else:
            nombre = request.POST['nombre']

            dato = bindex(morningstar_id=nombre).save()
            return HttpResponseRedirect("/bindex")

def getBranding(request):
    dato = branding.objects.all()
    print(dato)
    url = ''
    filter_id = request.GET.get('filter_id')
    filter_Nom = request.GET.get('filter_Nom')
    page = request.GET.get('page')

    if filter_id != None and filter_id != '' and filter_id != 'None':
            dato = dato.filter(pk__icontains=filter_id)
            url += 'filter_id=' + filter_id + '&'

    if filter_Nom != None and filter_Nom != '' and filter_Nom != 'None':
            dato = dato.filter(nombre__icontains=filter_Nom)
            url += 'filter_Nom=' + filter_Nom + '&'

    if page is None:
       page = 1

    count = dato.count()
    paginator = Paginator(dato, 15)
    dato = dato[(15 * (int(page) - 1)): 15 * (int(page) - 1) + 15]

    try:
        lista=paginator.page(page)
    except PageNotAnInteger:
        lista=paginator.page(1)
    except EmptyPage:
        lista=paginator.page(paginator.num_pages)

    filtros = {'page': page, 'filter_Nom': filter_Nom, 'filter_id': filter_id}
    context = {"branding": dato, 'url': url, 'lista': lista}
    merged_dict = dict(list(filtros.items()) + list(context.items()))
    return render(request, "branding/lista.html", merged_dict)

def getBroadcategory(request):
    dato = broadCategory.objects.all()
    url = ''
    filter_id = request.GET.get('filter_id')
    filter_Nom = request.GET.get('filter_Nom')
    page = request.GET.get('page')

    if filter_id != None and filter_id != '' and filter_id != 'None':
            dato = dato.filter(pk__icontains=filter_id)
            url += 'filter_id=' + filter_id + '&'

    if filter_Nom != None and filter_Nom != '' and filter_Nom != 'None':
            dato = dato.filter(nombre__icontains=filter_Nom)
            url += 'filter_Nom=' + filter_Nom + '&'

    if page is None:
       page = 1

    count = dato.count()
    paginator = Paginator(dato, 15)
    dato = dato[(15 * (int(page) - 1)): 15 * (int(page) - 1) + 15]

    try:
        lista=paginator.page(page)
    except PageNotAnInteger:
        lista=paginator.page(1)
    except EmptyPage:
        lista=paginator.page(paginator.num_pages)

    filtros = {'page': page, 'filter_Nom': filter_Nom, 'filter_id': filter_id}
    context = {"broadcategory": dato, 'url': url, 'lista': lista}
    merged_dict = dict(list(filtros.items()) + list(context.items()))
    return render(request, "broadcategory/lista.html", merged_dict)

def getPais(request):
    dato = pais.objects.all()
    url = ''
    filter_id = request.GET.get('filter_id')
    filter_Nom = request.GET.get('filter_Nom')
    filter_Nom_ingles = request.GET.get('filter_Nom_ingles')

    page = request.GET.get('page')

    if filter_id != None and filter_id != '' and filter_id != 'None':
            dato = dato.filter(pk__icontains=filter_id)
            url += 'filter_id=' + filter_id + '&'

    if filter_Nom != None and filter_Nom != '' and filter_Nom != 'None':
            dato = dato.filter(nombre__icontains=filter_Nom)
            url += 'filter_Nom=' + filter_Nom + '&'

    if filter_Nom_ingles != None and filter_Nom_ingles != '' and filter_Nom_ingles != 'None':
            dato = dato.filter(nombre_ing__icontains=filter_Nom_ingles)
            url += 'filter_Nom_ingles=' + filter_Nom_ingles + '&'



    if page is None:
       page = 1

    count = dato.count()
    paginator = Paginator(dato, 15)
    dato = dato[(15 * (int(page) - 1)): 15 * (int(page) - 1) + 15]

    try:
        lista=paginator.page(page)
    except PageNotAnInteger:
        lista=paginator.page(1)
    except EmptyPage:
        lista=paginator.page(paginator.num_pages)

    filtros = {'page': page,'filter_id': filter_id, 'filter_Nom': filter_Nom, 'filter_Nom_ingles': filter_Nom_ingles}
    context = {"pais": dato, 'url': url, 'lista': lista}
    merged_dict = dict(list(filtros.items()) + list(context.items()))
    return render(request, "pais/lista.html", merged_dict)

def editarPais(request, id=None):
    if request.method=='GET':
        if id != None:
            dato = pais.objects.get(pk=id)
            form = formPais(initial ={ 'nombre' : dato.nombre, 'nombre_ingles': dato.nombre_ing})

        else:
            form = formPais()

        formulario = {'form': form}
        return render(request, "pais/editar.html", formulario)
    if request.method=='POST':
        try:
            #query set
            dato = pais.objects.get(pk=id)

            #datos entrantes
            nombre = request.POST['nombre']
            nombreIng = request.POST['nombre_ingles']

            #salvar datos
            dato.nombre = nombre
            dato.nombre_ing = nombreIng
            dato.save()

            return HttpResponseRedirect("/pais/?resp=1")

        except dato.DoesNotExist:
            pass
            return HttpResponseRedirect("/pais/?resp=2")

def getProveedor(request):
    dato = proveedor.objects.all()

    url = ''
    filter_id = request.GET.get('filter_id')
    filter_Nom = request.GET.get('filter_Nom')

    page = request.GET.get('page')

    if filter_id != None and filter_id != '' and filter_id != 'None':
            dato = dato.filter(pk__icontains=filter_id)
            url += 'filter_id=' + filter_id + '&'

    if filter_Nom != None and filter_Nom != '' and filter_Nom != 'None':
            dato = dato.filter(nombre__icontains=filter_Nom)
            url += 'filter_Nom=' + filter_Nom + '&'



    if page is None:
       page = 1

    count = dato.count()
    paginator = Paginator(dato, 15)
    dato = dato[(15 * (int(page) - 1)): 15 * (int(page) - 1) + 15]

    try:
        lista=paginator.page(page)
    except PageNotAnInteger:
        lista=paginator.page(1)
    except EmptyPage:
        lista=paginator.page(paginator.num_pages)

    filtros = {'page': page, 'filter_id': filter_id, 'filter_Nom': filter_Nom}
    context = {"proveedor": dato, 'url': url, 'lista': lista}
    merged_dict = dict(list(filtros.items()) + list(context.items()))
    return render(request, "proveedor/lista.html", merged_dict)




def getDomicilio(request):
    dato = domicilio.objects.all()
    url = ''
    filter_id = request.GET.get('filter_id')
    filter_Nom = request.GET.get('filter_Nom')

    page = request.GET.get('page')

    if filter_id != None and filter_id != '' and filter_id != 'None':
            dato = dato.filter(pk__icontains=filter_id)
            url += 'filter_id=' + filter_id + '&'

    if filter_Nom != None and filter_Nom != '' and filter_Nom != 'None':
            dato = dato.filter(nombre__icontains=filter_Nom)
            url += 'filter_Nom=' + filter_Nom + '&'

    if page is None:
       page = 1

    count = dato.count()
    paginator = Paginator(dato, 15)
    dato = dato[(15 * (int(page) - 1)): 15 * (int(page) - 1) + 15]

    try:
        lista=paginator.page(page)
    except PageNotAnInteger:
        lista=paginator.page(1)
    except EmptyPage:
        lista=paginator.page(paginator.num_pages)

    filtros = {'page': page, 'filter_Nom': filter_Nom, 'filter_id': filter_id}
    context = {"domicilio": dato, 'url': url, 'lista': lista}
    merged_dict = dict(list(filtros.items()) + list(context.items()))
    return render(request, "domicilio/lista.html", merged_dict)


def editarDomicilio(request, id=None):
    if request.method == 'GET':
        if id != None:
            dato = domicilio.objects.get(pk=id)
            form = formDomicilio(initial ={ 'nombre' : dato.nombre})

        else:
            form = formDomicilio()

        formulario = {'form': form}
        return render(request, "domicilio/editar.html", formulario)
    if request.method == 'POST':
        try:
            #query set
            dato = domicilio.objects.get(pk=id)

            #datos entrantes
            nombre = request.POST['nombre']

            #salvar datos
            dato.nombre = nombre
            dato.save()

            return HttpResponseRedirect("/domicilio/?resp=1")

        except dato.DoesNotExist:
            pass
            return HttpResponseRedirect("/domicilio/?resp=2")


def getMoneda(request):
    dato = moneda.objects.all()
    url = ''
    filter_Nom = request.GET.get('filter_Nom')
    filter_id = request.GET.get('filter_id')

    page = request.GET.get('page')

    if filter_Nom != None and filter_Nom != '' and filter_Nom != 'None':
            dato = dato.filter(nombre__icontains=filter_Nom)
            url += 'filter_Nom=' + filter_Nom + '&'

    if filter_id != None and filter_id != '' and filter_id != 'None':
            dato = dato.filter(pk__icontains=filter_id)
            url += 'filter_id=' + filter_id + '&'

    if page is None:
       page = 1

    count = dato.count()
    paginator = Paginator(dato, 15)
    dato = dato[(15 * (int(page) - 1)): 15 * (int(page) - 1) + 15]

    try:
        lista=paginator.page(page)
    except PageNotAnInteger:
        lista=paginator.page(1)
    except EmptyPage:
        lista=paginator.page(paginator.num_pages)

    filtros = {'page': page, 'filter_Nom': filter_Nom, 'filter_id': filter_id}
    context = {"moneda": dato, 'url': url, 'lista': lista}
    merged_dict = dict(list(filtros.items()) + list(context.items()))
    return render(request, "moneda/lista.html", merged_dict)

def getTipoInstrumento(request):
    dato = tipoInstrumento.objects.all()
    url = ''
    filter_Nom = request.GET.get('filter_Nom')

    page = request.GET.get('page')

    if filter_Nom != None and filter_Nom != '' and filter_Nom != 'None':
            dato = dato.filter(nombre__icontains=filter_Nom)
            url += 'filter_Nom=' + filter_Nom + '&'

    if page is None:
       page = 1

    count = dato.count()
    paginator = Paginator(dato, 15)
    dato = dato[(15 * (int(page) - 1)): 15 * (int(page) - 1) + 15]

    try:
        lista=paginator.page(page)
    except PageNotAnInteger:
        lista=paginator.page(1)
    except EmptyPage:
        lista=paginator.page(paginator.num_pages)

    filtros = {'page': page, 'filter_Nom': filter_Nom}
    context = {"tipoInstrumento": dato, 'url': url, 'lista': lista}
    merged_dict = dict(list(filtros.items()) + list(context.items()))
    return render(request, "tipoInstrumento/lista.html", merged_dict)

def editarTipoInstrumento(request, id=None):
    if request.method== 'GET':
        if id != None:
            dato = tipoInstrumento.objects.get(pk=id)
            form = formTipoInstrumento(initial ={ 'nombre' : dato.nombre})

        else:
            form = formTipoInstrumento()

        formulario = {'form': form}
        return render(request, "tipoInstrumento/editar.html", formulario)
    if request.method=='POST':
        if id != None:
            try:
                #query set
                dato = tipoInstrumento.objects.get(pk=id)

                #datos entrantes
                nombre = request.POST['nombre']

                #salvar datos
                dato.nombre = nombre
                dato.save()

                return HttpResponseRedirect("/tipoInstrumento/?resp=1")

            except dato.DoesNotExist:
                pass
                return HttpResponseRedirect("/tipoInstrumento/?resp=2")
        else:
            nombre = request.POST['nombre']

            dato = tipoInstrumento(nombre=nombre).save()
            return HttpResponseRedirect("/tipoInstrumento")
def getFrecuencia(request):
    dato = frecuenciaDistribucion.objects.all()
    print(dato)
    url = ''
    filter_Nom = request.GET.get('filter_Nom')

    page = request.GET.get('page')

    if filter_Nom != None and filter_Nom != '' and filter_Nom != 'None':
            dato = dato.filter(frecuencia__icontains=filter_Nom)
            url += 'filter_Nom=' + filter_Nom + '&'

    if page is None:
       page = 1

    count = dato.count()
    paginator = Paginator(dato, 15)
    dato = dato[(15 * (int(page) - 1)): 15 * (int(page) - 1) + 15]

    try:
        lista=paginator.page(page)
    except PageNotAnInteger:
        lista=paginator.page(1)
    except EmptyPage:
        lista=paginator.page(paginator.num_pages)

    filtros = {'page': page, 'filter_Nom': filter_Nom}
    context = {"frecuenciaDistribucion": dato, 'url': url, 'lista': lista}
    merged_dict = dict(list(filtros.items()) + list(context.items()))
    return render(request, "frecuenciaDistribucion/lista.html", merged_dict)



def editarFrecuencia(request, id=None):
    if request.method == 'GET':
        if id != None:
            dato = frecuenciaDistribucion.objects.get(pk=id)
            form = formFrecuenciaDistribucion(initial ={ 'nombre' : dato.frecuencia})

        else:
            form = formFrecuenciaDistribucion()

        formulario = {'form': form}
        return render(request, "frecuenciaDistribucion/editar.html", formulario)
    if request.method == 'POST':
        if id!=None:
            try:
                #query set
                dato = frecuenciaDistribucion.objects.get(pk=id)

                #datos entrantes
                nombre = request.POST['nombre']

                #salvar datos
                dato.frecuencia = nombre
                dato.save()

                return HttpResponseRedirect("/frecuencia/?resp=1")

            except dato.DoesNotExist:
                pass
                return HttpResponseRedirect("/frecuencia/?resp=2")
        else:
            nombre = request.POST['nombre']

            dato = frecuenciaDistribucion(frecuencia=nombre).save()
            return HttpResponseRedirect("/frecuencia")

def getRendimiento(request):
    dato = rendimiento.objects.all()
    url = ''
    filter_pk = request.GET.get('filter_pk')
    filter_estado = request.GET.get('filter_estado')
    print(filter_estado)

    page = request.GET.get('page')

    if filter_pk != None and filter_pk != '' and filter_pk != 'None':
            dato = dato.filter(pk__icontains=filter_pk)
            url += 'filter_pk=' + filter_pk + '&'

    if filter_estado != None and filter_estado != '' and filter_estado != 'None':
            dato = dato.filter(estado__icontains=filter_estado)
            url += 'filter_estado=' + filter_estado + '&'

    if page is None:
       page = 1

    count = dato.count()
    paginator = Paginator(dato, 15)
    dato = dato[(15 * (int(page) - 1)): 15 * (int(page) - 1) + 15]

    try:
        lista=paginator.page(page)
    except PageNotAnInteger:
        lista=paginator.page(1)
    except EmptyPage:
        lista=paginator.page(paginator.num_pages)

    filtros = {'page': page, 'filter_pk': filter_pk, 'filter_estado': filter_estado}
    context = {"rendimiento": dato, 'url': url, 'lista': lista}
    merged_dict = dict(list(filtros.items()) + list(context.items()))
    return render(request, "rendimiento/lista.html", merged_dict)


def getTipoInversion(request):
    dato = tipoInversion.objects.all()
    url = ''
    filter_Nom = request.GET.get('filter_Nom')

    page = request.GET.get('page')

    if filter_Nom != None and filter_Nom != '' and filter_Nom != 'None':
            dato = dato.filter(nombre__icontains=filter_Nom)
            url += 'filter_Nom=' + filter_Nom + '&'

    if page is None:
       page = 1

    count = dato.count()
    paginator = Paginator(dato, 15)
    dato = dato[(15 * (int(page) - 1)): 15 * (int(page) - 1) + 15]

    try:
        lista=paginator.page(page)
    except PageNotAnInteger:
        lista=paginator.page(1)
    except EmptyPage:
        lista=paginator.page(paginator.num_pages)

    filtros = {'page': page, 'filter_Nom': filter_Nom}
    context = {"tipoInversion": dato, 'url': url, 'lista': lista}
    merged_dict = dict(list(filtros.items()) + list(context.items()))
    return render(request, "tipoInversion/lista.html", merged_dict)

def editarTipoInversion(request, id=None):
    if request.method=='GET':
        if id != None:
            dato = tipoInversion.objects.get(pk=id)
            form = formTipoInversion(initial ={ 'id' : dato.id, 'nombre': dato.nombre})

        else:
            form = formTipoInversion()

        formulario = {'form': form}
        return render(request, "tipoInversion/editar.html", formulario)

    if request.method=='POST':
        if id != None:
            try:
                #query set
                dato = tipoInversion.objects.get(pk=id)

                #datos entrantes
                nombre = request.POST['nombre']

                #salvar datos
                dato.nombre = nombre
                dato.save()

                return HttpResponseRedirect("/tipoInversion/?resp=1")

            except dato.DoesNotExist:
                pass
                return HttpResponseRedirect("/tipoInversion/?resp=2")
        else:
            nombre = request.POST['nombre']

            dato = tipoInversion(nombre=nombre).save()
            return HttpResponseRedirect("/tipoInversion")

def getTipoMovimiento(request):
    dato = tipoMovimiento.objects.all()
    url = ''
    filter_Nom = request.GET.get('filter_Nom')

    page = request.GET.get('page')

    if filter_Nom != None and filter_Nom != '' and filter_Nom != 'None':
            dato = dato.filter(nombre__icontains=filter_Nom)
            url += 'filter_Nom=' + filter_Nom + '&'

    if page is None:
       page = 1

    count = dato.count()
    paginator = Paginator(dato, 15)
    dato = dato[(15 * (int(page) - 1)): 15 * (int(page) - 1) + 15]

    try:
        lista=paginator.page(page)
    except PageNotAnInteger:
        lista=paginator.page(1)
    except EmptyPage:
        lista=paginator.page(paginator.num_pages)

    filtros = {'page': page, 'filter_Nom': filter_Nom}
    context = {"tipoMovimiento": dato, 'url': url, 'lista': lista}
    merged_dict = dict(list(filtros.items()) + list(context.items()))
    return render(request, "tipoMovimiento/lista.html", merged_dict)



def editarTipoMovimiento(request, id=None):
    if request.method=='GET':
        if id != None:
            dato = tipoMovimiento.objects.get(pk=id)
            form = formTipoMovimiento(initial ={'nombre': dato.nombre})

        else:
            form = formTipoMovimiento()

        formulario = {'form': form}
        return render(request, "tipoMovimiento/editar.html", formulario)

    if request.method=='POST':
        if id != None :
            try:
                #query set
                dato = tipoMovimiento.objects.get(pk=id)

                #datos entrantes
                nombre = request.POST['nombre']

                #salvar datos
                dato.nombre = nombre
                dato.save()

                return HttpResponseRedirect("/tipoMovimiento/?resp=1")

            except dato.DoesNotExist:
                pass
                return HttpResponseRedirect("/tipoMovimiento/?resp=2")
        else:
            nombre = request.POST['nombre']

            dato = tipoMovimiento(nombre=nombre).save()
            return HttpResponseRedirect("/tipoMovimiento")

def getAsignacionActivo(request):
    dato = asignacionActivo.objects.all()
    url = ''
    #FILTROS GET**
    #filter_Nom = request.GET.get('filter_Nom')
    filter_bono = request.GET.get('filter_bono')
    filter_efectivo = request.GET.get('filter_efectivo')
    filter_convertible = request.GET.get('filter_convertible')
    filter_preferida = request.GET.get('filter_preferida')
    filter_acciones = request.GET.get('filter_acciones')
    filter_otra = request.GET.get('filter_otra')
    filter_fecha = request.GET.get('filter_fecha')

    page = request.GET.get('page')

    #el filtrado
    if filter_bono != None and filter_bono != '' and filter_bono != 'None':
            dato = dato.filter(red_bono__icontains=filter_bono)
            url += 'filter_bono=' + filter_bono + '&'

    if filter_efectivo != None and filter_efectivo != '' and filter_efectivo != 'None':
            dato = dato.filter(red_efectivo__icontains=filter_efectivo)
            url += 'filter_efectivo=' + filter_efectivo + '&'

    if filter_convertible != None and filter_convertible != '' and filter_convertible != 'None':
            dato = dato.filter(red_convertible__icontains=filter_convertible)
            url += 'filter_convertible=' + filter_convertible + '&'

    if filter_preferida != None and filter_preferida != '' and filter_preferida != 'None':
            dato = dato.filter(red_preferida__icontains=filter_preferida)
            url += 'filter_preferida=' + filter_preferida + '&'

    if filter_acciones != None and filter_acciones != '' and filter_acciones != 'None':
            dato = dato.filter(red_acciones__icontains=filter_acciones)
            url += 'filter_acciones=' + filter_acciones + '&'

    if filter_otra != None and filter_otra != '' and filter_otra != 'None':
            dato = dato.filter(red_otra__icontains=filter_otra)
            url += 'filter_otra=' + filter_otra + '&'

    if filter_fecha != None and filter_fecha != '' and filter_fecha != 'None':
            dato = dato.filter(portafolio_fecha__icontains=filter_fecha)
            url += 'filter_fecha=' + filter_fecha + '&'



    if page is None:
       page = 1

    count = dato.count()
    paginator = Paginator(dato, 15)
    dato = dato[(15 * (int(page) - 1)): 15 * (int(page) - 1) + 15]

    try:
        lista=paginator.page(page)
    except PageNotAnInteger:
        lista=paginator.page(1)
    except EmptyPage:
        lista=paginator.page(paginator.num_pages)

    filtros = {'page': page,'filter_bono': filter_bono, 'filter_efectivo': filter_efectivo, 'filter_convertible': filter_convertible, 'filter_preferida': filter_preferida, 'filter_acciones': filter_acciones, 'filter_otra': filter_otra, 'filter_fecha': filter_fecha}
    context = {"datos": dato, 'url': url, 'lista': lista}
    merged_dict = dict(list(filtros.items()) + list(context.items()))
    return render(request, "asignacionActivo/lista.html", merged_dict)



def editarAsignacionActivo(request, id=None):
    if request.method=='GET':
        if id != None:
            dato = asignacionActivo.objects.get(pk=id)
            print(dato)
            form = formAsignacionActivo(initial ={'bono': dato.red_bono, 'efectivo': dato.red_efectivo, 'convertible': dato.red_convertible, 'preferida': dato.red_preferida, 'accciones': dato.red_acciones, 'otra': dato.red_otra, 'fecha': dato.portafolio_fecha})

        else:
            form = formAsignacionActivo()

        formulario = {'form': form}
        return render(request, "asignacionActivo/editar.html", formulario)

    if request.method=='POST':
        if id != None :
            try:
                #query set
                dato = asignacionActivo.objects.get(pk=id)

                #datos entrantes
                #nombre = request.POST['nombre']
                bono = request.POST['filter_bono']
                efectivo = request.POST['filter_efectivo']
                convertible = request.POST['filter_convertible']
                preferida = request.POST['filter_preferida']
                acciones = request.POST['filter_acciones']
                otra = request.POST['filter_otra']
                fecha = request.POST['filter_fecha']


                #salvar datos
                dato.red_bono = bono
                dato.red_efectivo = efectivo
                dato.red_convertible = convertible
                dato.red_preferida = preferida
                dato.red_acciones = acciones
                dato.red_otra = otra
                dato.portafolio_fecha = portafolio_fecha


                #dato.nombre = nombre
                dato.save()

                return HttpResponseRedirect("/asignacionActivo/?resp=1")

            except dato.DoesNotExist:
                pass
                return HttpResponseRedirect("/asignacionActivo/?resp=2")
        else:
            nombre = request.POST['nombre']

            dato = asignacionActivo(nombre=nombre).save()
            return HttpResponseRedirect("/asignacionActivo")

def getCarteraCliente(request):
    dato = carteraCliente.objects.all()
    url = ''
    #FILTROS GET**
    #filter_Nom = request.GET.get('filter_Nom')

    filter_fecha = request.GET.get('filter_fecha')
    filter_monto = request.GET.get('filter_monto')
    filter_bindex = request.GET.get('filter_bindex')
    filter_cliente = request.GET.get('filter_cliente')
    filter_tipoInversion = request.GET.get('filter_tipoInversion')


    page = request.GET.get('page')

    #el filtrado
    if filter_fecha != None and filter_fecha != '' and filter_fecha != 'None':
            dato = dato.filter(fecha__icontains=filter_fecha)
            url += 'filter_fecha=' + filter_fecha + '&'

    if filter_monto != None and filter_monto != '' and filter_monto != 'None':
            dato = dato.filter(monto__icontains=filter_monto)
            url += 'filter_monto=' + filter_monto + '&'

    if filter_bindex != None and filter_bindex != '' and filter_bindex != 'None':
            dato = dato.filter(bindex__morningstar_id__icontains=filter_bindex)
            print(dato)
            url += 'filter_bindex=' + filter_bindex + '&'

    if filter_cliente != None and filter_cliente != '' and filter_cliente != 'None':
            dato = dato.filter(cliente__id__icontains=filter_cliente)
            url += 'filter_cliente=' + filter_cliente + '&'

    if filter_tipoInversion != None and filter_tipoInversion != '' and filter_tipoInversion != 'None':
            dato = dato.filter(tipoInversion__nombre__icontains=filter_tipoInversion)
            url += 'filter_tipoInversion=' + filter_tipoInversion + '&'



    if page is None:
       page = 1

    count = dato.count()
    paginator = Paginator(dato, 15)
    dato = dato[(15 * (int(page) - 1)): 15 * (int(page) - 1) + 15]

    try:
        lista=paginator.page(page)
    except PageNotAnInteger:
        lista=paginator.page(1)
    except EmptyPage:
        lista=paginator.page(paginator.num_pages)

    filtros = {'page': page, 'filter_fecha': filter_fecha, 'filter_monto': filter_monto, 'filter_bindex': filter_bindex, 'filter_cliente': filter_cliente, 'filter_tipoInversion': filter_tipoInversion}
    context = {"datos": dato, 'url': url, 'lista': lista}
    merged_dict = dict(list(filtros.items()) + list(context.items()))
    return render(request, "carteraCliente/lista.html", merged_dict)





def editarCarteraCliente(request, id = None):
    return HttpResponse("ok")


def getCategoria(request):
    dato = categoria.objects.all()
    url = ''
    #FILTROS GET**
    #filter_Nom = request.GET.get('filter_Nom')

    filter_id = request.GET.get('filter_id')
    filter_nombre = request.GET.get('filter_nombre')
    filter_broadCategory = request.GET.get('filter_broadCategory')
    filter_moneda = request.GET.get('filter_moneda')


    page = request.GET.get('page')

    #el filtrado
    if filter_id != None and filter_id != '' and filter_id != 'None':
            dato = dato.filter(pk__icontains=filter_id)
            url += 'filter_id=' + filter_id + '&'

    if filter_nombre != None and filter_nombre != '' and filter_nombre != 'None':
            dato = dato.filter(nombre__icontains=filter_nombre)
            url += 'filter_nombre=' + filter_nombre + '&'

    if filter_broadCategory != None and filter_broadCategory != '' and filter_broadCategory != 'None':
            dato = dato.filter(broadCategory__nombre__icontains=filter_broadCategory)
            print(dato)
            url += 'filter_broadCategory=' + filter_broadCategory + '&'

    if filter_moneda != None and filter_moneda != '' and filter_moneda != 'None':
            dato = dato.filter(moneda__nombre__icontains=filter_moneda)
            url += 'filter_moneda=' + filter_moneda + '&'



    if page is None:
       page = 1

    count = dato.count()
    paginator = Paginator(dato, 15)
    dato = dato[(15 * (int(page) - 1)): 15 * (int(page) - 1) + 15]

    try:
        lista=paginator.page(page)
    except PageNotAnInteger:
        lista=paginator.page(1)
    except EmptyPage:
        lista=paginator.page(paginator.num_pages)

    filtros = {'page': page, 'filter_id': filter_id, 'filter_nombre': filter_nombre, 'filter_broadCategory': filter_broadCategory, 'filter_moneda': filter_moneda}
    context = {"datos": dato, 'url': url, 'lista': lista}
    merged_dict = dict(list(filtros.items()) + list(context.items()))
    return render(request, "categoria/lista.html", merged_dict)



def editarCategoria(request, id=None):
    return HttpResponse("ok")

def getFondo(request):
    dato = fondo.objects.all()
    url = ''
    #FILTROS GET**
    #filter_Nom = request.GET.get('filter_Nom')

    filter_id = request.GET.get('filter_id')
    filter_nombre = request.GET.get('filter_nombre')
    filter_nombreLegal = request.GET.get('filter_nombreLegal')
    filter_fecha_inicio = request.GET.get('filter_fecha_inicio')
    filter_domicilio = request.GET.get('filter_domicilio')
    filter_categoria = request.GET.get('filter_categoria')
    filter_moneda = request.GET.get('filter_moneda')


    page = request.GET.get('page')

    #el filtrado
    if filter_id != None and filter_id != '' and filter_id != 'None':
            dato = dato.filter(pk__icontains=filter_id)
            url += 'filter_id=' + filter_id + '&'

    if filter_nombre != None and filter_nombre != '' and filter_nombre != 'None':
            dato = dato.filter(nombre__icontains=filter_nombre)
            url += 'filter_nombre=' + filter_nombre + '&'

    if filter_nombreLegal != None and filter_nombreLegal != '' and filter_nombreLegal != 'None':
            dato = dato.filter(nombre_legal__icontains=filter_nombreLegal)
            url += 'filter_nombreLegal=' + filter_nombreLegal + '&'


    if filter_fecha_inicio != None and filter_fecha_inicio != '' and filter_fecha_inicio != 'None':
            dato = dato.filter(fecha_inicio__icontains=filter_fecha_inicio)
            url += 'filter_fecha_inicio=' + filter_fecha_inicio + '&'

    if filter_domicilio != None and filter_domicilio != '' and filter_domicilio != 'None':
            dato = dato.filter(domicilio__nombre__icontains=filter_domicilio)
            url += 'filter_domicilio=' + filter_domicilio + '&'

    if filter_categoria != None and filter_categoria != '' and filter_categoria != 'None':
            dato = dato.filter(categoria__nombre__icontains=filter_categoria)
            url += 'filter_categoria=' + filter_categoria + '&'

    if filter_moneda != None and filter_moneda != '' and filter_moneda != 'None':
            dato = dato.filter(moneda__nombre__icontains=filter_moneda)
            url += 'filter_moneda=' + filter_moneda + '&'


    if page is None:
       page = 1

    count = dato.count()
    paginator = Paginator(dato, 15)
    dato = dato[(15 * (int(page) - 1)): 15 * (int(page) - 1) + 15]

    try:
        lista=paginator.page(page)
    except PageNotAnInteger:
        lista=paginator.page(1)
    except EmptyPage:
        lista=paginator.page(paginator.num_pages)

    filtros = {'page': page, 'filter_id': filter_id, 'filter_nombre': filter_nombre, 'filter_nombreLegal': filter_nombreLegal, 'filter_fecha_inicio': filter_fecha_inicio,'filter_domicilio': filter_domicilio,'filter_categoria': filter_categoria,'filter_moneda': filter_moneda}
    context = {"datos": dato, 'url': url, 'lista': lista}
    merged_dict = dict(list(filtros.items()) + list(context.items()))
    return render(request, "fondo/lista.html", merged_dict)



def editarFondo(request, id=None):
    return HttpResponse("ok")

def getInstrumento(request):
    dato = instrumento.objects.all()
    url = ''
    #FILTROS GET**
    #filter_Nom = request.GET.get('filter_Nom')

    filter_run = request.GET.get('filter_run')
    filter_clase = request.GET.get('filter_clase')
    filter_opera = request.GET.get('filter_opera')
    filter_branding = request.GET.get('filter_branding')
    filter_fondo = request.GET.get('filter_fondo')
    filter_frecencia = request.GET.get('filter_frecencia')
    filter_proveedor = request.GET.get('filter_proveedor')
    filter_rendimiento = request.GET.get('filter_rendimiento')
    filter_tipoInstrumento = request.GET.get('filter_tipoInstrumento')
    filter_nombre = request.GET.get('filter_nombre')


    page = request.GET.get('page')

    #el filtrado
    if filter_run != None and filter_run != '' and filter_run != 'None':
            dato = dato.filter(run_svs__icontains=filter_run)
            url += 'filter_run=' + filter_run + '&'

    if filter_clase != None and filter_clase != '' and filter_clase != 'None':
            dato = dato.filter(clase_proveedor__icontains=filter_clase)
            url += 'filter_clase=' + filter_clase + '&'

    if filter_opera != None and filter_opera != '' and filter_opera != 'None':
            dato = dato.filter(operation_ready__icontains=filter_opera)
            print(dato)
            url += 'filter_opera=' + filter_opera + '&'

    if filter_branding != None and filter_branding != '' and filter_branding != 'None':
            dato = dato.filter(branding__nombre__icontains=filter_branding)
            url += 'filter_branding=' + filter_branding + '&'

    if filter_fondo != None and filter_fondo != '' and filter_fondo != 'None':
            dato = dato.filter(fondo__nombre__icontains=filter_fondo)
            url += 'filter_fondo=' + filter_fondo + '&'

    if filter_frecencia != None and filter_frecencia != '' and filter_frecencia != 'None':
            dato = dato.filter(frecuenciaDistribucion__frecuencia__icontains=filter_frecencia)
            url += 'filter_frecencia=' + filter_frecencia + '&'

    if filter_proveedor != None and filter_proveedor != '' and filter_proveedor != 'None':
            dato = dato.filter(proveedor__nombre__icontains=filter_proveedor)
            url += 'filter_proveedor=' + filter_proveedor + '&'

    if filter_rendimiento != None and filter_rendimiento != '' and filter_rendimiento != 'None':
            dato = dato.filter(rendimiento__id__icontains=filter_rendimiento)
            url += 'filter_rendimiento=' + filter_rendimiento + '&'

    if filter_tipoInstrumento != None and filter_tipoInstrumento != '' and filter_tipoInstrumento != 'None':
            dato = dato.filter(tipoInstrumento__nombre__icontains=filter_tipoInstrumento)
            url += 'filter_tipoInstrumento=' + filter_tipoInstrumento + '&'

    if filter_nombre != None and filter_nombre != '' and filter_nombre != 'None':
            dato = dato.filter(nombre__icontains=filter_nombre)
            url += 'filter_nombre=' + filter_nombre + '&'

    if page is None:
       page = 1

    count = dato.count()
    paginator = Paginator(dato, 15)
    dato = dato[(15 * (int(page) - 1)): 15 * (int(page) - 1) + 15]

    try:
        lista=paginator.page(page)
    except PageNotAnInteger:
        lista=paginator.page(1)
    except EmptyPage:
        lista=paginator.page(paginator.num_pages)

    filtros = {'page': page, 'filter_run': filter_run,
                             'filter_clase': filter_clase,
                             'filter_opera': filter_opera,
                             'filter_branding': filter_branding,
                             'filter_fondo': filter_fondo,
                             'filter_frecencia': filter_frecencia,
                             'filter_proveedor': filter_proveedor,
                             'filter_rendimiento': filter_rendimiento,
                             'filter_tipoInstrumento': filter_tipoInstrumento,
                             'filter_nombre': filter_nombre,
                             }
    context = {"datos": dato, 'url': url, 'lista': lista}
    merged_dict = dict(list(filtros.items()) + list(context.items()))
    return render(request, "instrumento/lista.html", merged_dict)



def editarInstrumento(request, id=None):
    return HttpResponse("ok")


def getMovimiento(request):
    dato = movimiento.objects.all()
    url = ''
    #FILTROS GET**
    #filter_Nom = request.GET.get('filter_Nom')

    filter_monto = request.GET.get('filter_monto')
    filter_fecha = request.GET.get('filter_fecha')
    filter_cuota = request.GET.get('filter_cuota')
    filter_cliente = request.GET.get('filter_cliente')
    filter_tipoInversion = request.GET.get('filter_tipoInversion')
    filter_tipoMovimiento = request.GET.get('filter_tipoMovimiento')
    filter_bindex = request.GET.get('filter_bindex')

    page = request.GET.get('page')

    #el filtrado
    if filter_monto != None and filter_monto != '' and filter_monto != 'None':
            dato = dato.filter(monto__icontains=filter_monto)
            url += 'filter_monto=' + filter_monto + '&'

    if filter_fecha != None and filter_fecha != '' and filter_fecha != 'None':
            dato = dato.filter(fecha__icontains=filter_fecha)
            url += 'filter_fecha=' + filter_fecha + '&'

    if filter_cuota != None and filter_cuota != '' and filter_cuota != 'None':
            dato = dato.filter(numero_cuotas__icontains=filter_cuota)
            print(dato)
            url += 'filter_cuota=' + filter_cuota + '&'

    if filter_cliente != None and filter_cliente != '' and filter_cliente != 'None':
            dato = dato.filter(cliente__id__icontains=filter_cliente)
            url += 'filter_cliente=' + filter_cliente + '&'

    if filter_tipoInversion != None and filter_tipoInversion != '' and filter_tipoInversion != 'None':
            dato = dato.filter(tipoInversion__nombre__icontains=filter_tipoInversion)
            url += 'filter_tipoInversion=' + filter_tipoInversion + '&'

    if filter_tipoMovimiento != None and filter_tipoMovimiento != '' and filter_tipoMovimiento != 'None':
            dato = dato.filter(tipoMovimiento__nombre__icontains=filter_tipoMovimiento)
            url += 'filter_tipoMovimiento=' + filter_tipoMovimiento + '&'

    if filter_bindex != None and filter_bindex != '' and filter_bindex != 'None':
            dato = dato.filter(bindex__morningstar_id__icontains=filter_bindex)
            url += 'filter_bindex=' + filter_bindex + '&'


    if page is None:
       page = 1

    count = dato.count()
    paginator = Paginator(dato, 15)
    dato = dato[(15 * (int(page) - 1)): 15 * (int(page) - 1) + 15]

    try:
        lista=paginator.page(page)
    except PageNotAnInteger:
        lista=paginator.page(1)
    except EmptyPage:
        lista=paginator.page(paginator.num_pages)

    filtros = {'page': page, 'filter_monto': filter_monto,
                             'filter_fecha': filter_fecha,
                             'filter_cuota': filter_cuota,
                             'filter_cliente': filter_cliente,
                             'filter_tipoInversion': filter_tipoInversion,
                             'filter_tipoMovimiento': filter_tipoMovimiento,
                             'filter_bindex': filter_bindex}


    context = {"datos": dato, 'url': url, 'lista': lista}
    merged_dict = dict(list(filtros.items()) + list(context.items()))
    return render(request, "movimiento/lista.html", merged_dict)




def editarMovimiento(request, id=None):
    return HttpResponse("ok")

def getReporteAnualCouta(request):
    dato = reporte_anual_cuota.objects.all()
    url = ''
    #FILTROS GET**
    #filter_Nom = request.GET.get('filter_Nom')

    AnnualReportDate = request.GET.get('AnnualReportDate')
    NetExpenseRatio = request.GET.get('NetExpenseRatio')
    AnnualReportPerformanceFee = request.GET.get('AnnualReportPerformanceFee')
    InterimNetExpenseRatioDate = request.GET.get('InterimNetExpenseRatioDate')
    InterimNetExpenseRatio = request.GET.get('InterimNetExpenseRatio')


    page = request.GET.get('page')

    #el filtrado
    if AnnualReportDate != None and AnnualReportDate != '' and AnnualReportDate != 'None':
            dato = dato.filter(AnnualReportDate__icontains=AnnualReportDate)
            url += 'AnnualReportDate=' + AnnualReportDate + '&'

    if NetExpenseRatio != None and NetExpenseRatio != '' and NetExpenseRatio != 'None':
            dato = dato.filter(NetExpenseRatio__icontains=NetExpenseRatio)
            url += 'NetExpenseRatio=' + NetExpenseRatio + '&'

    if AnnualReportPerformanceFee != None and AnnualReportPerformanceFee != '' and AnnualReportPerformanceFee != 'None':
            dato = dato.filter(AnnualReportPerformanceFee__icontains=AnnualReportPerformanceFee)
            print(dato)
            url += 'AnnualReportPerformanceFee=' + AnnualReportPerformanceFee + '&'

    if InterimNetExpenseRatioDate != None and InterimNetExpenseRatioDate != '' and InterimNetExpenseRatioDate != 'None':
            dato = dato.filter(InterimNetExpenseRatioDate__icontains=InterimNetExpenseRatioDate)
            url += 'InterimNetExpenseRatioDate=' + InterimNetExpenseRatioDate + '&'

    if InterimNetExpenseRatio != None and InterimNetExpenseRatio != '' and InterimNetExpenseRatio != 'None':
            dato = dato.filter(InterimNetExpenseRatio__icontains=InterimNetExpenseRatio)
            url += 'InterimNetExpenseRatio=' + InterimNetExpenseRatio + '&'



    if page is None:
       page = 1

    count = dato.count()
    paginator = Paginator(dato, 15)
    dato = dato[(15 * (int(page) - 1)): 15 * (int(page) - 1) + 15]

    try:
        lista=paginator.page(page)
    except PageNotAnInteger:
        lista=paginator.page(1)
    except EmptyPage:
        lista=paginator.page(paginator.num_pages)

    filtros = {'page': page, 'AnnualReportDate': AnnualReportDate,
                             'NetExpenseRatio': NetExpenseRatio,
                             'AnnualReportPerformanceFee': AnnualReportPerformanceFee,
                             'InterimNetExpenseRatioDate': InterimNetExpenseRatioDate,
                             'InterimNetExpenseRatio': InterimNetExpenseRatio}


    context = {"datos": dato, 'url': url, 'lista': lista}
    merged_dict = dict(list(filtros.items()) + list(context.items()))
    return render(request, "reporteAnualCouta/lista.html", merged_dict)




def editarReporteAnualCouta(request, id=None):
    return HttpResponse("ok")

def getSector(request):
    dato = sector.objects.all()
    url = ''
    #FILTROS GET**
    #filter_Nom = request.GET.get('filter_Nom')

    materiales_basicos = request.GET.get('materiales_basicos')
    servicio_comunicacion = request.GET.get('servicio_comunicacion')
    ciclico_consumidor = request.GET.get('ciclico_consumidor')
    defensa_consumidor = request.GET.get('defensa_consumidor')
    energia = request.GET.get('energia')
    servicios_financieros = request.GET.get('servicios_financieros')
    cuidado_salud = request.GET.get('cuidado_salud')
    acciones_industriales = request.GET.get('acciones_industriales')
    bienes_raices = request.GET.get('bienes_raices')
    tecnologia = request.GET.get('tecnologia')
    utilidades = request.GET.get('utilidades')
    portafolio_fecha = request.GET.get('portafolio_fecha')


    page = request.GET.get('page')
    servicio_comunicacion
    #el filtrado
    if materiales_basicos != None and materiales_basicos != '' and materiales_basicos != 'None':
            dato = dato.filter(materiales_basicos__icontains=materiales_basicos)
            url += 'materiales_basicos=' + materiales_basicos + '&'

    if servicio_comunicacion != None and servicio_comunicacion != '' and servicio_comunicacion != 'None':
            dato = dato.filter(servicio_comunicacion__icontains=servicio_comunicacion)
            url += 'servicio_comunicacion=' + servicio_comunicacion + '&'

    if ciclico_consumidor != None and ciclico_consumidor != '' and ciclico_consumidor != 'None':
            dato = dato.filter(ciclico_consumidor__icontains=ciclico_consumidor)
            print(dato)
            url += 'ciclico_consumidor=' + ciclico_consumidor + '&'

    if defensa_consumidor != None and defensa_consumidor != '' and defensa_consumidor != 'None':
            dato = dato.filter(defensa_consumidor__icontains=defensa_consumidor)
            url += 'defensa_consumidor=' + defensa_consumidor + '&'

    if energia != None and energia != '' and energia != 'None':
            dato = dato.filter(energia__icontains=energia)
            url += 'energia=' + energia + '&'

    if servicios_financieros != None and servicios_financieros != '' and servicios_financieros != 'None':
            dato = dato.filter(servicios_financieros__icontains=energia)
            url += 'servicios_financieros=' + servicios_financieros + '&'

    if cuidado_salud != None and cuidado_salud != '' and cuidado_salud != 'None':
            dato = dato.filter(cuidado_salud__icontains=energia)
            url += 'cuidado_salud=' + cuidado_salud + '&'


    if acciones_industriales != None and acciones_industriales != '' and acciones_industriales != 'None':
            dato = dato.filter(acciones_industriales__icontains=energia)
            url += 'acciones_industriales=' + acciones_industriales + '&'

    if bienes_raices != None and bienes_raices != '' and bienes_raices != 'None':
            dato = dato.filter(bienes_raices__icontains=energia)
            url += 'bienes_raices=' + bienes_raices + '&'

    if tecnologia != None and tecnologia != '' and tecnologia != 'None':
            dato = dato.filter(tecnologia__icontains=energia)
            url += 'tecnologia=' + tecnologia + '&'

    if utilidades != None and utilidades != '' and utilidades != 'None':
            dato = dato.filter(utilidades__icontains=energia)
            url += 'utilidades=' + utilidades + '&'

    if portafolio_fecha != None and portafolio_fecha != '' and portafolio_fecha != 'None':
            dato = dato.filter(portafolio_fecha__icontains=energia)
            url += 'portafolio_fecha=' + portafolio_fecha + '&'


    if page is None:
       page = 1

    count = dato.count()
    paginator = Paginator(dato, 15)
    dato = dato[(15 * (int(page) - 1)): 15 * (int(page) - 1) + 15]

    try:
        lista=paginator.page(page)
    except PageNotAnInteger:
        lista=paginator.page(1)
    except EmptyPage:
        lista=paginator.page(paginator.num_pages)



    filtros = {'page': page, 'materiales_basicos': materiales_basicos,
                             'servicio_comunicacion': servicio_comunicacion,
                             'ciclico_consumidor': ciclico_consumidor,
                             'defensa_consumidor': defensa_consumidor,
                             'energia': energia,
                             'servicios_financieros': servicios_financieros,
                             'cuidado_salud': cuidado_salud,
                             'acciones_industriales': acciones_industriales,
                             'bienes_raices': bienes_raices,
                             'tecnologia': tecnologia,
                             'utilidades': utilidades,
                             'portafolio_fecha': portafolio_fecha}


    context = {"datos": dato, 'url': url, 'lista': lista}
    merged_dict = dict(list(filtros.items()) + list(context.items()))
    return render(request, "sector/lista.html", merged_dict)




def editarSector(request, id=None):
    return HttpResponse("ok")

def getSaldoMensual(request):
    dato = saldoMensual.objects.all()
    url = ''
    #FILTROS GET**
    #filter_Nom = request.GET.get('filter_Nom')

    cliente = request.GET.get('cliente')
    tipoInversion = request.GET.get('tipoInversion')
    anio = request.GET.get('anio')
    mes = request.GET.get('mes')
    saldoCierre = request.GET.get('saldoCierre')


    page = request.GET.get('page')

    #el filtrado
    if cliente != None and cliente != '' and cliente != 'None':
            dato = dato.filter(cliente_id__icontains=cliente)
            url += 'cliente=' + cliente + '&'

    if tipoInversion != None and tipoInversion != '' and tipoInversion != 'None':
            dato = dato.filter(tipoInversion__nombre__icontains=tipoInversion)
            url += 'tipoInversion=' + tipoInversion + '&'

    if anio != None and anio != '' and anio != 'None':
            dato = dato.filter(anio__icontains=anio)
            print(dato)
            url += 'anio=' + anio + '&'

    if mes != None and mes != '' and mes != 'None':
            dato = dato.filter(mes__icontains=mes)
            url += 'mes=' + mes + '&'

    if saldoCierre != None and saldoCierre != '' and saldoCierre != 'None':
            dato = dato.filter(saldoCierre__icontains=saldoCierre)
            url += 'saldoCierre=' + saldoCierre + '&'


    if page is None:
       page = 1

    count = dato.count()
    paginator = Paginator(dato, 15)
    dato = dato[(15 * (int(page) - 1)): 15 * (int(page) - 1) + 15]

    try:
        lista=paginator.page(page)
    except PageNotAnInteger:
        lista=paginator.page(1)
    except EmptyPage:
        lista=paginator.page(paginator.num_pages)




    filtros = {'page': page, 'cliente': cliente,
                             'tipoInversion': tipoInversion,
                             'anio': anio,
                             'mes': mes,
                             'saldoCierre': saldoCierre}


    context = {"datos": dato, 'url': url, 'lista': lista}
    merged_dict = dict(list(filtros.items()) + list(context.items()))
    return render(request, "saldoMensual/lista.html", merged_dict)




def editarSaldoMensual(request, id=None):
    return HttpResponse("ok")


def getSaldoActualizado(request):
    dato = saldoActualizado.objects.all()
    url = ''
    #FILTROS GET**
    #filter_Nom = request.GET.get('filter_Nom')

    cliente = request.GET.get('cliente')
    tipoInversion = request.GET.get('tipoInversion')
    filter_bindex = request.GET.get('filter_bindex')
    monto = request.GET.get('monto')
    fecha = request.GET.get('fecha')


    page = request.GET.get('page')

    #el filtrado
    if cliente != None and cliente != '' and cliente != 'None':
            dato = dato.filter(cliente__id__icontains=cliente)
            url += 'cliente=' + cliente + '&'

    if tipoInversion != None and tipoInversion != '' and tipoInversion != 'None':
            dato = dato.filter(tipoInversion__nombre__icontains=tipoInversion)
            url += 'tipoInversion=' + tipoInversion + '&'

    if filter_bindex != None and filter_bindex != '' and filter_bindex != 'None':
            dato = dato.filter(bindex__morningstar_id__icontains=filter_bindex)
            url += 'filter_bindex=' + filter_bindex + '&'

    if monto != None and monto != '' and monto != 'None':
            dato = dato.filter(monto__icontains=monto)
            url += 'monto=' + monto + '&'

    if fecha != None and fecha != '' and fecha != 'None':
            dato = dato.filter(fecha__icontains=fecha)
            url += 'fecha=' + fecha + '&'


    if page is None:
       page = 1

    count = dato.count()
    paginator = Paginator(dato, 15)
    dato = dato[(15 * (int(page) - 1)): 15 * (int(page) - 1) + 15]

    try:
        lista=paginator.page(page)
    except PageNotAnInteger:
        lista=paginator.page(1)
    except EmptyPage:
        lista=paginator.page(paginator.num_pages)




    filtros = {'page': page, 'cliente': cliente,
                             'tipoInversion': tipoInversion,
                             'filter_bindex': filter_bindex,
                             'monto': monto,
                             'fecha': fecha}


    context = {"datos": dato, 'url': url, 'lista': lista}
    merged_dict = dict(list(filtros.items()) + list(context.items()))
    return render(request, "saldoActualizado/lista.html", merged_dict)




def editarSaldoActualizado(request, id=None):
    return HttpResponse("ok")
