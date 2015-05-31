from django.conf.urls import url

from . import views
from . import index
from . import first_validaringreso

urlpatterns = [
    url(r'^$', index.index, name='index'),
    url(r'^validaringreso/$', first_validaringreso.first_validaringreso, name='first_validaringreso'),
]

