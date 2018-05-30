from django.contrib import admin
from django.db import models
from datetime import datetime, date, time, timedelta
'''
# class morningstar(models.Model):
#     id = models.CharField(max_length=15, primary_key=True)
#     country_exposure = models.TextField() #como json
# class morningstarAdmin(admin.ModelAdmin):
#     list_display = ['country_exposure']
#     search_fields = ['country_exposure']
# admin.site.register(morningstar, morningstarAdmin)'''

# *** = CAMBIOS EN COMPARACION AL MODELO ANTERIOR

#***
#se agrega morningstar_id y se elimina el campo country_exposure,
# ya que se decide que debe tener su propia tabla
class bindex(models.Model):
    morningstar_id = models.CharField(max_length=15)
class bindexAdmin(admin.ModelAdmin):
    list_display = ['id','morningstar_id']
    search_fields = ['id','morningstar_id']
admin.site.register(bindex, bindexAdmin)

class moneda(models.Model):#Currency
    id = models.CharField(max_length=15, primary_key=True)
    nombre = models.CharField(max_length=50)
class monedaAdmin(admin.ModelAdmin):
    list_display = ['nombre']
    search_fields = ['nombre']
admin.site.register(moneda, monedaAdmin)

class broadCategory(models.Model): #broadCategoryGroup
    id = models.CharField(max_length=15, primary_key=True)
    nombre = models.CharField(max_length=50)
class broadCategoryAdmin(admin.ModelAdmin):
    list_display = ['id','nombre']
    search_fields = ['id','nombre']
admin.site.register(broadCategory, broadCategoryAdmin)

class categoria(models.Model):#CategoryCurrency
    id = models.CharField(max_length=15, primary_key=True)
    nombre = models.CharField(max_length=50)
    broadCategory = models.ForeignKey(broadCategory, on_delete=models.CASCADE)
    moneda = models.ForeignKey(moneda, on_delete=models.CASCADE)
class categoriaAdmin(admin.ModelAdmin):
    list_display = ['nombre','broadCategory','moneda']
    search_fields = ['nombre','broadCategory','moneda']
admin.site.register(categoria, categoriaAdmin)

class domicilio(models.Model):#Domicile
    id = models.CharField(max_length=15, primary_key=True)
    nombre = models.CharField(max_length=50)
class domicilioAdmin(admin.ModelAdmin):
    list_display = ['id','nombre']
    search_fields = ['id','nombre']
admin.site.register(domicilio, domicilioAdmin)

#***
#se eliminan los campos estructura_legal y estado_distribucion
#se agregan los campos FFMM Nacional y FFMM Internacional
class tipoInstrumento(models.Model):
    id = models.CharField(max_length=15, primary_key=True)
    nombre = models.CharField(max_length=50)
    def __str__(self):
        return self.nombre

class tipoInstrumentoAdmin(admin.ModelAdmin):
    list_display = ['nombre']
    search_fields = ['nombre']
admin.site.register(tipoInstrumento, tipoInstrumentoAdmin)

#***
#se agregan los campos nombre y run
class proveedor(models.Model):#ProviderCompany
    id = models.CharField(max_length=10, primary_key=True)
    nombre = models.CharField(max_length=50)
    datos = models.TextField() #como json
class proveedorAdmin(admin.ModelAdmin):
    list_display = ['id','nombre','datos']
    search_fields = ['id','nombre','datos']
admin.site.register(proveedor, proveedorAdmin)

class fondo(models.Model):
    id = models.CharField(max_length=15, primary_key=True)
    nombre = models.CharField(max_length=50,null=True, blank=True)
    nombre_legal = models.CharField(max_length=50,null=True, blank=True)
    fecha_inicio = models.DateField(null=True, blank=True)
    domicilio = models.ForeignKey(domicilio, null=True, blank=True, on_delete=models.CASCADE)
    categoria = models.ForeignKey(categoria,null=True, blank=True, on_delete=models.CASCADE)
    moneda = models.ForeignKey(moneda, null=True, blank=True, on_delete=models.CASCADE)

class fondoAdmin(admin.ModelAdmin):
    list_display = ['nombre','nombre_legal','fecha_inicio','domicilio','categoria','moneda']#definir cuales se necesitan
    search_fields = ['nombre','nombre_legal','fecha_inicio','domicilio','categoria','moneda']#definir cuales se necesitan
admin.site.register(fondo, fondoAdmin)

class frecuenciaDistribucion(models.Model):#DistributionFrecuency
    frecuencia = models.CharField(max_length=50)
class frecuenciaDistribucionAdmin(admin.ModelAdmin):
    list_display = ['frecuencia']
    search_fields = ['frecuencia']
admin.site.register(frecuenciaDistribucion, frecuenciaDistribucionAdmin)

