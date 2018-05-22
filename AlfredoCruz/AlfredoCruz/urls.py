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
from anuario.api.graficos import evolucionPatrimonio,patrimonioConsolidado,totalesConsolidados, cartolasConsolidadas,saldoAct
#from django.contrib.auth.views import login



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

#-------------API
    path('api/patrimonioConsolidado/<id>/<date>', patrimonioConsolidado),
    path('api/evolucionPatrimonio/<cliente_id>/',evolucionPatrimonio),
    path('api/evolucionPatrimonio/<cliente_id>/<fecha>',evolucionPatrimonio),
    path('api/totalesConsolidados/<cliente_id>/',totalesConsolidados),
    path('api/totalesConsolidados/<cliente_id>/<fecha>',totalesConsolidados),
    path('api/cartolasConsolidadas/<id>/',cartolasConsolidadas),
    path('api/saldoAct/',saldoAct),
    #path('api/cartolasConsolidadas/<cliente_id>/<fecha>',cartolasConsolidadas),

#-------------FIN API

]
