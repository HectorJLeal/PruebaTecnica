from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
      path('registrar/', views.Registrar.as_view( )),
]