class branding(models.Model): #Branding
    id = models.CharField(max_length=15, primary_key=True)
    nombre = models.CharField(max_length=50)
class brandingAdmin(admin.ModelAdmin):
    list_display = ['nombre']
    search_fields = ['nombre']
admin.site.register(branding, brandingAdmin)

class rendimiento(models.Model):#Performance
    id = models.CharField(max_length=10, primary_key=True)
    estado = models.IntegerField() #PerformanceReady
class rendimientoAdmin(admin.ModelAdmin):
    list_display = ['estado']
    search_fields = ['estado']
admin.site.register(rendimiento, rendimientoAdmin)

class pais(models.Model):
    id = models.CharField(max_length=10, primary_key=True)
    nombre = models.CharField(max_length=50)
    nombre_ing = models.CharField(max_length=50, null=True, blank=True)
class paisAdmin(admin.ModelAdmin):
    list_display = ['nombre']
    search_fields = ['nombre']
admin.site.register(pais, paisAdmin)

class instrumento(models.Model):
    bindex = models.OneToOneField(bindex,on_delete=models.CASCADE, primary_key=True)
    nombre = models.CharField(max_length=50, null=True, blank=True)
    run_svs = models.CharField(max_length=50, null=True, blank=True)
    clase_proveedor = models.CharField(max_length=50, null=True, blank=True)
    operation_ready = models.IntegerField(null=True, blank=True)
    branding = models.ForeignKey(branding, on_delete=models.CASCADE, null=True, blank=True)
    frecuenciaDistribucion = models.ForeignKey(frecuenciaDistribucion, on_delete=models.CASCADE, null=True, blank=True)
    rendimiento = models.ForeignKey(rendimiento, on_delete=models.CASCADE, null=True, blank=True) #Performance
    proveedor = models.ForeignKey(proveedor, on_delete=models.CASCADE, null=True, blank=True)
    tipoInstrumento = models.ForeignKey(tipoInstrumento, on_delete=models.CASCADE, null=True, blank=True)
    fondo = models.ForeignKey(fondo, on_delete=models.CASCADE, null=True, blank=True)

class instrumentoAdmin(admin.ModelAdmin):
    list_display = ['bindex','fondo','branding','frecuenciaDistribucion','rendimiento',
    'run_svs','clase_proveedor','operation_ready']
    search_fields = ['bindex','fondo','branding','frecuenciaDistribucion','rendimiento',
    'run_svs','clase_proveedor','operation_ready']
admin.site.register(instrumento,instrumentoAdmin)

class rentaFija(models.Model):#FixedIncome (excel)
    bindex = models.OneToOneField(bindex,on_delete=models.CASCADE, primary_key=True)
    bsed = models.FloatField()#BondStatisticsEffectiveDuration
    bsem = models.FloatField()#BondStatisticsEffectiveMaturity
    bsmd = models.FloatField()#BondStatisticsModifiedDuration
    bsym = models.FloatField()#BondStatisticsYieldToMaturity
    cred = models.FloatField()#CoverageRatioEffectiveDuration
    crem = models.FloatField()#CoverageRatioEffectiveMaturity
    crmd = models.FloatField()#CoverageRatioModifiedDuration
    crym = models.FloatField()#CoverageRatioYieldToMaturity
    portafolio_fecha = models.DateField()
class rentaFijaAdmin(admin.ModelAdmin):
    list_display = ['bsed','bsem','bsmd','bsym','cred','crem','crmd','crym','portafolio_fecha']
    search_fields = ['bsed','bsem','bsmd','bsym','cred','crem','crmd','crym','portafolio_fecha']
admin.site.register(rentaFija, rentaFijaAdmin)

class sector(models.Model):#SectorExposure
    bindex = models.OneToOneField(bindex,on_delete=models.CASCADE,primary_key=True)
    materiales_basicos = models.FloatField(null=True, blank=True) #BasicMaterials
    servicio_comunicacion = models.FloatField(null=True, blank=True)#CommunicationService
    ciclico_consumidor = models.FloatField(null=True, blank=True)#consumercyclical
    defensa_consumidor = models.FloatField(null=True, blank=True) #consumerDefensive
    energia = models.FloatField(null=True, blank=True) #Energy
    servicios_financieros = models.FloatField(null=True, blank=True) #FinancialServices
    cuidado_salud = models.FloatField(null=True, blank=True)#HealthCare
    acciones_industriales = models.FloatField(null=True, blank=True)#industrials
    bienes_raices = models.FloatField(null=True, blank=True)#RealEstate
    tecnologia = models.FloatField(null=True, blank=True)#Technology
    utilidades = models.FloatField(null=True, blank=True)#Utilities
    portafolio_fecha = models.DateField(null=True, blank=True)
