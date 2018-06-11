import json
from django.conf.urls import url, include
from anuario.models import countryExposure,fondo,instrumento,bindex
from rest_framework.decorators import api_view
from django.http import HttpResponse

@api_view(['GET','POST','PUT'])
def apiCountryExposure(request,id=None):
	if request.method == 'GET':
		if id is not None:
			try:
				query =countryExposure.objects.values('country_exposure','country_exposure_equity','country_exposure_bond','country_exposure_convertible').get(pk=id)

			except countryExposure.DoesNotExist:
				query = {"mensaje":"No existen datos"}

		else:
			try:
				query = countryExposure.objects.all()
				if query.count()<1:
					query = {"mensaje":"No existen datos"}
				else:
					query = list(countryExposure.objects.all().values('country_exposure','country_exposure_equity','country_exposure_bond','country_exposure_convertible'))

			except countryExposure.DoesNotExist:
				pass


		return HttpResponse(json.dumps(query,indent=4),content_type="application/json")

	elif request.method == 'POST':

		mensaje = ""
		flag=True

		c_e = request.data['countryExposure']
		c_e_e= request.data['countryExposureEquity']
		c_e_b=request.data['countryExposureBond']
		c_e_c = request.data['countryExposureConvertible']

		nombre_fondo = request.data['fondo']
		clase_proveedor = request.data['clase_proveedor']

		if c_e=='' or c_e_e==''or c_e_b==''or c_e_c==''or nombre_fondo==''or clase_proveedor=='':
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
					query = countryExposure.objects.filter(bindex=b,country_exposure=c_e,country_exposure_equity=c_e_e,country_exposure_bond=c_e_b,country_exposure_convertible=c_e_c)
					if query.count()>0:
						mensaje = {"mensaje":"El cliente que intentas crear ya existe"}
					else:
						b = bindex.objects.get(pk=i.bindex_id)
						cou_exp = countryExposure(bindex=b,country_exposure=c_e,country_exposure_equity=c_e_e,country_exposure_bond=c_e_b,country_exposure_convertible=c_e_c)
						cou_exp.save()
						mensaje = {"mensaje":"Datos guardados con exito"}
			except bindex.DoesNotExist:
				mensaje = {"mensaje":"error en los datos"}

		return HttpResponse(json.dumps(mensaje,indent=4),content_type="application/json")
