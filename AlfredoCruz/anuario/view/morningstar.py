import requests

from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from bs4 import BeautifulSoup, element, SoupStrainer

from anuario.models import countryExposure, pais, bindex, sector, asignacionActivo, rentabilidad, fondo, categoria, moneda, reporte_anual_cuota, precio_actual, broadCategory, instrumento, branding, frecuenciaDistribucion, rendimiento, tipoInstrumento, proveedor, domicilio

accesscode = "wng36fxdhjnqdejq8iduqh5spo8ukiyk"

def country_exposure():
    magnitud = 'CountryExposure'

    listamstar = list(bindex.objects.all())
    #mstar ='F00000V420'
    for mstar in listamstar:
        print(mstar.morningstar_id)
        try:
            b = bindex.objects.get(morningstar_id=mstar.morningstar_id)
        except bindex.DoesNotExist:
            b = bindex(morningstar_id=mstar)
            b.save()

        u = 'http://api.morningstar.com/v2/service/mf/'+magnitud+'/mstarid/'+mstar.morningstar_id+'?accesscode='+accesscode
        page = requests.get(u)
        soup = BeautifulSoup(page.content, 'html.parser')

        if soup.find('code').get_text() == '0':
            datos = soup.find('countryexposure')
            #soup = BeautifulSoup(page.content, 'lxml')
            paises = datos.findAll('breakdown')
            res = '{'
            for p in paises:
                p1 = p.find('country').get_text()
                p2 = p.find('value').get_text()

                try:
                    pai = pais.objects.get(nombre_ing=p1)
                    pai = pai.id
                except pais.DoesNotExist:
                    pai = 'ND'

                res+= '"'+str(pai)+'" : "'+str(p2)+'", '

            res = res[:-2]
            res +='}'

            res2 = None
            datos = soup.find('countryexposureequity')
            if datos != None:
                paises = datos.findAll('breakdown')
                res2 = '{'
                for p in paises:
                    p1 = p.find('country').get_text()
                    p2 = p.find('value').get_text()

                    try:
                        pai = pais.objects.get(nombre_ing=p1)
                        pai = pai.id
                    except pais.DoesNotExist:
                        pai = 'ND'

                    res2+= '"'+str(pai)+'" : "'+str(p2)+'", '

                res2 = res2[:-2]
                res2 +='}'

            res3 = None
            datos = soup.find('countryexposurebond')
            if datos != None:
                paises = datos.findAll('breakdown')
                res3 = '{'
                for p in paises:
                    p1 = p.find('country').get_text()
                    p2 = p.find('value').get_text()

                    try:
                        pai = pais.objects.get(nombre_ing=p1)
                        pai = pai.id
                    except pais.DoesNotExist:
                        pai = 'ND'

                    res3+= '"'+str(pai)+'" : "'+str(p2)+'", '

                res3 = res3[:-2]
                res3 +='}'

            res4 = None
            datos = soup.find('countryexposureconvertible')
            if datos != None:
                paises = datos.findAll('breakdown')
                res4 = '{'
                for p in paises:
                    p1 = p.find('country').get_text()
                    p2 = p.find('value').get_text()

                    try:
                        pai = pais.objects.get(nombre_ing=p1)
                        pai = pai.id
                    except pais.DoesNotExist:
                        pai = 'ND'

                    res4+= '"'+str(pai)+'" : "'+str(p2)+'", '

                res4 = res4[:-2]
                res4 +='}'
            try:
                ce =countryExposure.objects.get(bindex=b)
            except countryExposure.DoesNotExist:
                ce =countryExposure(bindex=b)
                ce.save()


            ce.country_exposure = res
            if res2 != None:
                ce.country_exposure_equity = res2
            if res3 != None:
                ce.country_exposure_bond = res3
            if res4 != None:
                ce.country_exposure_convertible = res4
            ce.save()
        else:
            pass


    return HttpResponse("CountryExposure guardado")

