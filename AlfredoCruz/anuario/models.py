from django.contrib import admin
from django.db import models
'''
# class morningstar(models.Model):
#     id = models.CharField(max_length=15, primary_key=True)
#     country_exposure = models.TextField() #como json
# class morningstarAdmin(admin.ModelAdmin):
#     list_display = ['country_exposure']
#     search_fields = ['country_exposure']
# admin.site.register(morningstar, morningstarAdmin)'''

class bindex(models.Model):
    country_exposure = models.TextField() #como json
class bindexAdmin(admin.ModelAdmin):
    list_display = ['id']
    search_fields = ['id']
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
    codigo = models.CharField(max_length=50)
    broadCategory = models.ForeignKey(broadCategory, on_delete=models.CASCADE)
    moneda = models.ForeignKey(moneda, on_delete=models.CASCADE)
class categoriaAdmin(admin.ModelAdmin):
    list_display = ['nombre','codigo','broadCategory','moneda']
    search_fields = ['nombre','codigo','broadCategory','moneda']
admin.site.register(categoria, categoriaAdmin)

class domicilio(models.Model):#Domicile
    id = models.CharField(max_length=15, primary_key=True)
    nombre = models.CharField(max_length=50)
class domicilioAdmin(admin.ModelAdmin):
    list_display = ['id','nombre']
    search_fields = ['id','nombre']
admin.site.register(domicilio, domicilioAdmin)

class tipoInstrumento(models.Model):
    id = models.CharField(max_length=15, primary_key=True)
    estructura_legal = models.CharField(max_length=50)
    estado_distribucion = models.CharField(max_length=50)
    def __str__(self):
        return self.estado_distribucion+' -- '+self.estructura_legal

class tipoInstrumentoAdmin(admin.ModelAdmin):
    list_display = ['estructura_legal','estado_distribucion']
    search_fields = ['estructura_legal','estado_distribucion']
admin.site.register(tipoInstrumento, tipoInstrumentoAdmin)

class proveedor(models.Model):#ProviderCompany
    id = models.CharField(max_length=10, primary_key=True)
    datos = models.TextField() #como json
class proveedorAdmin(admin.ModelAdmin):
    list_display = ['datos']
    search_fields = ['datos']
admin.site.register(proveedor, proveedorAdmin)

class fondo(models.Model):
    id = models.CharField(max_length=15, primary_key=True)
    nombre = models.CharField(max_length=50)
    nombre_legal = models.CharField(max_length=50)
    fecha_inicio = models.DateField()
    domicilio = models.ForeignKey(domicilio, on_delete=models.CASCADE)
    categoria = models.ForeignKey(categoria, on_delete=models.CASCADE)
    moneda = models.ForeignKey(moneda, on_delete=models.CASCADE)

class fondoAdmin(admin.ModelAdmin):
    list_display = ['nombre','nombre_legal','fecha_inicio','domicilio','categoria','moneda']#definir cuales se necesitan
    search_fields = ['nombre','nombre_legal','fecha_inicio','domicilio','categoria','moneda']#definir cuales se necesitan
admin.site.register(fondo, fondoAdmin)
#fondo quien contiene a otras tablas va como fk en instrumento, ahora proseguimos
#haciendo mas tablas que van como fk en instrumento, pero la mayoria de estas no contiene otras tablas
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
class paisAdmin(admin.ModelAdmin):
    list_display = ['nombre']
    search_fields = ['nombre']
admin.site.register(pais, paisAdmin)

class instrumento(models.Model):
    bindex = models.OneToOneField(bindex,on_delete=models.CASCADE, primary_key=True)
    run_svs = models.CharField(max_length=50)
    clase_proveedor = models.CharField(max_length=50)
    operation_ready = models.IntegerField()
    branding = models.ForeignKey(branding, on_delete=models.CASCADE)
    frecuenciaDistribucion = models.ForeignKey(frecuenciaDistribucion, on_delete=models.CASCADE)
    rendimiento = models.ForeignKey(rendimiento, on_delete=models.CASCADE) #Performance
    proveedor = models.ForeignKey(proveedor, on_delete=models.CASCADE)
    tipoInstrumento = models.ForeignKey(tipoInstrumento, on_delete=models.CASCADE)
    fondo = models.ForeignKey(fondo, on_delete=models.CASCADE)

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
    materiales_basicos = models.FloatField() #BasicMaterials
    servicio_comunicacion = models.FloatField()#CommunicationService
    ciclico_consumidor = models.FloatField()#consumercyclical
    defensa_consumidor = models.FloatField() #consumerDefensive
    energia = models.FloatField() #Energy
    servicios_financieros = models.FloatField() #FinancialServices
    cuidado_salud = models.FloatField()#HealthCare
    acciones_industriales = models.FloatField()#industrials
    bienes_raices = models.FloatField()#RealEstate
    tecnologia = models.FloatField()#Technology
    utilidades = models.FloatField()#Utilities
    portafolio_fecha = models.DateField()
class sectorAdmin(admin.ModelAdmin):
    list_display = ['materiales_basicos','servicio_comunicacion','ciclico_consumidor']#definir que atributos se ocuparan
    search_fields = ['materiales_basicos','servicio_comunicacion','ciclico_consumidor']#definir que atributos se ocuparan
admin.site.register(sector, sectorAdmin)

class asignacionActivo(models.Model):#AssetAllocation
    bindex = models.OneToOneField(bindex,on_delete=models.CASCADE, primary_key=True)
    red_bono = models.FloatField()#BondNet
    red_efectivo = models.FloatField()#CashNet
    red_convertible = models.FloatField()#ConvertibleNet
    red_preferida = models.FloatField()#PreferredNet #2veces
    red_acciones = models.FloatField()#PreferredNet
    red_otra = models.FloatField()#OtherNet
    portafolio_fecha = models.DateField()#portfolioDate
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
    tipoInversion = models.ForeignKey(tipoInversion, on_delete=models.CASCADE)
class clienteAdmin(admin.ModelAdmin):
    list_display = ['id','nombre','tipoInversion']
    search_fields = ['id','nombre','tipoInversion']
admin.site.register(cliente, clienteAdmin)

class carteraCliente(models.Model):
    fecha = models.DateField()
    saldo = models.IntegerField()
    tipoInversion = models.ForeignKey(tipoInversion, on_delete=models.CASCADE)
    cliente = models.ForeignKey(cliente, on_delete=models.CASCADE)
    bindex = models.ForeignKey(bindex, on_delete=models.CASCADE)
class carteraClienteAdmin(admin.ModelAdmin):
    list_display = ['id','saldo','tipoInversion','cliente','bindex']
    search_fields = ['id','saldo','tipoInversion','cliente','bindex']
admin.site.register(carteraCliente, carteraClienteAdmin)

class movimiento(models.Model):
    monto = models.IntegerField()
    fecha = models.DateField()
    numero_cuotas =  models.IntegerField()
    cliente = models.ForeignKey(cliente, on_delete=models.CASCADE)
    tipoInversion = models.ForeignKey(tipoInversion, on_delete=models.CASCADE)
    tipoMovimiento = models.ForeignKey(tipoMovimiento, default=1, on_delete=models.CASCADE)
    bindex = models.ForeignKey(bindex, on_delete=models.CASCADE)
class movimientoAdmin(admin.ModelAdmin):
    list_display = ['id','monto','fecha','numero_cuotas','cliente','tipoInversion','tipoInversion','bindex']
    search_fields = ['id','monto','fecha','numero_cuotas','cliente','tipoInversion','tipoInversion','bindex']
admin.site.register(movimiento, movimientoAdmin)
