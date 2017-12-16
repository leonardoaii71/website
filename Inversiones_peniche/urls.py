from django.conf.urls import url, include

#from .views import ClienteUpdate
from . import views


app_name = 'inversiones_peniche'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^.*\.html', views.gentella_html, name='gentella'),
    url(r'nuevo/cliente$', views.Clienteform.as_view(), name='cliente-add'),
    url(r'nuevo/vehiculo$', views.registro_vehiculo.as_view(), name='vehiculo-add'),
    url(r'editar/(?P<pk>[0-9]+)/$', views.ClienteUpdate.as_view(), name='cliente-update')
]