def global_sector():
    magnitud = 'GlobalStockSectorBreakdown'
    #mstar ='F00000V420'
    listamstar = list(bindex.objects.all())
    for mstar in listamstar:

        try:
            b = bindex.objects.get(morningstar_id=mstar.morningstar_id)
        except bindex.DoesNotExist:
            b = bindex(morningstar_id=mstar)
            b.save()

        u = 'http://api.morningstar.com/v2/service/mf/'+magnitud+'/mstarid/'+mstar.morningstar_id+'?accesscode='+accesscode
        page = requests.get(u)
        soup = BeautifulSoup(page.content, 'html.parser')
        #soup = BeautifulSoup(page.content, 'lxml')
        if soup != None:
            try:
                materiales_basicos = soup.find('basicmaterials').get_text()
            except AttributeError:
                materiales_basicos = None

            try:
                servicio_comunicacion = soup.find('communicationservices').get_text()
            except AttributeError:
                servicio_comunicacion = None

            try:
                ciclico_consumidor = soup.find('consumercyclical').get_text()
            except AttributeError:
                ciclico_consumidor = None

            try:
                defensa_consumidor = soup.find('consumerdefensive').get_text()
            except AttributeError:
                defensa_consumidor = None

            try:
                servicios_financieros = soup.find('financialservices').get_text()
            except AttributeError:
                servicios_financieros = None

            try:
                acciones_industriales = soup.find('industrials').get_text()
            except AttributeError:
                acciones_industriales = None

            try:
                bienes_raices = soup.find('realestate').get_text()
            except AttributeError:
                bienes_raices = None

            try:
                tecnologia = soup.find('technology').get_text()
            except AttributeError:
                tecnologia = None

            try:
                utilidades = soup.find('utilities').get_text()
            except AttributeError:
                utilidades = None

            try:
                portafolio_fecha = soup.find('portfoliodate').get_text()
            except AttributeError:
                portafolio_fecha = None

            #energia = soup.find('consumerdefensive').get_text() #Energy
            #cuidado_salud = models.FloatField()#HealthCare


            try:
                se =sector.objects.get(bindex=b)
            except sector.DoesNotExist:
                se =sector(bindex=b)
                se.save()

            se.materiales_basicos = materiales_basicos
            se.servicio_comunicacion = servicio_comunicacion
            se.ciclico_consumidor = ciclico_consumidor
            se.defensa_consumidor = defensa_consumidor
            se.servicios_financieros = servicios_financieros
            se.acciones_industriales = acciones_industriales
            se.bienes_raices = bienes_raices
            se.tecnologia = tecnologia
            se.utilidades = utilidades
            se.portafolio_fecha = portafolio_fecha
            se.save()
        else:
            pass


    return HttpResponse("Sector guardado")

def asset_allocation():
    magnitud = 'AssetAllocationBreakdown'
    #mstar ='F00000V420'

    listamstar = list(bindex.objects.all())
    for mstar in listamstar:

        try:
            b = bindex.objects.get(morningstar_id=mstar.morningstar_id)
        except bindex.DoesNotExist:
            b = bindex(morningstar_id=mstar)
            b.save()

        u = 'http://api.morningstar.com/v2/service/mf/'+magnitud+'/mstarid/'+mstar.morningstar_id+'?accesscode='+accesscode
        page = requests.get(u)
        soup = BeautifulSoup(page.content, 'html.parser')

        if soup != None:
            try:
                red_bono = soup.find('bondlong').get_text()
            except AttributeError:
                red_bono = None

            try:
                red_efectivo = soup.find('cashlong').get_text()
            except AttributeError:
                red_efectivo = None

            try:
                red_convertible = soup.find('convertiblelong').get_text()
            except AttributeError:
                red_convertible = None

            try:
                red_preferida = soup.find('preferredlong').get_text()
            except AttributeError:
                red_preferida = None

            try:
                red_acciones = soup.find('stocklong').get_text()
            except AttributeError:
                red_acciones = None

            try:
                red_otra = soup.find('otherlong').get_text()
            except AttributeError:
                red_otra = None

            try:
                portafolio_fecha = soup.find('portfoliodate').get_text()
            except AttributeError:
                portafolio_fecha = None


            try:
                a =asignacionActivo.objects.get(bindex=b)
            except asignacionActivo.DoesNotExist:
                a =asignacionActivo(bindex=b)
                a.save()

            a.red_bono = red_bono
            a.red_efectivo = red_efectivo
            a.red_convertible = red_convertible
            a.red_preferida = red_preferida
            a.red_acciones = red_acciones
            a.red_otra = red_otra
            a.portafolio_fecha = portafolio_fecha
            a.save()
        else:
            pass


    return HttpResponse("Asset allocation de "+str(mstar)+" guardados")

