from django.contrib import admin
from django.db import models


class categoriaGrupo(models.Model): #broadCategoryGroup
    nombre = models.CharField(max_length=50)
    codigo = models.CharField(max_length=50)
class categoriaGrupoAdmin(admin.ModelAdmin):
    list_display = ['nombre','codigo']
    search_fields = ['nombre','codigo']
admin.site.register(categoriaGrupo, categoriaGrupoAdmin)

class categoriaMoneda(models.Model):#CategoryCurrency
    id = models.CharField(max_length=10, primary_key=True)
    codigo = models.CharField(max_length=50)
    nombre = models.CharField(max_length=50)
    categoriaGrupo = models.ForeignKey(categoriaGrupo, on_delete=models.CASCADE)
class categoriaMonedaAdmin(admin.ModelAdmin):
    list_display = ['codigo','nombre','categoriaGrupo']
    search_fields = ['codigo','nombre','categoriaGrupo']
admin.site.register(categoriaMoneda, categoriaMonedaAdmin)

class domicilio(models.Model):#Domicile
    id = models.CharField(max_length=10, primary_key=True)
    nombre = models.CharField(max_length=50)
class domicilioAdmin(admin.ModelAdmin):
    list_display = ['id','nombre']
    search_fields = ['id','nombre']
admin.site.register(domicilio, domicilioAdmin)

class moneda(models.Model):#Currency
    id = models.CharField(max_length=10, primary_key=True)
    nombre = models.CharField(max_length=50)
class monedaAdmin(admin.ModelAdmin):
    list_display = ['nombre']
    search_fields = ['nombre']
admin.site.register(moneda, monedaAdmin)

class tipoFondo(models.Model):
    id = models.CharField(max_length=10, primary_key=True)
    descripcion = models.CharField(max_length=50)
class tipoFondoAdmin(admin.ModelAdmin):
    list_display = ['descripcion']
    search_fields = ['descripcion']
admin.site.register(tipoFondo, tipoFondoAdmin)

class fund(models.Model):#Fund
    id  = models.CharField(max_length=10, primary_key=True)
    nombre = models.CharField(max_length=50)
    nombre_legal = models.CharField(max_length=50)
    fecha_inicio = models.DateField()
    domicilio = models.ForeignKey(domicilio, on_delete=models.CASCADE)
    moneda = models.ForeignKey(moneda, on_delete=models.CASCADE)
    categoriaMoneda = models.ForeignKey(categoriaMoneda, on_delete=models.CASCADE)
    tipoFondo = models.ForeignKey(tipoFondo, on_delete=models.CASCADE)
class fundAdmin(admin.ModelAdmin):
    list_display = ['nombre','nombre_legal','fecha_inicio','domicilio','moneda','categoriaMoneda','tipoFondo']
    search_fields = ['nombre','nombre_legal','fecha_inicio','domicilio','moneda','categoriaMoneda','tipoFondo']
admin.site.register(fund, fundAdmin)

class estadoDistribucion(models.Model):#DistributionStatus
    estado = models.CharField(max_length=50)
class estadoDistribucionAdmin(admin.ModelAdmin):
    list_display = ['estado']
    search_fields = ['estado']
admin.site.register(estadoDistribucion, estadoDistribucionAdmin)

class frecuenciaDistribucion(models.Model):#DistributionFrecuency
    frecuencia = models.CharField(max_length=50)
class frecuenciaDistribucionAdmin(admin.ModelAdmin):
    list_display = ['frecuencia']
    search_fields = ['frecuencia']
admin.site.register(frecuenciaDistribucion, frecuenciaDistribucionAdmin)

class marca(models.Model): #Branding
    id = models.CharField(max_length=10, primary_key=True)
    nombre = models.CharField(max_length=50)
class marcaAdmin(admin.ModelAdmin):
    list_display = ['nombre']
    search_fields = ['nombre']
admin.site.register(marca, marcaAdmin)

class proveedor(models.Model):#ProviderCompany
    id = models.CharField(max_length=10, primary_key=True)
    nombre = models.CharField(max_length=50)
class proveedorAdmin(admin.ModelAdmin):
    list_display = ['nombre']
    search_fields = ['nombre']
admin.site.register(proveedor, proveedorAdmin)

class rendimiento(models.Model):#Performance
    id = models.CharField(max_length=10, primary_key=True)
    estado = models.IntegerField()
class rendimientoAdmin(admin.ModelAdmin):
    list_display = ['estado']
    search_fields = ['estado']
admin.site.register(rendimiento, rendimientoAdmin)

