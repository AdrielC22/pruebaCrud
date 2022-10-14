from django import forms
from django import forms
from .models import Tarea, Actividad

class TareaForm(forms.ModelForm):
    class Meta:
        model = Tarea
        fields = ['tarea','status']

class ActividadForm(forms.ModelForm):
    class Meta:
        model = Actividad
        fields = ['Actividad']