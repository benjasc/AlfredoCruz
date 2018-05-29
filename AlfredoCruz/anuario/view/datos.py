from django.shortcuts import render
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.urls import reverse
from django.conf import settings
from django.contrib.auth.models import User
from django.utils.datastructures import MultiValueDictKeyError

from AlfredoCruz.forms import Formimportarlista
from anuario.models import bindex, branding, proveedor, domicilio, moneda, broadCategory, categoria, tipoInstrumento, rendimiento, fondo, instrumento, frecuenciaDistribucion, rentaFija, asignacionActivo, sector, countryExposure, pais

import json, pyexcel
def verificar(s):
    if s.strip() != '' and s != None:
        return True
    else:
        return False

def importar_datos(request):


    if request.method == "POST":
        form = Formimportarlista(request.POST, request.FILES)
        user = request.user
        respuesta = ''
        respuesta += '=============INICIO DATOS=============<br>'
        try:
            filename = request.FILES['archivo'].name
            extension = filename.split(".")[-1]

            content = request.FILES['archivo'].read()
            sheet = pyexcel.get_array(file_type=extension, file_content=content)

            i = len(sheet[0])
            th = sheet[0]
            del sheet[0]


            for fila in range(len(sheet)):
                for col in range(len(sheet[0])):
            #        if type(sheet[fila][col]) != types.UnicodeType:
                    sheet[fila][col] = str(sheet[fila][col])


            for s in sheet:
                if verificar(s[0]) == True: #morningstar

                    try:
                        b = bindex.objects.get(morningstar=str(s[0].strip()))
                    except bindex.DoesNotExist:
                        b = bindex(morningstar=str(s[0].strip()))
                        b.save()

                    if verificar(s[1]) == True and verificar(s[2]) == True:
                        try:
                            br = branding.objects.get(pk=s[1].strip())
                        except branding.DoesNotExist:
                            br = branding(id=s[1].strip(), nombre= s[2].strip())
                            br.save()

                    if verificar(s[3]) == True and verificar(s[4]) == True:
                        try:
                            p = proveedor.objects.get(pk=s[3].strip())
                        except proveedor.DoesNotExist:
                            p = proveedor(id=s[3].strip(), nombre= s[4].strip())
                            p.save()
                        data = []
                        if verificar(s[30]) == True:
                            data.append({'telefono': s[30].strip()})

                        if verificar(s[31]) == True:
                            data.append({'sitio_web': s[31].strip()})

                        p.datos = json.dumps(data)
                        p.save()



                    if verificar(s[11]) == True and verificar(s[12]) == True:
                        try:
                            d = domicilio.objects.get(pk=s[11].strip())
                        except domicilio.DoesNotExist:
                            d = domicilio(id=s[11].strip(), nombre= s[12].strip())
                            d.save()

                    if verificar(s[13]) == True and verificar(s[14]) == True:
                        try:
                            m = moneda.objects.get(pk=s[13].strip())
                        except moneda.DoesNotExist:
                            m = moneda(id=s[13].strip(), nombre= s[14].strip())
                            m.save()


                    if verificar(s[18]) == True and verificar(s[19]) == True:
                        try:
                            bc = broadCategory.objects.get(pk=s[19].strip())
                        except broadCategory.DoesNotExist:
                            bc = broadCategory(id=s[19].strip(), nombre= s[18].strip())
                            bc.save()


                    if verificar(s[16]) == True and verificar(s[17]) == True:
                        try:
                            c = categoria.objects.get(pk=s[16].strip(), broadCategory = bc, moneda= moneda.objects.get(pk=s[15].strip()))
                        except categoria.DoesNotExist:
                            c = categoria(id=s[16].strip(), nombre= s[17].strip(), broadCategory = bc, moneda=moneda.objects.get(pk=s[15].strip()))
                            c.save()


                    if verificar(s[21]) == True:
                        try:
                            fd = frecuenciaDistribucion.objects.get(frecuencia=s[21].strip())
                        except frecuenciaDistribucion.DoesNotExist:
                            try:
                                fd = frecuenciaDistribucion.objects.get(frecuencia=s[21].strip())
                            except frecuenciaDistribucion.DoesNotExist:
                                fd = None
                    else:
                        fd = None

                    if verificar(s[22]) == True and verificar(s[23]) == True:
                        try:
                            ti = tipoInstrumento.objects.get(estado_distribucion=s[22].strip(), estructura_legal=s[23].strip())
                        except tipoInstrumento.DoesNotExist:
                            ti = tipoInstrumento(estado_distribucion=s[22].strip(), estructura_legal=s[23].strip())
                            ti.save()



                    if verificar(s[27]) == True:
                        try:
                            r = rendimiento.objects.get(pk=s[27].strip())
                        except rendimiento.DoesNotExist:
                            if verificar(s[28]) == True:
                                r = rendimiento(pk=s[27].strip(), estado=s[28].strip())
                                r.save()
                            else:
                                r = None
                    else:
                        r = None



                    if verificar(s[7]) == True and verificar(s[8]) == True and  verificar(s[9]) == True:
                        try:
                            f = fondo.objects.get(pk=s[7].strip(), domicilio= d, categoria=c, moneda=m, tipoInstrumento = ti)
                        except fondo.DoesNotExist:
                            f = fondo(pk=s[7].strip(), nombre= s[8].strip(), nombre_legal=s[9].strip(), domicilio= d, categoria =c, moneda=m, tipoInstrumento=ti)
                        f.fecha_inicio = s[10].strip()
                        f.save()




                    try:
                        instr = instrumento.objects.get(bindex=b, fondo = f, proveedor = p, branding = br, rendimiento = r)
                    except instrumento.DoesNotExist:
                        instr = instrumento(bindex=b, fondo = f, proveedor = p, branding = br, rendimiento = r)
                        instr.save()


                    instr.frecuenciaDistribucion =fd
                    instr.save()

                    if verificar(s[5]) == True:
                        instr.run_svs = s[5]
                    if verificar(s[20]) == True:
                        instr.clase_proveedor = s[20]
                    if verificar(s[24]) == True:
                        instr.operation_ready = int(s[24])
                    instr.save()

                respuesta += 'Fila '+str(s[0])+' insertada<br>'
        except MultiValueDictKeyError:
            pass
                #response = 1
        respuesta += '=============FIN DATOS=============<br>'

        #fixedincome
        respuesta += '=============INICIO FIXED INCOME=============<br>'
        try:

            filename = request.FILES['fixedincome'].name
            extension = filename.split(".")[-1]

            content = request.FILES['fixedincome'].read()
            sheet = pyexcel.get_array(file_type=extension, file_content=content)

            i = len(sheet[0])
            th = sheet[0]
            del sheet[0]


            for fila in range(len(sheet)):
                for col in range(len(sheet[0])):
            #        if type(sheet[fila][col]) != types.UnicodeType:
                    sheet[fila][col] = str(sheet[fila][col])

            for s in sheet:
                if verificar(s[0]) == True: #morningstar

                    try:
                        b = bindex.objects.get(morningstar=str(s[0].strip()))
                    except bindex.DoesNotExist:
                        b = bindex(morningstar=str(s[0].strip()))
                        b.save()

                    try:
                        rent = rentaFija.objects.get(bindex=b)
                        respuesta += 'Fila '+str(s[0])+' ya existe<br>'

                    except rent.DoesNotExist:
                        rent = rentaFija.objects.get(bindex = b)
                        rent.save()
                        if verificar(s[1]) == True:
                            rent.bsed = s[1]
                        if verificar(s[3]) == True:
                            rent.bsem = s[3]
                        if verificar(s[5]) == True:
                            rent.bsmd = s[5]
                        if verificar(s[7]) == True:
                            rent.bsym = s[7]
                        if verificar(s[9]) == True:
                            rent.cred = s[9]
                        if verificar(s[11]) == True:
                            rent.crem = s[11]
                        if verificar(s[13]) == True:
                            rent.crmd = s[13]
                        if verificar(s[15]) == True:
                            rent.crym = s[15]
                        if verificar(s[17]) == True:
                            rent.portafolio_fecha = s[17]
                        rent.save()
                    respuesta += 'Fila '+str(s[0])+' insertada<br>'
        except MultiValueDictKeyError:
            pass
        respuesta += '=============FIN FIXED INCOME=============<br>'

        #ASSET ALLOCATION
        respuesta += '=============INICIO ASSET ALLOCATION=============<br>'
        try:
            filename = request.FILES['assetallocation'].name
            extension = filename.split(".")[-1]

            content = request.FILES['assetallocation'].read()
            sheet = pyexcel.get_array(file_type=extension, file_content=content)

            i = len(sheet[0])
            th = sheet[0]
            del sheet[0]


            for fila in range(len(sheet)):
                for col in range(len(sheet[0])):
            #        if type(sheet[fila][col]) != types.UnicodeType:
                    sheet[fila][col] = str(sheet[fila][col])

            for s in sheet:
                if verificar(s[0]) == True: #morningstar

                    try:
                        b = bindex.objects.get(morningstar=str(s[0].strip()))
                    except bindex.DoesNotExist:
                        b = bindex(morningstar=str(s[0].strip()))
                        b.save()

                    try:
                        aa = asignacionActivo.objects.get(bindex=b)
                        respuesta += 'Fila '+str(s[0])+' ya existe<br>'

                    except aa.DoesNotExist:
                        aa = asignacionActivo.objects.get(bindex = b)
                        aa.save()

                        if verificar(s[1]) == True:
                            aa.red_bono = s[1]
                        if verificar(s[2]) == True:
                            aa.red_efectivo = s[2]
                        if verificar(s[3]) == True:
                            aa.red_convertible = s[3]
                        if verificar(s[4]) == True:
                            aa.red_preferida = s[4]
                        if verificar(s[5]) == True:
                            aa.red_acciones = s[5]
                        if verificar(s[6]) == True:
                            aa.red_otra = s[6]
                        if verificar(s[7]) == True:
                            aa.portafolio_fecha = s[7]
                        aa.save()
                    respuesta += 'Fila '+str(s[0])+' insertada<br>'
        except MultiValueDictKeyError:
            pass
        respuesta += '=============FIN ASSET ALLOCATION=============<br>'

        #Sector Exposure
        respuesta += '=============INICIO SECTOR EXPOSURE=============<br>'
        try:
            filename = request.FILES['sectorexposure'].name
            extension = filename.split(".")[-1]

            content = request.FILES['sectorexposure'].read()
            sheet = pyexcel.get_array(file_type=extension, file_content=content)

            i = len(sheet[0])
            th = sheet[0]
            del sheet[0]


            for fila in range(len(sheet)):
                for col in range(len(sheet[0])):
            #        if type(sheet[fila][col]) != types.UnicodeType:
                    sheet[fila][col] = str(sheet[fila][col])

            for s in sheet:
                if verificar(s[0]) == True: #morningstar

                    try:
                        b = bindex.objects.get(morningstar=str(s[0].strip()))
                    except bindex.DoesNotExist:
                        b = bindex(morningstar=str(s[0].strip()))
                        b.save()

                    try:
                        se = sector.objects.get(bindex=b)
                        respuesta += 'Fila '+str(s[0])+' ya existe<br>'

                    except s.DoesNotExist:
                        se = sector.objects.get(bindex = b)
                        se.save()


                        if verificar(s[1]) == True:
                            se.materiales_basicos = s[1]
                        if verificar(s[2]) == True:
                            se.servicio_comunicacion = s[2]
                        if verificar(s[3]) == True:
                            se.ciclico_consumidor = s[3]
                        if verificar(s[4]) == True:
                            se.defensa_consumidor = s[4]
                        if verificar(s[5]) == True:
                            se.energia = s[5]
                        if verificar(s[6]) == True:
                            se.servicios_financieros = s[6]
                        if verificar(s[7]) == True:
                            se.cuidado_salud = s[7]

                        if verificar(s[8]) == True:
                            se.acciones_industriales = s[8]
                        if verificar(s[9]) == True:
                            se.portafolio_fecha = s[9]
                        if verificar(s[10]) == True:
                            se.bienes_raices = s[10]
                        if verificar(s[11]) == True:
                            se.tecnologia = s[11]
                        if verificar(s[12]) == True:
                            se.utilidades = s[12]
                        se.save()
                    respuesta += 'Fila '+str(s[0])+' insertada<br>'
        except MultiValueDictKeyError:
            pass
        respuesta += '=============FIN SECTOR EXPOSURE=============<br>'

        #COUNTRY EXPOSURE
        respuesta += '=============INICIO COUNTRY EXPOSURE=============<br>'
        try:
            filename = request.FILES['assetallocation'].name
            extension = filename.split(".")[-1]

            content = request.FILES['countryexposure'].read()
            sheet = pyexcel.get_array(file_type=extension, file_content=content)

            i = len(sheet[0])
            th = sheet[0]
            del sheet[0]


            for fila in range(len(sheet)):
                for col in range(len(sheet[0])):
            #        if type(sheet[fila][col]) != types.UnicodeType:
                    sheet[fila][col] = str(sheet[fila][col])

            for s in sheet:
                if verificar(s[0]) == True: #morningstar

                    try:
                        b = bindex.objects.get(morningstar=str(s[0].strip()))
                    except bindex.DoesNotExist:
                        b = bindex(morningstar=str(s[0].strip()))
                        b.save()

                    try:
                        ce = countryExposure.objects.get(bindex=b)
                        respuesta += 'Fila '+str(s[0])+' ya existe<br>'

                    except ce.DoesNotExist:
                        ce = countryExposure.objects.get(bindex = b)
                        ce.save()

                        res = '{'
                        i = 1
                        while verificar(s[i]) == True:
                            try:
                                pa = pais.objects.get(nombre_ing=s[i])
                                res += '"'+str(pa.id)+'" : '
                            except pais.DoesNotExist:
                                res += '"---" : '
                            if verificar(s[i+1]) == True:
                                res += str(s[i+1])+', '
                            else:
                                res += '0, '
                            i +=2
                        res = res[:-2]
                        res +='}'

                        ce.country_exposure = res
                        ce.save()
                    respuesta += 'Fila '+str(s[0])+' insertada<br>'
        except MultiValueDictKeyError:
            pass
        respuesta += '=============FIN COUNTRY EXPOSURE============='


        return render(request, 'datos/importar.html', {'form': form, 'usuario': request.user,  "respuesta" : respuesta})

    else:
        form = Formimportarlista()
        return render(request, 'datos/importar.html', {'form': form, 'usuario': request.user})
