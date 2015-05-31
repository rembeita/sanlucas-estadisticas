from django.conf.urls import url

from . import views
from . import index
from . import nuevousuario
from . import first_validaringreso

urlpatterns = [
    url(r'^$', index.index, name='index'),
    url(r'^validaringreso/$', first_validaringreso.first_validaringreso, name='first_validaringreso'),
    url(r'^nuevousuario/$', nuevousuario.nuevousuario, name='nuevousuario'),
]

