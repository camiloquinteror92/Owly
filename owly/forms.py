from django import forms
from .models import Torre

class TorreForm(forms.ModelForm):
    class Meta:
        model = Torre
        fields = ['nombre_descripcion', 'Etapa', 'imagenes']

