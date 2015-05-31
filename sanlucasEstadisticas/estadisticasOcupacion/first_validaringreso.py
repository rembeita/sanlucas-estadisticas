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
	return render(request, 'estadisticasOcupacion/snd_panelgeneral.html', context)

