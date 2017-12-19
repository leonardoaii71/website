from django import forms
from django.core import validators
from django.core.validators import RegexValidator
from django.forms import ModelForm, TextInput, EmailInput, DateInput, RadioSelect, Select
import datetime
from django.utils import timezone
from .models import Vehiculo
from .models import Cliente
from .models import Prestamo
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class RegistroForm(UserCreationForm):

    class Meta:
        model = User
        fields = [
                'username',
                'first_name',
                'last_name',
                'email',
        ]
        labels = {
                'username' : 'Nombre de usuario',
                'first_name' : 'Nombre',
                'last_name' : 'Apellidos',
                'email': 'Correo',
        }


class VehiculoForm(forms.Form):
    matricula = forms.CharField(max_length=40)
    modelo = forms.CharField
    # tipo = forms.ForeignKey(Tipo, on_delete=forms.CASCADE)
    color = forms.CharField
    condicion = forms.CharField
    valor_mercado = forms.IntegerField


class ClienteForm(ModelForm):
    cedula = forms.CharField(validators=[
        RegexValidator(regex=r'\d{11}', code='invalid_cedula', message='La cedula debe contener solo 11 digitos')],
        max_length=20,
        widget=TextInput(attrs={'class': 'form-control has-feedback-left', 'placeholder': 'Cedula de Identidad'}))

    class Meta:
        model = Cliente
        fields = '__all__'

        widgets = {
            'nombre': TextInput(attrs={'class': 'form-control has-feedback-left', 'placeholder': 'Nombre', 'aria-describedby':"helpBlock", 'required':''}),
            'apellido': TextInput(attrs={'class': 'form-control', 'placeholder': 'Apellido'}),
            'correo': EmailInput(attrs={'class': 'form-control has-feedback-left', 'placeholder': 'Correo'}),
            'fecha_nacimiento': DateInput(attrs={'class': 'form-control','onblur':"(this.type='text')",
                                                                        'onfocus':"(this.type='date')",
                                                                        'placeholder': 'Fecha de Nacimiento'}),

            'direccion':    TextInput(attrs={'class': 'form-control', 'placeholder': 'Direccion'}),
            'numero_cel':   TextInput(attrs={'type': 'tel', 'class': 'form-control has-feedback-left',
                                           'data-inputmask':"'mask': '(999) 999-9999', 'removeMaskOnSubmit': true ",
                                           'placeholder': 'Celular'}),
            'numero_telefono': TextInput(attrs={'class': 'form-control',
                                                'data-inputmask':"'mask': '(999) 999-9999', 'removeMaskOnSubmit': true ",
                                                'placeholder': 'Telefono'}),
            'vehiculo': TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'})
        }

        help_texts = {
            'nombre': 'Escriba el nombre de la persona e.g Leonardo',
        }
        error_messages = {
            'nombre': {
                'max_length': "Este nombre es muy largo",

            },

        }

        def clean_fecha_nacimiento(self):
            fecha = self.cleaned_data['fecha_nacimiento']
            if fecha > timezone.now():
                raise validators.ValidationError(message='Fecha incorrecta: no puede ser una fecha futura')
            return fecha


class VehiculoForm(ModelForm):

    class Meta:
        model = Vehiculo
        fields = '__all__'

        widgets = {
            'matricula': TextInput(attrs={'class': "form-control has-feedback-left", 'placeholder': 'Matricula'}),
            'modelo': TextInput(attrs={'class': "form-control ", 'placeholder': 'Modelo '}),
            'year': TextInput(attrs={'class': "form-control has-feedback-left", 'placeholder': 'Ano'}),
            'color': TextInput(attrs={'class': "form-control ", 'placeholder': 'Color'}),
            'condicion': TextInput(attrs={'class': "form-control has-feedback-left", 'placeholder': 'Condicion'}),
            'valor_mercado': TextInput(attrs={'class': "form-control ", 'placeholder': 'Valor de mercado'}),
        }

class PrestamoForm(ModelForm):


    class Meta:
        model = Prestamo
        fields = ['cliente', 'vehiculo', 'operador', 'fecha_actual', 'monto_prestado', 'tasa_interes', 'monto_total', 'pago_mensual', 'tipo_prestamo', 'total_intereses', 'plazo']

        widgets = {

            'cliente': TextInput(attrs={'class': "form-control has-feedback-left", 'placeholder': 'Cliente Asociado', 'id': "clienteAsoc"}),
            'vehiculo': TextInput(attrs={'class': "form-control ", 'placeholder': 'Vehiculo Asociado ', 'id': "vehiculoAsoc"}),
            'operador': TextInput(attrs={'class': "form-control has-feedback-left", 'placeholder': 'Operador', 'id': "usuario"}),
            'fecha_actual': TextInput(attrs={'class': "form-control ", 'placeholder': 'Fecha Actual', 'id': "fechaActual"}),
            'monto_prestado': TextInput(attrs={'class': "form-control has-feedback-left", 'placeholder': 'Monto Prestado', 'id': "principal"}),
            'tasa_interes': TextInput(attrs={'class': "form-control ", 'placeholder': 'Tasa de Interes', 'id': "interest"}),
            'monto_total': TextInput(attrs={'class': "form-control ", 'id': "total"}),
            'pago_mensual': TextInput(attrs={'class': "form-control ", 'id': "payment"}),
            'total_intereses': TextInput(attrs={'class': "form-control ", 'id': "totalinterest"}),
            'tipo_prestamo': RadioSelect(attrs={'class': "flat ", 'required' :""}),
            'plazo': Select(attrs={'class': "form-control", 'required': "", 'id': 'terms'})

        }