class sectorAdmin(admin.ModelAdmin):
    list_display = ['materiales_basicos','servicio_comunicacion','ciclico_consumidor']#definir que atributos se ocuparan
    search_fields = ['materiales_basicos','servicio_comunicacion','ciclico_consumidor']#definir que atributos se ocuparan
admin.site.register(sector, sectorAdmin)

class asignacionActivo(models.Model):#AssetAllocation
    bindex = models.OneToOneField(bindex,on_delete=models.CASCADE, primary_key=True)
    red_bono = models.FloatField(null=True, blank=True)#BondNet
    red_efectivo = models.FloatField(null=True, blank=True)#CashNet
    red_convertible = models.FloatField(null=True, blank=True)#ConvertibleNet
    red_preferida = models.FloatField(null=True, blank=True)#PreferredNet
    red_acciones = models.FloatField(null=True, blank=True)#Stocknet
    red_otra = models.FloatField(null=True, blank=True)#OtherNet
    portafolio_fecha = models.DateField(null=True, blank=True)#portfolioDate
class asignacionActivoAdmin(admin.ModelAdmin):
    list_display = ['red_bono','red_efectivo','red_convertible','red_preferida','red_acciones','red_otra','portafolio_fecha']
    search_fields = ['red_bono','red_efectivo','red_convertible','red_preferida','red_acciones','red_otra','portafolio_fecha']
admin.site.register(asignacionActivo, asignacionActivoAdmin)

class valorCuota(models.Model):
    bindex = models.OneToOneField(bindex,on_delete=models.CASCADE,primary_key=True)
    anio = models.CharField(max_length=50)
    datos = models.TextField()
class valorCuotaAdmin(admin.ModelAdmin):
    list_display = ['bindex','anio','datos']
    search_fields = ['bindex','anio','datos']
admin.site.register(valorCuota, valorCuotaAdmin)

class claseActivo(models.Model):
    bindex = models.OneToOneField(bindex,on_delete=models.CASCADE,primary_key=True)
    datos = models.TextField()
class claseActivoAdmin(admin.ModelAdmin):
    list_display = ['bindex','datos']
    search_fields = ['bindex','datos']
admin.site.register(claseActivo, claseActivoAdmin)

class tipoInversion(models.Model):
    nombre = models.CharField(max_length=50)
class tipoInversionAdmin(admin.ModelAdmin):
    list_display = ['id','nombre']
    search_fields = ['id','nombre']
admin.site.register(tipoInversion, tipoInversionAdmin)

class tipoMovimiento(models.Model):
    nombre = models.CharField(max_length=50)
class tipoMovimientoAdmin(admin.ModelAdmin):
    list_display = ['id','nombre']
    search_fields = ['id','nombre']
admin.site.register(tipoMovimiento, tipoMovimientoAdmin)

class cliente(models.Model):
    nombre = models.CharField(max_length=50)
    #tipoInversion = models.ForeignKey(tipoInversion, on_delete=models.CASCADE)
class clienteAdmin(admin.ModelAdmin):
    list_display = ['id','nombre']
    search_fields = ['id','nombre']
admin.site.register(cliente, clienteAdmin)

class carteraCliente(models.Model):
    fecha = models.DateField()
    monto = models.IntegerField()
    tipoInversion = models.ForeignKey(tipoInversion, on_delete=models.CASCADE)
    cliente = models.ForeignKey(cliente, on_delete=models.CASCADE)
    bindex = models.ForeignKey(bindex, on_delete=models.CASCADE)
class carteraClienteAdmin(admin.ModelAdmin):
    list_display = ['id','monto','tipoInversion','cliente','bindex']
    search_fields = ['id','monto','tipoInversion','cliente','bindex']
admin.site.register(carteraCliente, carteraClienteAdmin)

class movimiento(models.Model):
    monto = models.IntegerField()
    fecha = models.DateField()
    numero_cuotas =  models.IntegerField()
    cliente = models.ForeignKey(cliente, on_delete=models.CASCADE)
    tipoInversion = models.ForeignKey(tipoInversion, on_delete=models.CASCADE)
    tipoMovimiento = models.ForeignKey(tipoMovimiento, on_delete=models.CASCADE)
    bindex = models.ForeignKey(bindex, on_delete=models.CASCADE)
class movimientoAdmin(admin.ModelAdmin):
    list_display = ['id','monto','fecha','numero_cuotas','cliente','tipoInversion','tipoInversion','bindex']
    search_fields = ['id','monto','fecha','numero_cuotas','cliente','tipoInversion','tipoInversion','bindex']
admin.site.register(movimiento, movimientoAdmin)

