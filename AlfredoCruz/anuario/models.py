from django.contrib import admin
from django.db import models
#definimos las dos tablas mas importantes, morningstar y bindex
class morningstar(models.Model):
    id = models.CharField(max_length=15, primary_key=True)
    country_exposure = models.TextField() #como json
class morningstarAdmin(admin.ModelAdmin):
    list_display = ['country_exposure']
    search_fields = ['country_exposure']
admin.site.register(morningstar, morningstarAdmin)

class bindex(models.Model):
    id = models.AutoField(primary_key=True)
    morningstar = models.ForeignKey(morningstar, on_delete=models.CASCADE)
class bindexAdmin(admin.ModelAdmin):
    list_display = ['id','morningstar']
    search_fields = ['id','morningstar']
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
class tipoInstrumentoAdmin(admin.ModelAdmin):
    list_display = ['estructura_legal','estado_distribucion']
    search_fields = ['estructura_legal','estado_distribucion']
admin.site.register(tipoInstrumento, tipoInstrumentoAdmin)

class fondo(models.Model):
    id = models.CharField(max_length=15, primary_key=True)
    nombre = models.CharField(max_length=50)
    nombre_legal = models.CharField(max_length=50)
    fecha_inicio = models.CharField(max_length=50)
    domicilio = models.ForeignKey(domicilio, on_delete=models.CASCADE)
    categoria = models.ForeignKey(categoria, on_delete=models.CASCADE)
    moneda = models.ForeignKey(moneda, on_delete=models.CASCADE)
    tipoInstrumento = models.ForeignKey(tipoInstrumento, on_delete=models.CASCADE)
class fondoAdmin(admin.ModelAdmin):
    list_display = ['nombre','nombre_legal','fecha_inicio','domicilio','categoria','moneda','tipoInstrumento']#definir cuales se necesitan
    search_fields = ['nombre','nombre_legal','fecha_inicio','domicilio','categoria','moneda','tipoInstrumento']#definir cuales se necesitan
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

class proveedor(models.Model):#ProviderCompany
    id = models.CharField(max_length=10, primary_key=True)
    json = models.TextField()
class proveedorAdmin(admin.ModelAdmin):
    list_display = ['json']
    search_fields = ['json']
admin.site.register(proveedor, proveedorAdmin)

class pais(models.Model):
    id = models.CharField(max_length=10, primary_key=True)
    nombre = models.IntegerField()
class paisAdmin(admin.ModelAdmin):
    list_display = ['nombre']
    search_fields = ['nombre']
admin.site.register(pais, paisAdmin)

class instrumento(models.Model):
    bindex = models.OneToOneField(bindex,on_delete=models.CASCADE, primary_key=True)
    fondo = models.ForeignKey(fondo, on_delete=models.CASCADE)
    proveedor = models.ForeignKey(proveedor, on_delete=models.CASCADE)
    branding = models.ForeignKey(branding, on_delete=models.CASCADE)
    frecuenciaDistribucion = models.ForeignKey(frecuenciaDistribucion, on_delete=models.CASCADE)
    rendimiento = models.ForeignKey(rendimiento, on_delete=models.CASCADE) #Performance
    run_svs = models.CharField(max_length=50)
    clase_proveedor = models.CharField(max_length=50)
    operation_ready = models.BooleanField()
class instrumentoAdmin(admin.ModelAdmin):
    list_display = ['bindex','fondo','proveedor','branding','frecuenciaDistribucion','rendimiento',
    'run_svs','clase_proveedor','operation_ready']
    search_fields = ['bindex','fondo','proveedor','branding','frecuenciaDistribucion','rendimiento',
    'run_svs','clase_proveedor','operation_ready']
admin.site.register(instrumento,instrumentoAdmin)

class rentaFija(models.Model):#FixedIncome (excel)
    bindex = models.OneToOneField(bindex,on_delete=models.CASCADE, primary_key=True)
    bsed = models.BooleanField()#BondStatisticsEffectiveDuration
    bsem = models.BooleanField()#BondStatisticsEffectiveMaturity
    bsmd = models.BooleanField()#BondStatisticsModifiedDuration
    bsym = models.BooleanField()#BondStatisticsYieldToMaturity
    cred = models.BooleanField()#CoverageRatioEffectiveDuration
    crem = models.BooleanField()#CoverageRatioEffectiveMaturity
    crmd = models.BooleanField()#CoverageRatioModifiedDuration
    crym = models.BooleanField()#CoverageRatioYieldToMaturity
    portafolio_fecha = models.DateField()
class rentaFijaAdmin(admin.ModelAdmin):
    list_display = ['bsed','bsem','bsmd','bsym','cred','crem','crmd','crym','portafolio_fecha']
    search_fields = ['bsed','bsem','bsmd','bsym','cred','crem','crmd','crym','portafolio_fecha']
admin.site.register(rentaFija, rentaFijaAdmin)

