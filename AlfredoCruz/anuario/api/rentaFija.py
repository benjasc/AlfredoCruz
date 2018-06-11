import json
from django.conf.urls import url, include
from anuario.models import countryExposure,fondo,instrumento,bindex,precio_actual,moneda
from rest_framework.decorators import api_view
from django.http import HttpResponse

@api_view(['GET','POST','PUT'])
def apiRentaFija(request,id=None):
	if request.method == 'GET':
		if id is not None:
			try:
				lista=[]
				query =precio_actual.objects.values('bsed','bsem','bsmd','bsym','cred','UnsplitNAV','NAV52wkHigh','NAV52wkHighDate','NAV52wkLow','NAV52wkLowDate','PerformanceReturnSource').get(pk=id)
				lista.append({
					'DayEndNAVDate':str(query['DayEndNAVDate']),
					'DayEndNAV':query['DayEndNAV'],
					'MonthEndNAVDate':str(query['MonthEndNAVDate']),
					'MonthEndNAV':query['MonthEndNAV'],
					'UnsplitNAV':query['UnsplitNAV'],
					'NAV52wkHigh':query['NAV52wkHigh'],
					'NAV52wkHighDate':str(query['NAV52wkHighDate']),

					'NAV52wkLow':query['NAV52wkLow'],
					'NAV52wkLowDate':str(query['NAV52wkLowDate']),
					'PerformanceReturnSource':query['PerformanceReturnSource'],
					'moneda':query['CurrencyISO3__nombre']
					})
			except precio_actual.DoesNotExist:
				lista = {"mensaje":"No existen datos"}

		else:
			try:
				lista=[]
				query = precio_actual.objects.all().values('CurrencyISO3__nombre','DayEndNAVDate','DayEndNAV','MonthEndNAVDate','MonthEndNAV','UnsplitNAV','NAV52wkHigh','NAV52wkHighDate','NAV52wkLow','NAV52wkLowDate','PerformanceReturnSource')
				if query.count()>0:
					for x in query:
						lista.append({
							'DayEndNAVDate':str(x['DayEndNAVDate']),
							'DayEndNAV':x['DayEndNAV'],
							'MonthEndNAVDate':str(x['MonthEndNAVDate']),
							'MonthEndNAV':x['MonthEndNAV'],
							'UnsplitNAV':x['UnsplitNAV'],
							'NAV52wkHigh':x['NAV52wkHigh'],
							'NAV52wkHighDate':str(x['NAV52wkHighDate']),

							'NAV52wkLow':x['NAV52wkLow'],
							'NAV52wkLowDate':str(x['NAV52wkLowDate']),
							'PerformanceReturnSource':x['PerformanceReturnSource'],
							'moneda':x['CurrencyISO3__nombre']
							})
				else:
					lista = {"mensaje":"No existen datos"}

			except precio_actual.DoesNotExist:
				pass


		return HttpResponse(json.dumps(lista,indent=4),content_type="application/json")

	elif request.method == 'POST':

		mensaje = ""
		flag=True

		DayEndNAVDate = request.data['DayEndNAVDate']
		DayEndNAV= request.data['DayEndNAV']
		MonthEndNAVDate=request.data['MonthEndNAVDate']
		MonthEndNAV = request.data['MonthEndNAV']
		UnsplitNAV = request.data['UnsplitNAV']
		NAV52wkHigh= request.data['NAV52wkHigh']
		NAV52wkHighDate=request.data['NAV52wkHighDate']
		NAV52wkLow = request.data['NAV52wkLow']
		NAV52wkLowDate=request.data['NAV52wkLowDate']
		PerformanceReturnSource = request.data['PerformanceReturnSource']

		mon= request.data['moneda']

		nombre_fondo = request.data['fondo']
		clase_proveedor = request.data['clase_proveedor']

		if DayEndNAVDate=='' or DayEndNAV==''or MonthEndNAVDate==''or MonthEndNAV==''or UnsplitNAV==''or NAV52wkHigh==''or NAV52wkHighDate==''or NAV52wkLow==''or NAV52wkLowDate==''or PerformanceReturnSource=='' or mon=='':
			mensaje = {"mensaje":"Debes completar todos los campos"}
		else:
			try:
				f = fondo.objects.get(nombre=nombre_fondo)
			except fondo.DoesNotExist:
				flag = False
				mensaje = {"mensaje":"error en los datos"}

			try:
				if flag==True:
					i = instrumento.objects.get(fondo=f,clase_proveedor=clase_proveedor)
			except instrumento.DoesNotExist:
				flag = False
				mensaje = {"mensaje":"error en los datos"}

			try:
				if flag==True:
					m = moneda.objects.get(nombre=mon)
			except moneda.DoesNotExist:
				flag = False
				mensaje = {"mensaje":"error en los datos"}

			try:
				if flag==True:
					b = bindex.objects.get(pk=i.bindex_id)
					query = precio_actual.objects.filter(bindex=b,DayEndNAVDate=DayEndNAVDate,DayEndNAV=DayEndNAV,MonthEndNAVDate=MonthEndNAVDate,MonthEndNAV=MonthEndNAV
					,UnsplitNAV=UnsplitNAV,NAV52wkHigh=NAV52wkHigh,NAV52wkHighDate=NAV52wkHighDate,NAV52wkLow=NAV52wkLow, NAV52wkLowDate= NAV52wkLowDate
					,PerformanceReturnSource=PerformanceReturnSource,CurrencyISO3=m)
					if query.count()>0:
						mensaje = {"mensaje":"El cliente que intentas crear ya existe"}
					else:
						b = bindex.objects.get(pk=i.bindex_id)
						preact = precio_actual(bindex=b,DayEndNAVDate=DayEndNAVDate,DayEndNAV=DayEndNAV,MonthEndNAVDate=MonthEndNAVDate,MonthEndNAV=MonthEndNAV
						,UnsplitNAV=UnsplitNAV,NAV52wkHigh=NAV52wkHigh,NAV52wkHighDate=NAV52wkHighDate,NAV52wkLow=NAV52wkLow, NAV52wkLowDate= NAV52wkLowDate
						,PerformanceReturnSource=PerformanceReturnSource,CurrencyISO3=m)
						preact.save()
						mensaje = {"mensaje":"Datos guardados con exito"}
			except bindex.DoesNotExist:
				mensaje = {"mensaje":"error en los datos"}

		return HttpResponse(json.dumps(mensaje,indent=4),content_type="application/json")