def daily_performance():
    magnitud = 'DailyPerformance'
    #mstar ='F00000V420'
    i= 1
    listamstar = list(bindex.objects.all())
    for mstar in listamstar:

        try:
            b = bindex.objects.get(morningstar_id=mstar.morningstar_id)
        except bindex.DoesNotExist:
            b = bindex(morningstar_id=mstar)
            b.save()

        u = 'http://api.morningstar.com/v2/service/mf/'+magnitud+'/mstarid/'+mstar.morningstar_id+'?accesscode='+accesscode
        page = requests.get(u)
        soup = BeautifulSoup(page.content, 'html.parser')

        if soup != None:
            try:
                fundname = soup.find('fundname').get_text()
                try:
                    f = fondo.objects.get(nombre=fundname)
                except fondo.DoesNotExist:
                    catcode = soup.find('categorycode').get_text()

                    try:
                        c = categoria.objects.get(id=catcode)
                    except categoria.DoesNotExist:
                        catname = soup.find('categoryname').get_text()
                        c = categoria(id=catcode, nombre=catname)
                        c.save()

                    try:
                        currency =  soup.find('currency').get_text()
                        m = moneda.objects.get(nombre=currency)
                    except moneda.DoesNotExist:
                        m = None


                    f = fondo(id = catcode, nombre=fundname, categoria= c, moneda= m)
                    f.save()
            except AttributeError:
                f = None

            try:
                DayEndDate = soup.find('dayenddate').get_text()
            except AttributeError:
                DayEndDate = None

            try:
                DayEndNAV = soup.find('dayendnav').get_text()
            except AttributeError:
                DayEndNAV = None

            try:
                NAVChange = soup.find('navchange').get_text()
            except AttributeError:
                NAVChange = None

            try:
                NAVChangePercentage = soup.find('navchangepercentage').get_text()
            except AttributeError:
                NAVChangePercentage = None

            Retorno = '{'
            try:
                Return1Day = soup.find('return1day').get_text()
                Retorno += '"Return1Day" : "'+Return1Day+'", '
            except AttributeError:
                pass
            try:
                Return1Week = soup.find('return1week').get_text()
                Retorno += '"Return1Week" : "'+Return1Week+'", '
            except AttributeError:
                pass
            try:
                Return1Mth = soup.find('return1mth').get_text()
                Retorno += '"Return1Mth" : "'+Return1Mth+'", '
            except AttributeError:
                pass

            try:
                Return2Mth = soup.find('return2mth').get_text()
                Retorno += '"Return2Mth" : "'+Return2Mth+'", '
            except AttributeError:
                pass

            try:
                Return3Mth = soup.find('return3mth').get_text()
                Retorno += '"Return3Mth" : "'+Return3Mth+'", '
            except AttributeError:
                pass

            try:
                Return6Mth = soup.find('return6mth').get_text()
                Retorno += '"Return6Mth" : "'+Return6Mth+'", '
            except AttributeError:
                pass

            try:
                Return1Yr = soup.find('return1yr').get_text()
                Retorno += '"Return1Yr" : "'+Return1Yr+'", '
            except AttributeError:
                pass

            try:
                Return2Yr = soup.find('return2yr').get_text()
                Retorno += '"Return2Yr" : "'+Return2Yr+'", '
            except AttributeError:
                pass

            try:
                ReturnMTD = soup.find('returnmtd').get_text()
                Retorno += '"ReturnMTD" : "'+ReturnMTD+'", '
            except AttributeError:
                pass

            try:
                ReturnQTD = soup.find('returnqtd').get_text()
                Retorno += '"ReturnQTD" : "'+ReturnQTD+'", '
            except AttributeError:
                pass

            try:
                ReturnYTD = soup.find('returnytd').get_text()
                Retorno += '"ReturnYTD" : "'+ReturnYTD+'", '
            except AttributeError:
                pass

            try:
                ReturnSinceInception = soup.find('returnsinceinception').get_text()
                Retorno += '"ReturnSinceInception" : "'+ReturnSinceInception+'", '
            except AttributeError:
                pass

            if Retorno != '{':
                Retorno = Retorno[:-2]
            Retorno +='}'



            Rank = '{'
            try:
                Rank1Day = soup.find('rank1day').get_text()
                Rank += '"Rank1Day" : "'+Rank1Day+'", '
            except AttributeError:
                pass
            try:
                Rank1Week = soup.find('rank1week').get_text()
                Rank += '"Rank1Week" : "'+Rank1Week+'", '
            except AttributeError:
                pass
            try:
                Rank1Mth = soup.find('rank1mth').get_text()
                Rank += '"Rank1Mth" : "'+Rank1Mth+'", '
            except AttributeError:
                pass

            try:
                Rank2Mth = soup.find('rank2mth').get_text()
                Rank += '"Rank2Mth" : "'+Rank2Mth+'", '
            except AttributeError:
                pass

            try:
                Rank3Mth = soup.find('rank3mth').get_text()
                Rank += '"Rank3Mth" : "'+Rank3Mth+'", '
            except AttributeError:
                pass

            try:
                Rank6Mth = soup.find('rank6mth').get_text()
                Rank += '"Rank6Mth" : "'+Rank6Mth+'", '
            except AttributeError:
                pass

            try:
                RankMTD = soup.find('rankmtd').get_text()
                Rank += '"RankMTD" : "'+RankMTD+'", '
            except AttributeError:
                pass

            try:
                RankQTD = soup.find('rankqtd').get_text()
                Rank += '"RankQTD" : "'+RankQTD+'", '
            except AttributeError:
                pass

            try:
                RankYTD = soup.find('rankytd').get_text()
                Rank += '"RankYTD" : "'+RankYTD+'", '
            except AttributeError:
                pass

            if Rank != '{':
                Rank = Rank[:-2]
            Rank +='}'




            CategoryReturn = '{'
            try:
                CategoryReturn1Day = soup.find('categoryreturn1day').get_text()
                CategoryReturn += '"CategoryReturn1Day" : "'+CategoryReturn1Day+'", '
            except AttributeError:
                pass
            try:
                CategoryReturn1Week = soup.find('categoryreturn1week').get_text()
                CategoryReturn += '"CategoryReturn1Week" : "'+CategoryReturn1Week+'", '
            except AttributeError:
                pass
            try:
                CategoryReturn1Mth = soup.find('categoryreturn1mth').get_text()
                CategoryReturn += '"CategoryReturn1Mth" : "'+CategoryReturn1Mth+'", '
            except AttributeError:
                pass

            try:
                CategoryReturn2Mth = soup.find('categoryreturn2mth').get_text()
                CategoryReturn += '"CategoryReturn2Mth" : "'+CategoryReturn2Mth+'", '
            except AttributeError:
                pass

            try:
                CategoryReturn3Mth = soup.find('categoryreturn3mth').get_text()
                CategoryReturn += '"CategoryReturn3Mth" : "'+CategoryReturn3Mth+'", '
            except AttributeError:
                pass

            try:
                CategoryReturn6Mth = soup.find('categoryreturn6mth').get_text()
                CategoryReturn += '"CategoryReturn6Mth" : "'+CategoryReturn6Mth+'", '
            except AttributeError:
                pass

            try:
                CategoryReturn1Yr = soup.find('categoryreturn1yr').get_text()
                CategoryReturn += '"CategoryReturn1Yr" : "'+CategoryReturn1Yr+'", '
            except AttributeError:
                pass

            try:
                CategoryReturn3Yr = soup.find('categoryreturn3yr').get_text()
                CategoryReturn += '"CategoryReturn3Yr" : "'+CategoryReturn3Yr+'", '
            except AttributeError:
                pass

            try:
                CategoryReturn5Yr = soup.find('categoryreturn5yr').get_text()
                CategoryReturn += '"CategoryReturn5Yr" : "'+CategoryReturn5Yr+'", '
            except AttributeError:
                pass

            try:
                CategoryReturn10Yr = soup.find('categoryreturn10yr').get_text()
                CategoryReturn += '"CategoryReturn10Yr" : "'+CategoryReturn10Yr+'", '
            except AttributeError:
                pass

            try:
                CategoryReturn10Yr = soup.find('categoryreturn10yr').get_text()
                CategoryReturn += '"CategoryReturn10Yr" : "'+CategoryReturn10Yr+'", '
            except AttributeError:
                pass

            try:
                CategoryReturn15Yr = soup.find('categoryreturn15yr').get_text()
                CategoryReturn += '"CategoryReturn15Yr" : "'+CategoryReturn15Yr+'", '
            except AttributeError:
                pass

            try:
                CategoryReturn20Yr = soup.find('categoryreturn20yr').get_text()
                CategoryReturn += '"CategoryReturn20Yr" : "'+CategoryReturn20Yr+'", '
            except AttributeError:
                pass

            try:
                CategoryReturnMTD = soup.find('categoryreturnmtd').get_text()
                CategoryReturn += '"CategoryReturnMTD" : "'+CategoryReturnMTD+'", '
            except AttributeError:
                pass

            try:
                CategoryReturnQTD = soup.find('categoryreturnqtd').get_text()
                CategoryReturn += '"CategoryReturnQTD" : "'+CategoryReturnQTD+'", '
            except AttributeError:
                pass

            try:
                CategoryReturnYTD = soup.find('categoryreturnytd').get_text()
                CategoryReturn += '"CategoryReturnYTD" : "'+CategoryReturnYTD+'", '
            except AttributeError:
                pass


            if CategoryReturn != '{':
                CategoryReturn = CategoryReturn[:-2]
            CategoryReturn +='}'




            CategorySize = '{'
            try:
                CategorySize1Day = soup.find('categorysize1day').get_text()
                CategorySize += '"CategorySize1Day" : "'+CategorySize1Day+'", '
            except AttributeError:
                pass
            try:
                CategorySize1Week = soup.find('categorysize1week').get_text()
                CategorySize += '"CategorySize1Week" : "'+CategorySize1Week+'", '
            except AttributeError:
                pass
            try:
                CategorySize1Mth = soup.find('categorysize1mth').get_text()
                CategorySize += '"CategorySize1Mth" : "'+CategorySize1Mth+'", '
            except AttributeError:
                pass

            try:
                CategorySize2Mth = soup.find('categorysize2mth').get_text()
                CategorySize += '"CategorySize2Mth" : "'+CategorySize2Mth+'", '
            except AttributeError:
                pass

            try:
                CategorySize3Mth = soup.find('categorysize3mth').get_text()
                CategorySize += '"CategorySize3Mth" : "'+CategorySize3Mth+'", '
            except AttributeError:
                pass

            try:
                CategorySize6Mth = soup.find('categorysize6mth').get_text()
                CategorySize += '"CategorySize6Mth" : "'+CategorySize6Mth+'", '
            except AttributeError:
                pass

            try:
                CategorySize1Yr = soup.find('categorysize1yr').get_text()
                CategorySize += '"CategorySize1Yr" : "'+CategorySize1Yr+'", '
            except AttributeError:
                pass

            try:
                CategorySize3Yr = soup.find('categorysize3yr').get_text()
                CategorySize += '"CategorySize3Yr" : "'+CategorySize3Yr+'", '
            except AttributeError:
                pass

            try:
                CategorySize5Yr = soup.find('categorysize5yr').get_text()
                CategorySize += '"CategorySize5Yr" : "'+CategorySize5Yr+'", '
            except AttributeError:
                pass

            try:
                CategorySize10Yr = soup.find('categorysize10yr').get_text()
                CategorySize += '"CategorySize10Yr" : "'+CategorySize10Yr+'", '
            except AttributeError:
                pass

            try:
                CategorySize10Yr = soup.find('categorysize10yr').get_text()
                CategorySize += '"CategorySize10Yr" : "'+CategorySize10Yr+'", '
            except AttributeError:
                pass

            try:
                CategorySize15Yr = soup.find('categorysize15yr').get_text()
                CategorySize += '"CategorySize15Yr" : "'+CategorySize15Yr+'", '
            except AttributeError:
                pass

            try:
                CategorySize20Yr = soup.find('categorysize20yr').get_text()
                CategorySize += '"CategorySize20Yr" : "'+CategorySize20Yr+'", '
            except AttributeError:
                pass

            try:
                CategorySizeMTD = soup.find('categorysizemtd').get_text()
                CategorySize += '"CategorySizeMTD" : "'+CategorySizeMTD+'", '
            except AttributeError:
                pass

            try:
                CategorySizeQTD = soup.find('categorysizeqtd').get_text()
                CategorySize += '"CategorySizeQTD" : "'+CategorySizeQTD+'", '
            except AttributeError:
                pass

            try:
                CategorySizeYTD = soup.find('categorysizeytd').get_text()
                CategorySize += '"CategorySizeYTD" : "'+CategorySizeYTD+'", '
            except AttributeError:
                pass


            if CategorySize != '{':
                CategorySize = CategorySize[:-2]
            CategorySize +='}'

            try:
                PricingFrequency = soup.find('PricingFrequency').get_text()
            except AttributeError:
                PricingFrequency = None

            try:
                r =rentabilidad.objects.get(bindex=b, fondo= f)
            except rentabilidad.DoesNotExist:
                r =rentabilidad(bindex=b, fondo = f)
                r.save()

            r.DayEndDate = DayEndDate
            r.DayEndNAV = DayEndNAV
            r.NAVChange = NAVChange
            r.NAVChangePercentage = NAVChangePercentage
            r.Retorno = Retorno
            r.Rank = Rank
            r.CategoryReturn = CategoryReturn
            r.CategorySize = CategorySize
            r.PricingFrequency = PricingFrequency
            r.save()

            print(str(i)+'.-'+mstar.morningstar_id)
            i +=1
        else:
            pass


    return HttpResponse("Daily Performance - datos guardados")

