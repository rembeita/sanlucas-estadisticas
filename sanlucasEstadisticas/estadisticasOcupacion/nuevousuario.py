from django.shortcuts import render


# Create your views here.

from django.http import HttpResponse
from django.template import RequestContext, loader
from django.views.generic import RedirectView


from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User

def nuevousuario(request):

	user = User.objects.create_user('rodrigo', 'rodrigo@gmail.com', 'rod161082')
	user.save()
	context = localas()

	return render(request, 'estadisticasOcupacion/index.html', context)