class rentaFija(models.Model):#FixedIncome (excel)
    id = models.CharField(max_length=10, primary_key=True)
    descripcion = models.CharField(max_length=50)
    bsed = models.IntegerField()#BondStatisticsEffectiveDuration
    bsem = models.IntegerField()#BondStatisticsEffectiveMaturity
    bsmd = models.IntegerField()#BondStatisticsModifiedDuration
    bsym = models.IntegerField()#BondStatisticsYieldToMaturity
    cred = models.IntegerField()#CoverageRatioEffectiveDuration
    crem = models.IntegerField()#CoverageRatioEffectiveMaturity
    crmd = models.IntegerField()#CoverageRatioModifiedDuration
    crym = models.IntegerField()#CoverageRatioYieldToMaturity
    portafolio_fecha = models.DateField()
class rentaFijaAdmin(admin.ModelAdmin):
    list_display = ['descripcion','bsed','bsem','bsmd','bsym','cred','crem','crmd','crym','portafolio_fecha']
    search_fields = ['descripcion','bsed','bsem','bsmd','bsym','cred','crem','crmd','crym','portafolio_fecha']
admin.site.register(rentaFija, rentaFijaAdmin)

class asignacionActivo(models.Model):#AssetAllocation
    id = models.CharField(max_length=10, primary_key=True)
    red_bono = models.IntegerField()#BondNet
    red_efectivo = models.IntegerField()#CashNet
    red_convertible = models.IntegerField()#ConvertibleNet
    red_preferida = models.IntegerField()#PreferredNet #2veces
    red_acciones = models.IntegerField()#PreferredNet
    red_otra = models.IntegerField()#OtherNet
    portafolio_fecha = models.DateField()#portfolioDate
class asignacionActivoAdmin(admin.ModelAdmin):
    list_display = ['red_bono','red_efectivo','red_convertible','red_preferida','red_acciones','red_otra','portafolio_fecha']
    search_fields = ['red_bono','red_efectivo','red_convertible','red_preferida','red_acciones','red_otra','portafolio_fecha']
admin.site.register(asignacionActivo, asignacionActivoAdmin)


class sector(models.Model):#AssetAllocation
    id = models.CharField(max_length=10, primary_key=True)
    materiales_basicos =  models.IntegerField()#BasicMaterials
    servicio_comunicacion = models.IntegerField()#CommunicationService
    ciclico_consumidor = models.IntegerField()#consumercyclical
    defensa_consumidor = models.IntegerField()#consumerDefensive
    energia = models.IntegerField()#Energy
    servicios_financieros = models.IntegerField()#FinancialServices
    cuidado_salud = models.IntegerField()#HealthCare
    acciones_industriales = models.IntegerField()#industrials
    portafolio_fecha = models.DateField()
    bienes_raices = models.IntegerField()#RealEstate
    tecnologia = models.IntegerField()#Technology
    utilidades = models.IntegerField()#Utilities
class sectorAdmin(admin.ModelAdmin):
    list_display = ['materiales_basicos','servicio_comunicacion','ciclico_consumidor']#definir que atributos se ocuparan
    search_fields = ['materiales_basicos','servicio_comunicacion','ciclico_consumidor']#definir que atributos se ocuparan
admin.site.register(sector, sectorAdmin)

class morningstar(models.Model):
    id = models.CharField(max_length=10, primary_key=True)
    country_exposure = models.TextField()
    sector = models.ForeignKey(sector,on_delete=models.CASCADE)
    asignacionActivo = models.ForeignKey(asignacionActivo,on_delete=models.CASCADE)
class morningstarAdmin(admin.ModelAdmin):
    list_display = ['country_exposure','sector']
    search_fields = ['country_exposure','sector']
admin.site.register(morningstar, morningstarAdmin)

class fondo(models.Model):
    id = models.CharField(max_length=10, primary_key=True)
    marca = models.ForeignKey(marca, on_delete=models.CASCADE)
    proveedor = models.ForeignKey(proveedor, on_delete=models.CASCADE)
    fund = models.ForeignKey(fund, on_delete=models.CASCADE)
    estadoDistribucion = models.ForeignKey(estadoDistribucion, on_delete=models.CASCADE)
    frecuenciaDistribucion = models.ForeignKey(frecuenciaDistribucion, on_delete=models.CASCADE)
    rendimiento = models.ForeignKey(rendimiento, on_delete=models.CASCADE)
    rentaFija = models.ForeignKey(rentaFija, on_delete=models.CASCADE)
    morningstar = models.ForeignKey(morningstar,on_delete=models.CASCADE)
class fondoAdmin(admin.ModelAdmin):
    list_display = ['marca','proveedor','fund','estadoDistribucion','frecuenciaDistribucion']#definir cuales se necesitan
    search_fields = ['marca','proveedor','fund','estadoDistribucion','frecuenciaDistribucion']#definir cuales se necesitan
admin.site.register(fondo, fondoAdmin)

class pais(models.Model):#Performance
    id = models.CharField(max_length=10, primary_key=True)
    nombre = models.IntegerField()
class paisAdmin(admin.ModelAdmin):
    list_display = ['nombre']
    search_fields = ['nombre']
admin.site.register(pais, paisAdmin)