def anual_report_fees():
    magnitud = 'AnnualReportFees'
    listamstar = list(bindex.objects.all())
    for mstar in listamstar:

        try:
            b = bindex.objects.get(morningstar_id=mstar.morningstar_id)
        except bindex.DoesNotExist:
            b = bindex(morningstar_id=mstar)
            b.save()

        u = 'http://api.morningstar.com/v2/service/mf/'+magnitud+'/mstarid/'+mstar.morningstar_id+'?accesscode='+accesscode
        page = requests.get(u)
        soup = BeautifulSoup(page.content, 'html.parser')
        #soup = BeautifulSoup(page.content, 'lxml')
        if soup != None:
            try:
                AnnualReportDate = soup.find('annualreportdate').get_text()
            except AttributeError:
                AnnualReportDate = None

            try:
                NetExpenseRatio = soup.find('netexpenseratio').get_text()
            except AttributeError:
                NetExpenseRatio = None

            try:
                AnnualReportPerformanceFee = soup.find('annualreportperformancefee').get_text()
            except AttributeError:
                AnnualReportPerformanceFee = None

            try:
                InterimNetExpenseRatioDate = soup.find('interimnetexpenseratiodate').get_text()
            except AttributeError:
                InterimNetExpenseRatioDate = None

            try:
                InterimNetExpenseRatio = soup.find('interimnetexpenseratio').get_text()
            except AttributeError:
                InterimNetExpenseRatio = None


            try:
                r =reporte_anual_cuota.objects.get(bindex=b)
            except reporte_anual_cuota.DoesNotExist:
                r =reporte_anual_cuota(bindex=b)
                r.save()

            r.AnnualReportDate = AnnualReportDate
            r.NetExpenseRatio = NetExpenseRatio
            r.AnnualReportPerformanceFee = AnnualReportPerformanceFee
            r.InterimNetExpenseRatioDate = InterimNetExpenseRatioDate
            r.InterimNetExpenseRatio = InterimNetExpenseRatio
            r.save()
            print(mstar.morningstar_id)
        else:
            pass


    return HttpResponse("reporte anual guardado")

