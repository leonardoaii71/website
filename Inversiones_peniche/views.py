from django.http import HttpResponse, response
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from Inversiones_peniche.mixins import AjaxFormMixin
from .models import Cliente
from .forms import ClienteForm
from Inversiones_peniche.models import Vehiculo
from django.views.generic import CreateView
from django.views.generic.edit import UpdateView, DeleteView
from Inversiones_peniche.forms import RegistroForm
from Inversiones_peniche.forms import VehiculoForm
from .multiforms import MultiFormsView
from Inversiones_peniche.models import Vehiculo
from .forms import ClienteForm
from .models import Cliente
# from .models import Prestamo


# Create your views here.
class RegistroUsuario(CreateView):
    model = User
    template_name = "app/registrar.html"
    form_class = RegistroForm
    success_url = reverse_lazy('inversiones_peniche:index')


# class PrestamoCreate(CreateView):
#     model = Prestamo
#     template_name = "app/pruebaPrestamos.html"
#     form_class = PrestamoForm
#     success_url = reverse_lazy('inversiones_peniche:index')


def index(request):
    context = {}
    template = loader.get_template('app/index.html')
    return HttpResponse(template.render(context, request))


def gentella_html(request):
    context = {}
    # The template to be loaded as per gentelella.
    # All resource paths for gentelella end in .html.

    # Pick out the html file name from the url. And load that template.
    load_template = request.path.split('/')[-1]
    template = loader.get_template('app/' + load_template)
    return HttpResponse(template.render(context, request))


class Clienteform(MultiFormsView):

    form_classes = {'cliente': ClienteForm, 'vehiculo': VehiculoForm}
    template_name = 'app/cliente_form2.html'
    success_url = reverse_lazy('inversiones_peniche:index')



class ClienteCreate(CreateView):
    model = Cliente
    form_class = ClienteForm
    template_name = 'app/cliente_form.html'
    success_url = reverse_lazy('inversiones_peniche:index')


class ClienteUpdate(UpdateView):
    model = Cliente
    form_class = ClienteForm
    template_name = 'app/cliente_form.html'
    success_url = reverse_lazy('inversiones_peniche:index')


class ClienteDelete(DeleteView):
    model = Cliente
    #success_url = reverse_lazy('cliente-list')


class VehiculoCreate(CreateView):
    model = Vehiculo
    form_class = VehiculoForm
    template_name = 'app/cliente_form.html'
    success_url = reverse_lazy('inversiones_peniche:index')


class registro_vehiculo(CreateView, AjaxFormMixin):
    model = Vehiculo
    form_class = VehiculoForm
    template_name = 'app/cliente_form2.html'
    success_url = reverse_lazy('inversiones_peniche:index')

    def form_valid(self, form):
        super().form_valid(form)
        return ""
