import json
from django.conf.urls import url, include
from anuario.models import reporte_anual_cuota,bindex,instrumento,fondo
from rest_framework.decorators import api_view
from django.http import HttpResponse

@api_view(['GET','POST','PUT'])
def apiReporteAnualCuota(request,id=None):
	if request.method == 'GET':
		if id is not None:
			try:
				lista=[]
				query =reporte_anual_cuota.objects.values('AnnualReportDate','NetExpenseRatio','AnnualReportPerformanceFee','InterimNetExpenseRatioDate','InterimNetExpenseRatio').get(pk=id)
				lista.append({
					'AnnualReportDate':str(query['AnnualReportDate']),
					'NetExpenseRatio':query['NetExpenseRatio'],
					'AnnualReportPerformanceFee':query['AnnualReportPerformanceFee'],
					'InterimNetExpenseRatioDate':str(query['InterimNetExpenseRatioDate']),
					'InterimNetExpenseRatio':query['InterimNetExpenseRatio'],
					})
			except reporte_anual_cuota.DoesNotExist:
				lista = {"mensaje":"No existen datos"}

		else:
			try:
				lista=[]
				query = reporte_anual_cuota.objects.all().values('AnnualReportDate','NetExpenseRatio','AnnualReportPerformanceFee','InterimNetExpenseRatioDate','InterimNetExpenseRatio')
				if query.count()>0:
					for x in query:
						lista.append({
        					'AnnualReportDate':str(x['AnnualReportDate']),
        					'NetExpenseRatio':x['NetExpenseRatio'],
        					'AnnualReportPerformanceFee':x['AnnualReportPerformanceFee'],
        					'InterimNetExpenseRatioDate':str(x['InterimNetExpenseRatioDate']),
        					'InterimNetExpenseRatio':x['InterimNetExpenseRatio'],
        					})
				else:
					lista = {"mensaje":"No existen datos"}

			except reporte_anual_cuota.DoesNotExist:
				pass


		return HttpResponse(json.dumps(lista,indent=4),content_type="application/json")

	elif request.method == 'POST':

		mensaje = ""
		flag=True

		AnnualReportDate = request.data['AnnualReportDate']
		NetExpenseRatio= request.data['NetExpenseRatio']
		AnnualReportPerformanceFee=request.data['AnnualReportPerformanceFee']
		InterimNetExpenseRatioDate = request.data['InterimNetExpenseRatioDate']
		InterimNetExpenseRatio = request.data['InterimNetExpenseRatio']

		nombre_fondo = request.data['fondo']
		clase_proveedor = request.data['clase_proveedor']

		if AnnualReportDate=='' or NetExpenseRatio==''or AnnualReportPerformanceFee==''or InterimNetExpenseRatioDate==''or InterimNetExpenseRatio=='':
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
					b = bindex.objects.get(pk=i.bindex_id)
					query = reporte_anual_cuota.objects.filter(bindex=b,AnnualReportDate=AnnualReportDate,NetExpenseRatio=NetExpenseRatio,AnnualReportPerformanceFee=AnnualReportPerformanceFee,InterimNetExpenseRatioDate=InterimNetExpenseRatioDate,InterimNetExpenseRatio=InterimNetExpenseRatio)
					if query.count()>0:
						mensaje = {"mensaje":"El cliente que intentas crear ya existe"}
					else:
						b = bindex.objects.get(pk=i.bindex_id)
						repanu = reporte_anual_cuota(bindex=b,AnnualReportDate=AnnualReportDate,NetExpenseRatio=NetExpenseRatio,AnnualReportPerformanceFee=AnnualReportPerformanceFee,InterimNetExpenseRatioDate=InterimNetExpenseRatioDate,InterimNetExpenseRatio=InterimNetExpenseRatio)
						repanu.save()
						mensaje = {"mensaje":"Datos guardados con exito"}
			except bindex.DoesNotExist:
				mensaje = {"mensaje":"error en los datos"}

		return HttpResponse(json.dumps(mensaje,indent=4),content_type="application/json")
