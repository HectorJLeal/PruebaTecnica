from dataclasses import fields
from django import forms
from .models import Users

class FormularioRegistro(forms.ModelForm):
    class Meta:
        
        model = Users
        fields = (
            'Nombre',
            'Users',
            'Contraseña',
        )

        widgets = {
            'Nombre': forms.TextInput(
                attrs= {
                    'placeholder': 'Ingrese texto',
                    'class': 'campo',
                }
            ),
            'Users': forms.TextInput(
                attrs= {
                    'class': 'campo',
                }
            ),
            'Contraseña': forms.PasswordInput(
                attrs= {
                    'class': 'campo',
                }
            )
        }
    def clean_nombre(self):
        nombre = self.cleaned_data.get('Nombre')

        return nombre