def current_price():
    magnitud = 'CurrentPrice'
    listamstar = list(bindex.objects.all())
    for mstar in listamstar:

        try:
            b = bindex.objects.get(morningstar_id=mstar.morningstar_id)
        except bindex.DoesNotExist:
            b = bindex(morningstar_id=mstar)
            b.save()

        u = 'http://api.morningstar.com/v2/service/mf/'+magnitud+'/mstarid/'+mstar.morningstar_id+'?accesscode='+accesscode
        page = requests.get(u)
        soup = BeautifulSoup(page.content, 'html.parser')
        #soup = BeautifulSoup(page.content, 'lxml')
        if soup != None:
            try:
                DayEndNAVDate = soup.find('dayendnavdate').get_text()
            except AttributeError:
                DayEndNAVDate = None

            try:
                DayEndNAV = soup.find('dayendnav').get_text()
            except AttributeError:
                DayEndNAV = None

            try:
                MonthEndNAVDate = soup.find('monthendnavdate').get_text()
            except AttributeError:
                MonthEndNAVDate = None

            try:
                MonthEndNAV = soup.find('monthendnav').get_text()
            except AttributeError:
                MonthEndNAV = None

            try:
                UnsplitNAV = soup.find('unsplitnav').get_text()
            except AttributeError:
                UnsplitNAV = None

            try:
                CurrencyISO3 = soup.find('currencyiso3').get_text()
                try:
                    c = moneda.objects.get(id__endswith=CurrencyISO3)
                except moneda.DoesNotExist:
                    c = None
            except AttributeError:
                c = None

            try:
                NAV52wkHigh = soup.find('nav52wkhigh').get_text()
            except AttributeError:
                NAV52wkHigh = None

            try:
                NAV52wkHighDate = soup.find('nav52wkhighdate').get_text()
            except AttributeError:
                NAV52wkHighDate = None

            try:
                NAV52wkLow = soup.find('nav52wklow').get_text()
            except AttributeError:
                NAV52wkLow = None

            try:
                NAV52wkLowDate = soup.find('nav52wklowdate').get_text()
            except AttributeError:
                NAV52wkLowDate = None

            try:
                PerformanceReturnSource = soup.find('performancereturnsource').get_text()
            except AttributeError:
                PerformanceReturnSource = None

            try:
                p=precio_actual.objects.get(bindex=b)
            except precio_actual.DoesNotExist:
                p =precio_actual(bindex=b)
                p.save()

            p.DayEndNAVDate = DayEndNAVDate
            p.DayEndNAV = DayEndNAV
            p.MonthEndNAVDate = MonthEndNAVDate
            p.MonthEndNAV = MonthEndNAV
            p.UnsplitNAV = UnsplitNAV
            p.NAV52wkHigh = NAV52wkHigh
            p.NAV52wkHighDate = NAV52wkHighDate
            p.NAV52wkLow = NAV52wkLow
            p.NAV52wkLowDate = NAV52wkLowDate
            p.PerformanceReturnSource = PerformanceReturnSource
            p.CurrencyISO3 = c
            p.save()
            print(mstar.morningstar_id)
        else:
            pass


    return HttpResponse("reporte anual guardado")

