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
from anuario.views import login, perfil, index, SaldoInicial, tipoMovimiento, tipoInversion,Instrumento, getProveedor,getFondos,guardarSaldo
from anuario.api.graficos import evolucionPatrimonio,patrimonioConsolidado,totalesConsolidados, cartolasConsolidadas,graficos,resumenMoneda,resumenFondo,resumenBranding,resumenCompletoDia, resumenCuentas,resumenCompletoMes
from anuario.api.pais import apiPaises
from anuario.api.movimiento import apiMovimiento
from anuario.api.tipoInversion import apiTipoInversion
from anuario.api.tipoMovimiento import apiTipoMovimiento
from anuario.api.tipoInstrumento import apiTipoInstrumento
from anuario.api.cliente import apiCliente
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
    path('tipoMovimiento/',tipoMovimiento,name='index'),
    path('tipoInversion/',tipoInversion,name='index'),
    path('Instrumento/',Instrumento,name='index'),
#-------------movimiento-----> SaldoInicial
    path('proveedor/',getProveedor),
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
#-------------FIN API MODELOS

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
