from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from django.views.generic import CreateView
from django.views.generic.edit import UpdateView, DeleteView
from Inversiones_peniche.forms import RegistroForm
from Inversiones_peniche.forms import VehiculoForm
from Inversiones_peniche.models import Vehiculo
from .forms import ClienteForm
from .models import Cliente


class RegistroUsuario(CreateView):
    model = User
    template_name = "app/registrar.html"
    form_class = RegistroForm
    success_url = reverse_lazy('inversiones_peniche:index')


# Create your views here.
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


def registro_vehiculo(request):
    if request.method == 'POST':

        form = VehiculoForm(request.POST)
        if form.is_valid():
            matricula = request.POST.get('matricula', '')
            modelo = request.POST.get('modelo', '')
            color = request.POST.get('color', '')
            condicion = request.POST.get('condicion', '')
            valor_mercado = request.POST.get('valor_mercado', '')
            vehiculo_obj = Vehiculo(matricula=matricula, modelo=modelo, color=color, condicion=condicion,
                                    valor_mercado=valor_mercado)
            vehiculo_obj.save()

            # return HttpResponseRedirect(reverse('inversiones_peniche:'))
    else:
        form = VehiculoForm()

    return render(request, 'inversiones_peniche/form_vehiculo.html', {
        'form': form,
    })

