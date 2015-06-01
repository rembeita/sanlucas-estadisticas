from django.shortcuts import render


# Create your views here.

from django.http import HttpResponse
from django.template import RequestContext, loader
from django.views.generic import RedirectView
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate
from .models import Camas



def first_validaringreso(request):
	if request.method == 'POST':
		formvar = request.POST
		uservalue = str(formvar['user_frm'])
		passvalue = str(formvar['password_frm'])

	userquery = authenticate(username=uservalue, password=passvalue)

	context = locals()

	if userquery is None:
		mensaje = "El usuario o Password es incorrecto."
		mensaje2 = "Comuniquese con el departamento de Sistemas"
		context['MENSAJE'] = mensaje
		context['MENSAJE2'] = mensaje2
		return render(request, 'estadisticasOcupacion/first_novalidaingreso.html', context)


	camasquery = Camas.objects.all()
	camas = camasquery.filter(estad = "S").filter(asignable = "S")
	total_camas = camas.count()
	camas_ocupadas = camas.filter(internac__gt=0).count()
	print total_camas
	print camas_ocupadas
	camas_ocupadas_porcentaje = (float(camas_ocupadas) * 100) / float(total_camas)
	camas_ocupadas_porcentaje = float("{0:.2f}".format(camas_ocupadas_porcentaje))
	context['CAMAS_OCUPADAS'] = camas_ocupadas_porcentaje
	context['CAMAS_DISPONIBLES'] = 100 - camas_ocupadas_porcentaje

	edificio1 = [ "NEO", "PI1", "PI2", "PI3", "UC5", "UP", "UTI" ]
	edificio2 = [ "H20", "H21", "H22" ]
	camas_edificio1 = [] 
	camas_edificio2 = [] 
	for i in edificio1:
		camas_planta = []
		piso_camas = 0
		print "I: " + str(i)
		desc_edificio2 = camas.filter(cama__istartswith = i).values()
		generando_porcentaje = 0
		for j in desc_edificio2:
			piso_camas = piso_camas + 1
			tmplist = []
			tmplist.append(j['cama'])
			tmplist.append(j['descripcion'])
			tmplist.append(j['internac'])
			camas_planta.append(tmplist)
			if j['internac'] > 0:
				generando_porcentaje = generando_porcentaje + 1

		piso_ocupadas_porcentaje = (float(generando_porcentaje) * 100) / float(piso_camas)
		piso_ocupadas_porcentaje = float("{0:.2f}".format(piso_ocupadas_porcentaje))
		camas_planta.append(piso_ocupadas_porcentaje)
		camas_edificio1.append(camas_planta)

	for i in edificio2:
		camas_planta = []
		piso_camas = 0
		print "I: " + str(i)
		desc_edificio2 = camas.filter(cama__istartswith = i).values()
		generando_porcentaje = 0
		for j in desc_edificio2:
			piso_camas = piso_camas + 1
			tmplist = []
			tmplist.append(j['cama'])
			tmplist.append(j['descripcion'])
			tmplist.append(j['internac'])
			camas_planta.append(tmplist)
			if j['internac'] > 0:
				generando_porcentaje = generando_porcentaje + 1

		piso_ocupadas_porcentaje = (float(generando_porcentaje) * 100) / float(piso_camas)
		piso_ocupadas_porcentaje = float("{0:.2f}".format(piso_ocupadas_porcentaje))
		camas_planta.append(piso_ocupadas_porcentaje)
		camas_edificio2.append(camas_planta)

	print camas_edificio1
	print camas_edificio2
			#print desc_edificio2[j]
		#desc_edificio2 = camas.filter(cama__istartswith = i).values()
		#dic_camas_edificio2[i] = camas_edificio2
	#	print dir(camas_edificio2)
	#	print edificio2[i]

#	for key,piso in edificio2.items():
#		print "imprimir key"
#		print piso.values()

	context["EDIFICIO1"] = edificio1
	context["EDIFICIO2"] = edificio2 
	context["CAMAS_PLANTA"] = camas_planta
	context["CAMAS_EDIFICIO1"] = camas_edificio1
	context["CAMAS_EDIFICIO2"] = camas_edificio2

	return render(request, 'estadisticasOcupacion/snd_panelgeneral.html', context)

