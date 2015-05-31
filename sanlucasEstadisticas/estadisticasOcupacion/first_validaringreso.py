from django.shortcuts import render


# Create your views here.

from django.http import HttpResponse
from django.template import RequestContext, loader
from django.views.generic import RedirectView
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate


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


	return render(request, 'turnosapp/validaingreso.html', context)

