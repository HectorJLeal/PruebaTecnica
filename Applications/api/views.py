from django.shortcuts import render
from django.views.generic import CreateView
from .models import Users
from .forms import FormularioRegistro


class Registrar(CreateView):
    model = Users
    template_name = 'registrar.html'
    form_class = FormularioRegistro
    success_url = '/'
