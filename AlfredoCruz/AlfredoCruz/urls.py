"""AlfredoCruz URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.urls import path
from anuario.views import login, perfil, index, SaldoInicial, tipoMovimiento, tipoInversion,Instrumento,getFondos,guardarSaldo,getCliente, editarCliente, getBranding, getBroadcategory, getPais, editarPais, getDomicilio, editarDomicilio, getMoneda, getTipoInstrumento, editarTipoInstrumento, getFrecuencia, editarFrecuencia, getRendimiento, getProveedor, getTipoInversion, editarTipoInversion, getTipoMovimiento, editarTipoMovimiento, getBindex, editarBindex, getAsignacionActivo, editarAsignacionActivo, getCarteraCliente, editarCarteraCliente, getCategoria, editarCategoria, getFondo, editarFondo, getInstrumento, editarInstrumento, getMovimiento, editarMovimiento, getReporteAnualCouta, editarReporteAnualCouta, getSector, editarSector, getSaldoMensual, editarSaldoMensual, getSaldoActualizado, editarSaldoActualizado
from anuario.api.graficos import evolucionPatrimonio,patrimonioConsolidado,totalesConsolidados, cartolasConsolidadas,graficos,resumenMoneda,resumenFondo,resumenBranding,resumenCompletoDia, resumenCuentas,resumenCompletoMes
from anuario.api.pais import apiPaises
from anuario.api.movimiento import apiMovimiento
from anuario.api.tipoInversion import apiTipoInversion
from anuario.api.tipoMovimiento import apiTipoMovimiento
from anuario.api.tipoInstrumento import apiTipoInstrumento
from anuario.api.cliente import apiCliente
from anuario.api.carteraCliente import apiCarteraCliente
from anuario.api.saldoActualizado import apiSaldoActualizado
from anuario.api.saldoMensual import apiSaldoMensual
from anuario.api.asignacionActivo import apiAsignacionActivo
from anuario.api.bindex import apiBindex
from anuario.api.branding import apiBranding
from anuario.api.broadCategory import apiBroadCategory
from anuario.api.categoria import apiCategoria
from anuario.api.countryExposure import apiCountryExposure
from anuario.api.domicilio import apiDomicilio
from anuario.api.fondo import apiFondo
from anuario.api.frecuenciaDistribucion import apiFrecuenciaDistribucion
from anuario.api.instrumento import apiInstrumento
from anuario.api.moneda import apiMoneda
from anuario.api.precioActual import apiPrecioActual
from anuario.api.proveedor import apiProveedor
from anuario.api.rendimiento import apiRendimiento
from anuario.api.rentaFija import apiRentaFija
from anuario.api.reporteAnualCuota import apiReporteAnualCuota
from anuario.api.sector import apiSector









#from django.contrib.auth.views import login
#import felipe
from anuario.view.morningstar import country_exposure, global_sector, asset_allocation, daily_performance, anual_report_fees, current_price, fund_info
from anuario.view.datos import importar_datos



urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/',login, name='login' ),
    path('perfil/',perfil, name='perfil' ),
    path('index/',index,name='index'),

    path('SaldoInicial/',SaldoInicial,name='index'),
    #path('tipoMovimiento/',tipoMovimiento,name='index'),
    #path('tipoInversion/',tipoInversion,name='index'),
    #path('Instrumento/',Instrumento,name='index'),
#-------------movimiento-----> SaldoInicial
    #path('proveedor/',getProveedor),
    path('fondos/',getFondos),
    path('guardarSaldo/',guardarSaldo),
#-------------FinSaldoInicial

#-------------API graficos

    path('api/patrimonioConsolidado/<id>/<fecha>', patrimonioConsolidado),
    path('api/patrimonioConsolidado/<id>', patrimonioConsolidado),
    path('api/evolucionPatrimonio/<id>/',evolucionPatrimonio),
    path('api/evolucionPatrimonio/<id>/<fecha>',evolucionPatrimonio),
    path('api/totalesConsolidados/<id>/',totalesConsolidados),
    path('api/totalesConsolidados/<id>/<fecha>',totalesConsolidados),
    path('api/cartolasConsolidadas/<id>/',cartolasConsolidadas),
    path('api/cartolasConsolidadas/<id>/<fecha>',cartolasConsolidadas),
    path('api/resumenCuentas/<id>/<fecha>',resumenCuentas),
    path('api/resumenCuentas/<id>/',resumenCuentas),
    #path('api/saldoAct/',saldoAct),
    path('api/resumenMoneda/<id>/',resumenMoneda),
    path('api/resumenFondo/<id>/',resumenFondo),
    path('api/resumenBranding/<id>/',resumenBranding),
    path('api/resumenCompletoDia/<id>/',resumenCompletoDia),
    path('api/resumenCompletoMes/<id>/',resumenCompletoMes),
    path('api/graficos/<id>/',graficos),
    path('api/graficos/<id>/<fecha>',graficos),

#-------------FIN API
#-------------API MODELOS
    path('api/pais/',apiPaises),
    path('api/pais/<id>/',apiPaises),
    path('api/movimiento/',apiMovimiento),
    path('api/movimiento/<id>/',apiMovimiento),
    path('api/tipo_inversion/',apiTipoInversion),
    path('api/tipo_inversion/<id>/',apiTipoInversion),
    path('api/tipo_movimiento/',apiTipoMovimiento),
    path('api/tipo_movimiento/<id>/',apiTipoMovimiento),
    path('api/tipo_instrumento/',apiTipoInstrumento),
    path('api/tipo_instrumento/<id>/',apiTipoInstrumento),
    path('api/cliente/',apiCliente),
    path('api/cliente/<id>/',apiCliente),
    path('api/cartera_cliente/',apiCarteraCliente),
    path('api/cartera_cliente/<id>/',apiCarteraCliente),
    path('api/saldo_actualizado/',apiSaldoActualizado),
    path('api/saldo_actualizado/<id>/',apiSaldoActualizado),
    path('api/saldo_mensual/',apiSaldoMensual),
    path('api/saldo_mensual/<id>/',apiSaldoMensual),
    path('api/asignacion_activo/',apiAsignacionActivo),
    path('api/asignacion_activo/<id>/',apiAsignacionActivo),
    path('api/bindex/',apiBindex),
    path('api/bindex/<id>/',apiBindex),
    path('api/branding/',apiBranding),
    path('api/branding/<id>/',apiBranding),
    path('api/broadCategory/',apiBroadCategory),
    path('api/broadCategory/<id>/',apiBroadCategory),
    path('api/categoria/',apiCategoria),
    path('api/categoria/<id>/',apiCategoria),
    path('api/country_exposure/',apiCountryExposure),
    path('api/country_exposure/<id>/',apiCountryExposure),
    path('api/domicilio/',apiDomicilio),
    path('api/domicilio/<id>/',apiDomicilio),
    path('api/fondo/',apiFondo),
    path('api/fondo/<id>/',apiFondo),
    path('api/frecuencia_distribucion/',apiFrecuenciaDistribucion),
    path('api/frecuencia_distribucion/<id>/',apiFrecuenciaDistribucion),
    path('api/instrumento/',apiInstrumento),
    path('api/instrumento/<id>/',apiInstrumento),
    path('api/moneda/',apiMoneda),
    path('api/moneda/<id>/',apiMoneda),
    path('api/precio_actual/',apiPrecioActual),
    path('api/precio_actual/<id>/',apiPrecioActual),
    path('api/proveedor/',apiProveedor),
    path('api/proveedor/<id>/',apiProveedor),
    path('api/rendimiento/',apiRendimiento),
    path('api/rendimiento/<id>/',apiRendimiento),
    path('api/renta_fija/',apiRentaFija),
    path('api/renta_fija/<id>/',apiRentaFija),
    path('api/reporte_anual_cuota/',apiReporteAnualCuota),
    path('api/reporte_anual_cuota/<id>/',apiReporteAnualCuota),
    path('api/sector/',apiSector),
    path('api/sector/<id>/',apiSector),

#-------------FIN API MODELOS
#-------------CRUD's
#-------------CRUD
    path('cliente/',getCliente),
    path('cliente/editar/<id>', editarCliente),
    path('cliente/editar/', editarCliente),

    path('bindex/',getBindex),
    path('bindex/editar/<id>',editarBindex),
    path('bindex/editar/',editarBindex),

    path('branding/',getBranding),

    path('broadcategory/',getBroadcategory),

    path('carteraCliente/',getCarteraCliente),
    path('carteraCliente/editar/<id>',editarCarteraCliente),
    path('carteraCliente/editar/',editarCarteraCliente),

    path('categoria/',getCategoria),
    path('categoria/editar/<id>',editarCategoria),
    path('categoria/editar/',editarCategoria),

    path('pais/',getPais),
    path('pais/editar/<id>',editarPais),
    path('pais/editar/',editarPais),

    path('proveedor/',getProveedor),

    path('domicilio/',getDomicilio),
    path('domicilio/editar/<id>',editarDomicilio),
    path('domicilio/editar/',editarDomicilio),

    path('fondo/',getFondo),
    path('fondo/editar/<id>',editarFondo),
    path('fondo/editar/',editarFondo),

    path('moneda/',getMoneda),

    path('movimiento/',getMovimiento),
    path('movimiento/editar/<id>',editarMovimiento),
    path('movimiento/editar/',editarMovimiento),

    path('frecuencia/',getFrecuencia),
    path('frecuencia/editar/<id>',editarFrecuencia),
    path('frecuencia/editar/',editarFrecuencia),

    path('instrumento/',getInstrumento),
    path('instrumento/editar/<id>',editarInstrumento),
    path('instrumento/editar/',editarInstrumento),

    path('rendimiento/',getRendimiento),

    #reporteAnualCouta
    path('reporteAnualCouta/',getReporteAnualCouta),
    path('reporteAnualCouta/editar/<id>',editarReporteAnualCouta),
    path('reporteAnualCouta/editar/',editarReporteAnualCouta),

    path('saldoActualizado/',getSaldoActualizado),
    path('saldoActualizado/editar/<id>',editarSaldoActualizado),
    path('saldoActualizado/editar/',editarSaldoActualizado),

    path('saldoMensual/',getSaldoMensual),
    path('saldoMensual/editar/<id>',editarSaldoMensual),
    path('saldoMensual/editar/',editarSaldoMensual),

    path('tipoInstrumento/',getTipoInstrumento),
    path('tipoInstrumento/editar/<id>',editarTipoInstrumento),
    path('tipoInstrumento/editar/',editarTipoInstrumento),

    path('tipoInversion/',getTipoInversion),
    path('tipoInversion/editar/<id>',editarTipoInversion),
    path('tipoInversion/editar/',editarTipoInversion),

    path('tipoMovimiento/',getTipoMovimiento),
    path('tipoMovimiento/editar/<id>',editarTipoMovimiento),
    path('tipoMovimiento/editar/',editarTipoMovimiento),

    path('asignacionActivo/',getAsignacionActivo),
    path('asignacionActivo/editar/<id>',editarAsignacionActivo),
    path('asignacionActivo/editar/',editarAsignacionActivo),

    path('sector/',getSector),
    path('sector/editar/<id>',editarSector),
    path('sector/editar/',editarSector),
#-------------FinCrud





#-------------FIN CRUD's


#-------------API XML
    path('xml/country_exposure/', country_exposure),
    path('xml/global_sector/', global_sector),
    path('xml/asset_allocation/', asset_allocation),
    path('xml/daily_performance/', daily_performance),
    path('xml/anual_report_fees/', anual_report_fees),
    path('xml/current_price/', current_price),
    path('xml/fund_info/', fund_info),#1

    path('perfil/datos/importar/', importar_datos),



]