class sector(models.Model):#SectorExposure
    bindex = models.OneToOneField(bindex,on_delete=models.CASCADE,primary_key=True)
    materiales_basicos =  models.BooleanField()#BasicMaterials
    servicio_comunicacion = models.BooleanField()#CommunicationService
    ciclico_consumidor = models.BooleanField()#consumercyclical
    defensa_consumidor = models.BooleanField()#consumerDefensive
    energia = models.BooleanField()#Energy
    servicios_financieros = models.BooleanField()#FinancialServices
    cuidado_salud = models.BooleanField()#HealthCare
    acciones_industriales = models.BooleanField()#industrials
    bienes_raices = models.BooleanField()#RealEstate
    tecnologia = models.BooleanField()#Technology
    utilidades = models.BooleanField()#Utilities
    portafolio_fecha = models.DateField()
class sectorAdmin(admin.ModelAdmin):
    list_display = ['materiales_basicos','servicio_comunicacion','ciclico_consumidor']#definir que atributos se ocuparan
    search_fields = ['materiales_basicos','servicio_comunicacion','ciclico_consumidor']#definir que atributos se ocuparan
admin.site.register(sector, sectorAdmin)

class asignacionActivo(models.Model):#AssetAllocation
    bindex = models.OneToOneField(bindex,on_delete=models.CASCADE, primary_key=True)
    red_bono = models.BooleanField()#BondNet
    red_efectivo = models.BooleanField()#CashNet
    red_convertible = models.BooleanField()#ConvertibleNet
    red_preferida = models.BooleanField()#PreferredNet #2veces
    red_acciones = models.BooleanField()#PreferredNet
    red_otra = models.BooleanField()#OtherNet
    portafolio_fecha = models.DateField()#portfolioDate
class asignacionActivoAdmin(admin.ModelAdmin):
    list_display = ['red_bono','red_efectivo','red_convertible','red_preferida','red_acciones','red_otra','portafolio_fecha']
    search_fields = ['red_bono','red_efectivo','red_convertible','red_preferida','red_acciones','red_otra','portafolio_fecha']
admin.site.register(asignacionActivo, asignacionActivoAdmin)

class valorCuota(models.Model):
    bindex = models.OneToOneField(bindex,on_delete=models.CASCADE,primary_key=True)
    anio = models.CharField(max_length=50)
    json = models.TextField()
class valorCuotaAdmin(admin.ModelAdmin):
    list_display = ['bindex','anio','json']
    search_fields = ['bindex','anio','json']
admin.site.register(valorCuota, valorCuotaAdmin)

class claseActivo(models.Model):
    bindex = models.OneToOneField(bindex,on_delete=models.CASCADE,primary_key=True)
    json = models.TextField()
class claseActivoAdmin(admin.ModelAdmin):
    list_display = ['bindex','json']
    search_fields = ['bindex','json']
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
    saldo =  models.BooleanField()
    tipoInversion = models.ForeignKey(tipoInversion, on_delete=models.CASCADE)
    cliente = models.ForeignKey(cliente, on_delete=models.CASCADE)
    bindex = models.ForeignKey(bindex, on_delete=models.CASCADE)
class carteraClienteAdmin(admin.ModelAdmin):
    list_display = ['id','saldo','tipoInversion','cliente','bindex']
    search_fields = ['id','saldo','tipoInversion','cliente','bindex']
admin.site.register(carteraCliente, carteraClienteAdmin)

class saldoInicial(models.Model):
    saldo = models.BooleanField()
    fecha = models.CharField(max_length=50)
    numero_cuotas =  models.BooleanField()
    cliente = models.ForeignKey(cliente, on_delete=models.CASCADE)
    tipoInversion = models.ForeignKey(tipoInversion, on_delete=models.CASCADE)
    bindex = models.ForeignKey(bindex, on_delete=models.CASCADE)
class saldoInicialAdmin(admin.ModelAdmin):
    list_display = ['id','fecha','numero_cuotas','cliente','tipoInversion','bindex']
    search_fields = ['id','fecha','numero_cuotas','cliente','tipoInversion','bindex']
admin.site.register(saldoInicial, saldoInicialAdmin)

class movimiento(models.Model):
    fecha = models.CharField(max_length=50)
    numero_cuotas =  models.BooleanField()
    cliente = models.ForeignKey(cliente, on_delete=models.CASCADE)
    tipoInversion = models.ForeignKey(tipoInversion, on_delete=models.CASCADE)
    tipoMovimiento = models.ForeignKey(tipoMovimiento, on_delete=models.CASCADE)
    bindex = models.ForeignKey(bindex, on_delete=models.CASCADE)
class movimientoAdmin(admin.ModelAdmin):
    list_display = ['id','fecha','numero_cuotas','cliente','tipoInversion','tipoInversion','bindex']
    search_fields = ['id','fecha','numero_cuotas','cliente','tipoInversion','tipoInversion','bindex']
admin.site.register(movimiento, movimientoAdmin)
