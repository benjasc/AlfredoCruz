from django.db import models

class CategoriaGrupo(models.Model): #broadCategoryGroup
    nombre = models.CharField(max_length=50)
    codigo = models.CharField(max_length=50)

class CategoriaMoneda(models.Model):#CategoryCurrency
    id = models.CharField(max_length=10, primary_key=True)
    codigo = models.CharField(max_length=50)
    nombre = models.CharField(max_length=50)
    CategoriaGrupo = models.ForeignKey('CategoriaGrupo', on_delete=models.CASCADE)

class Domicilio(models.Model):#Domicile
    id = models.CharField(max_length=10, primary_key=True)
    nombre = models.CharField(max_length=50)

class Moneda(models.Model):#Currency
    id = models.CharField(max_length=10, primary_key=True)
    nombre = models.CharField(max_length=50)

class TipoFondo(models.Model):
    id = models.CharField(max_length=10, primary_key=True)
    descripcion = models.CharField(max_length=50)

class Fund(models.Model):#Fund
    id  = models.CharField(max_length=10, primary_key=True)
    nombre = models.CharField(max_length=50)
    nombre_legal = models.CharField(max_length=50)
    fecha_inicio = models.DateField()
    Domicilio = models.ForeignKey('Domicilio', on_delete=models.CASCADE)
    Moneda = models.ForeignKey('Moneda', on_delete=models.CASCADE)
    CategoriaMoneda = models.ForeignKey('CategoriaMoneda', on_delete=models.CASCADE)
    TipoFondo = models.ForeignKey('TipoFondo', on_delete=models.CASCADE)

class EstadoDistribucion(models.Model):#DistributionStatus
    estado = models.CharField(max_length=50)

class FrecuenciaDistribucion(models.Model):#DistributionFrecuency
    frecuencia = models.CharField(max_length=50)

class marca(models.Model): #Branding
    id = models.CharField(max_length=10, primary_key=True)
    nombre = models.CharField(max_length=50)

class Proveedor(models.Model):#ProviderCompany
    id = models.CharField(max_length=10, primary_key=True)
    nombre = models.CharField(max_length=50)

class Rendimiento(models.Model):#Performance
    id = models.CharField(max_length=10, primary_key=True)
    estado = models.IntegerField()

class RentaFija(models.Model):#FixedIncome (excel)
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

class AsignacionActivos(models.Model):#AssetAllocation
    id = models.CharField(max_length=10, primary_key=True)
    red_bono = models.IntegerField()#BondNet
    red_efectivo = models.IntegerField()#CashNet
    red_convertible = models.IntegerField()#ConvertibleNet
    red_preferida = models.IntegerField()#PreferredNet
    red_acciones = models.IntegerField()#PreferredNet
    red_preferida = models.IntegerField()#StockNet
    red_otra = models.IntegerField()#OtherNet
    portafolio_fecha = models.DateField()#portfolioDate


class Sector(models.Model):#AssetAllocation
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

class Morningstar(models.Model):
    id = models.CharField(max_length=10, primary_key=True)
    country_exposure = models.TextField()
    Sector = models.ForeignKey('Sector',on_delete=models.CASCADE)
    AsignacionActivos = models.ForeignKey('AsignacionActivos',on_delete=models.CASCADE)

class Fondo(models.Model):
    id = models.CharField(max_length=10, primary_key=True)
    Marca = models.ForeignKey('Marca', on_delete=models.CASCADE)
    Proveedor = models.ForeignKey('Proveedor', on_delete=models.CASCADE)
    Fund = models.ForeignKey('Fund', on_delete=models.CASCADE)
    EstadoDistribucion = models.ForeignKey('EstadoDistribucion', on_delete=models.CASCADE)
    FrecuenciaDistribucion = models.ForeignKey('FrecuenciaDistribucion', on_delete=models.CASCADE)
    Rendimiento = models.ForeignKey('Rendimiento', on_delete=models.CASCADE)
    RentaFija = models.ForeignKey('RentaFija', on_delete=models.CASCADE)
    Morningstar = models.ForeignKey('Morningstar',on_delete=models.CASCADE)