def fund_info():
    magnitud = 'FundShareClassBasicInfo'

    listamstar = list(bindex.objects.all())
    #mstar ='F00000V420'
    for mstar in listamstar:
        print(mstar.morningstar_id)
        try:
            b = bindex.objects.get(morningstar_id=mstar.morningstar_id)
        except bindex.DoesNotExist:
            b = bindex(morningstar_id=mstar)
            b.save()

        u = 'http://api.morningstar.com/v2/service/mf/'+magnitud+'/mstarid/'+mstar.morningstar_id+'?accesscode='+accesscode
        page = requests.get(u)
        soup = BeautifulSoup(page.content, 'html.parser')
        if soup.find('code').get_text() == '0':
            #primero categoria

            try:
                broadcategorygroupid = soup.find('broadcategorygroupid').get_text()
                try:
                    bc = broadCategory.objects.get(id= broadcategorygroupid)
                except broadCategory.DoesNotExist:
                    BroadCategoryGroup = soup.find('broadcategorygroup').get_text()
                    bc = broadCategory(id=broadcategorygroupid, nombre= BroadCategoryGroup)
                    bc.save()

            except AttributeError:
                bc = None

            try:
                CurrencyId = soup.find('currencyid').get_text()
                try:
                    m = moneda.objects.get(id= CurrencyId)
                except moneda.DoesNotExist:
                    Currency = soup.find('currency').get_text()
                    m = moneda(id=CurrencyId, nombre= Currency)
                    m.save()

            except AttributeError:
                m = None

            try:
                CategoryCode = soup.find('categorycode').get_text()
                try:
                    cat = categoria.objects.get(id=CategoryCode)
                except categoria.DoesNotExist:
                    CategoryName = soup.find('categoryname').get_text()

                    cat = categoria(id=CategoryCode, nombre=CategoryName, broadcategory= bc, moneda=m)
                    cat.save()

            except AttributeError:
                cat = None

            try:
                DomicileId = soup.find('domicileid').get_text()
                try:
                    dom = domicilio.objects.get(id=DomicileId)
                except domicilio.DoesNotExist:
                    Domicile = soup.find('domicile').get_text()

                    dom = domicilio(id=DomicileId, nombre=Domicile)
                    dom.save()

            except AttributeError:
                dom = None


            #FONDO
            try:
                nombre = soup.find('fundname').get_text()
            except AttributeError:
                nombre= None

            try:
                nombre_legal = soup.find('legalname').get_text()
            except AttributeError:
                nombre= None

            try:
                fecha_inicio = soup.find('inceptiondate').get_text()
            except AttributeError:
                fecha_inicio = None

            try:
                fund_id = soup.find('fundid').get_text()
                try:
                    f = fondo.objects.get(id = fund_id)
                except fondo.DoesNotExist:
                    nombre_fondo = soup.find('fundname').get_text()
                    f = fondo(id=fund_id, nombre=nombre_fondo)
                    f.save()

                f.domicilio = dom
                f.categoria = cat
                f.moneda = m
                f.save()
            except AttributeError:
                f =None

            #instrumento



            try:
                FundStandardName = soup.find('fundstandardname').get_text()
            except AttributeError:
                fundstandardname = None


            try:
                RUN = soup.find('run').get_text()
            except AttributeError:
                RUN = None

            try:
                CompanyClassType = soup.find('companyclasstype').get_text()
            except AttributeError:
                CompanyClassType = None

            try:
                OperationReady = soup.find('operationready').get_text()
            except AttributeError:
                OperationReady = None

            try:
                BrandingID = soup.find('brandingid').get_text()
                try:
                    br = branding.objects.get(id = BrandingID)
                except branding.DoesNotExist:
                    BrandingName = soup.find('BrandingName').get_text()
                    br = branding(id=BrandingID, nombre=BrandingName)
                    br.save()
            except AttributeError:
                br =None

            try:
                DistributionStatus = soup.find('DistributionStatus').get_text()
                try:
                    fd = frecuenciaDistribucion.objects.get(nombre = DistributionStatus)
                except frecuenciaDistribucion.DoesNotExist:
                    fd = frecuenciaDistribucion(nombre=DistributionStatus)
                    fd.save()
            except AttributeError:
                fd =None

            try:
                PerformanceID = soup.find('performanceid').get_text()
                try:
                    rend = rendimiento.objects.get(pk = PerformanceID)
                except rendimiento.DoesNotExist:
                    rend = None
            except AttributeError:
                rend =None

            if soup.find('domicile').get_text() == 'Chile':
                tinstr = tipoInstrumento.objects.get(pk = 1)
            else:
                tinstr = tipoInstrumento.objects.get(pk = 2)


            try:
                ProviderCompanyID = soup.find('providercompanyid').get_text()
                try:
                    prov = proveedor.objects.get(id = ProviderCompanyID)
                except proveedor.DoesNotExist:
                    ProviderCompanyName = soup.find('providercompanyname').get_text()
                    prov = branding(id=ProviderCompanyID, nombre=ProviderCompanyName)

                    ProviderCompanyWebsite = soup.find('providercompanywebsite').get_text()
                    ProviderCompanyPhoneNumber = soup.find('providercompanyphonenumber').get_text()

                    prov.datos = '{"website": "'+str(ProviderCompanyWebsite)+'" , "Telefono" : "'+str(ProviderCompanyPhoneNumber)+'"}'
                    prov.save()
            except AttributeError:
                prov =None

            print(mstar.morningstar_id)
            try:
                i =instrumento.objects.get(bindex=b)
            except instrumento.DoesNotExist:
                i =instrumento(bindex=b)
                i.proveedor = prov
                i.tipoInstrumento = tinstr
                i.branding = br
                i.frecuenciaDistribucion = fd
                i.rendimiento = rend

                i.operation_ready = OperationReady
                i.clase_proveedor = CompanyClassType
                i.run_svs = RUN
                i.nombre = FundStandardName
                i.fondo = f
                i.save()



            #soup = BeautifulSoup(page.content, 'lxml')
        else:
            pass
