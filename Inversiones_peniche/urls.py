from django.conf.urls import url, include

from .views import ClienteUpdate
from . import views
from .views import RegistroUsuario
from django.contrib import admin
from django.contrib.auth.views import login
from django.conf.urls import url

app_name = 'inversiones_peniche'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^.*\.html', views.gentella_html, name='gentella'),
    url(r'nuevo/$', views.ClienteCreate.as_view(), name='cliente-add'),
    url(r'editar/(?P<pk>[0-9]+)/$', ClienteUpdate.as_view(), name='cliente-update'),
    url(r'^login$', login, {'template_name': 'loginUsuario.html'}, name='login'),
    url(r'^registrar', RegistroUsuario.as_view(), name="registrar"),
    # url(r'nuevo/$',views.PrestamoCreate.as_view(), name="prestamo-add")

]