class saldoActualizado(models.Model):
    cliente = models.ForeignKey(cliente, on_delete=models.CASCADE)
    tipoInversion = models.ForeignKey(tipoInversion, on_delete=models.CASCADE)
    bindex = models.ForeignKey(bindex, on_delete=models.CASCADE)
    monto = models.IntegerField()
    fecha = models.DateField()


    def variacionDia(obj):
        hoy = obj.fecha
        ayer = hoy - timedelta(days=30)
        qPasado = saldoActualizado.objects.filter(cliente=obj.cliente, fecha=ayer).values('cliente__nombre', 'monto')
        old =0
        for x in qPasado:
            old += x['monto']
        try:
            return ((obj.monto-old)/old)*100
        except ZeroDivisionError:
            return 0


class saldoMensual(models.Model):
    cliente = models.ForeignKey(cliente, on_delete=models.CASCADE)
    tipoInversion = models.ForeignKey(tipoInversion, on_delete=models.CASCADE)
    anio = models.IntegerField()
    mes = models.IntegerField()
    saldoCierre = models.IntegerField()

    def sumaAnterio(obj):
        periodo_anterior = []
        if obj.mes == 1:
            periodo_anterior = [obj.anio-1, 12]
        else:
            periodo_anterior = [obj.anio, obj.mes-1]
        suma = 0
        query = saldoMensual.objects.filter(anio= periodo_anterior[0], mes= periodo_anterior[1], cliente=obj.cliente)
        for s in query:
            suma= suma + int(s.saldoCierre)
        return suma

    def variacion(obj): #monto saldo final - inicial
        periodo_anterior = []
        if obj.mes == 1:
            periodo_anterior = [obj.anio-1, 12]
        else:
            periodo_anterior = [obj.anio, obj.mes-1]
        try:
            sa = saldoMensual.objects.get(anio= periodo_anterior[0], mes = periodo_anterior[1], tipoInversion= obj.tipoInversion, cliente = obj.cliente)
            return obj.saldoCierre - sa.saldoCierre
        except saldoMensual.DoesNotExist:
            return 0
    def porcentaje_variacion(obj):
        aux = obj.variacion()
        try:
            return aux/obj.saldoCierre
        except ZeroDivisionError:
            return 0

#felipe
class countryExposure(models.Model):
   bindex = models.OneToOneField(bindex, on_delete=models.CASCADE, primary_key =True)
   country_exposure = models.TextField(null=True, blank=True) #como json
   country_exposure_equity = models.TextField(null=True, blank=True) #como json
   country_exposure_bond = models.TextField(null=True, blank=True) #como json
   country_exposure_convertible = models.TextField(null=True, blank=True) #como json

class rentabilidad(models.Model):
    bindex = models.OneToOneField(bindex, on_delete=models.CASCADE, primary_key =True)
    fondo = models.ForeignKey(fondo, on_delete=models.CASCADE, null = True, blank=True)
    #categoria = models.ForeignKey(categoria, on_delete=models.CASCADE)
    DayEndDate = models.DateField(null = True, blank=True)
    DayEndNAV = models.FloatField(null = True, blank=True)
    NAVChange = models.FloatField(null = True, blank=True)
    NAVChangePercentage = models.FloatField(null = True, blank=True)
    Retorno = models.TextField(null=True, blank=True)
    Rank = models.TextField(null=True, blank=True)
    CategoryEndDate= models.DateField(null = True, blank=True)
    CategoryReturn =  models.TextField(null=True, blank=True)
    CategorySize =  models.TextField(null=True, blank=True)
    PricingFrequency= models.CharField(max_length=20, null = True, blank=True)

class reporte_anual_couta(models.Model):
    bindex = models.OneToOneField(bindex, on_delete=models.CASCADE, primary_key =True)
    AnnualReportDate = models.DateField(null = True, blank=True)
    NetExpenseRatio = models.FloatField(null = True, blank=True)
    AnnualReportPerformanceFee = models.FloatField(null = True, blank=True)
    InterimNetExpenseRatioDate = models.DateField(null = True, blank=True)
    InterimNetExpenseRatio = models.FloatField(null = True, blank=True)

class precio_actual(models.Model): #Current Price
    bindex = models.OneToOneField(bindex, on_delete=models.CASCADE, primary_key =True)
    CurrencyISO3 = models.ForeignKey(moneda, on_delete=models.CASCADE, null=True, blank=True)
    DayEndNAVDate = models.DateField(null = True, blank=True)
    DayEndNAV =models.FloatField(null = True, blank=True)
    MonthEndNAVDate = models.DateField(null = True, blank=True)
    MonthEndNAV = models.FloatField(null = True, blank=True)
    UnsplitNAV = models.FloatField(null = True, blank=True)
    NAV52wkHigh = models.FloatField(null = True, blank=True)
    NAV52wkHighDate = models.DateField(null = True, blank=True)
    NAV52wkLow = models.FloatField(null = True, blank=True)
    NAV52wkLowDate = models.DateField(null = True, blank=True)
    PerformanceReturnSource = models.CharField(max_length=20, null = True, blank=True)
