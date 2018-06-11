import json
from django.conf.urls import url, include
from anuario.models import categoria,broadCategory,moneda
from rest_framework.decorators import api_view
from django.http import HttpResponse

@api_view(['GET','POST','PUT'])
def apiCategoria(request,id=None):
	if request.method == 'GET':
		if id is not None:
			try:
				query =categoria.objects.values('id','nombre','broadCategory__nombre','moneda__nombre').get(pk=id)

			except categoria.DoesNotExist:
				query = {"mensaje":"No existen datos"}

		else:
			try:
				query = categoria.objects.all()
				if query.count()<1:
					query = {"mensaje":"No existen datos"}
				else:
					query = list(categoria.objects.all().values('id','nombre','broadCategory__nombre','moneda__nombre'))

			except categoria.DoesNotExist:
				pass


		return HttpResponse(json.dumps(query,indent=4),content_type="application/json")

	elif request.method == 'POST':
		flag = True
		mensaje = ""

		cat_id =  request.data['categoria_id']
		cat_nombre = request.data['categoria']

		broadCat_nombre= request.data['broadCategory']
		mon_nombre = request.data['moneda']

		if broadCat_nombre=='' or mon_nombre==''or cat_nombre==''or cat_id=='':
			mensaje = {"mensaje":"Debes completar todos los campos"}
		else:
			try:
				bro = broadCategory.objects.get(nombre=broadCat_nombre)
			except broadCategory.DoesNotExist:
				flag = False
				mensaje = {"mensaje":"error en los datos"}

			try:
				if flag == True:
					m = moneda.objects.get(nombre=mon_nombre)
			except moneda.DoesNotExist:
				flag = False
				mensaje = {"mensaje":"error en los datos"}

			try:
				if flag == True:
					query = categoria.objects.filter(id=cat_id,nombre=cat_nombre,broadCategory=bro,moneda=m)
					if query.count()>0:
						mensaje = {"mensaje":"El cliente que intentas crear ya existe"}
					else:
						cat = categoria(id=cat_id,nombre=cat_nombre,broadCategory=bro,moneda=m)
						cat.save()
						mensaje = {"mensaje":"Datos guardados con exito"}
				else:
					mensaje = {"mensaje":"error en los datos"}

			except:
				mensaje = {"mensaje":"error en los datos"}

		return HttpResponse(json.dumps(mensaje,indent=4),content_type="application/json")
