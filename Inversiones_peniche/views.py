from django.http import JsonResponse
from django.http import HttpResponse
from django.http import JsonResponse
from django.template import loader
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.views.generic.edit import UpdateView, DeleteView
from django.contrib.auth.models import User
from Inversiones_peniche.forms import RegistroForm
from Inversiones_peniche.forms import VehiculoForm
from Inversiones_peniche.models import Vehiculo
from .forms import ClienteForm
from .models import Cliente
from .multiforms import MultiFormsView


# from .models import Prestamo
from .forms import ClienteForm, PrestamoForm
from .models import Cliente, Prestamo
from django.http import HttpResponse
import json



# Create your views here.

def busqueda(request):
    if request.is_ajax():
        clientes = Cliente.objects.filter(nombre__startswith=request.GET['nombre']).values('nombre', 'id')
        return HttpResponse(json.dumps(list(clientes)), content_type='application/json')
    else:
        return HttpResponse("Solo Ajax");



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
    template_name = 'app/cliente_form.html'
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
    template_name = 'app/cliente_form.html'
    success_url = reverse_lazy('inversiones_peniche:index')

    def form_invalid(self, form):
        response = super().form_invalid(form)
        if self.request.is_ajax():
            return JsonResponse(form.errors, status=400)
        else:
            return response

    def form_valid(self, form):
        response = super().form_valid(form)

        if self.request.is_ajax():
            print(form.cleaned_data)
            data = {
                'val': form.cleaned_data['matricula'],
                'desc': form.cleaned_data['matricula'] +"  "+ form.cleaned_data['modelo'] +"  "+  str(form.cleaned_data['year'])
            }
            return JsonResponse(data)
        else:
            return response