from dataclasses import fields
from django import forms
from .models import Users

class FormularioRegistro(forms.ModelForm):
    class Meta:
        
        model = Users
        fields = (
            'name',
            'user',
            'password',
        )

        widgets = {
            'name': forms.TextInput(
                attrs= {
                    'placeholder': 'Ingrese texto',
                    'class': 'campo',
                }
            ),
            'user': forms.TextInput(
                attrs= {
                    'class': 'campo',
                }
            ),
            'password': forms.PasswordInput(
                attrs= {
                    'class': 'campo',
                }
            )
        }
    def clean_nombre(self):
        nombre = self.cleaned_data.get('name')
    
        return nombre