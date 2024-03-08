from django import forms
from django.core.exceptions import ValidationError
import re
from .models import Alumno

class AlumnoForm(forms.ModelForm):
    class Meta:
        model = Alumno
        fields = ['carnet', 'nombres', 'apellidos', 'correoElectronico', 'fechaNacimiento']
        widgets = {
            'fechaNacimiento': forms.DateInput(attrs={'type': 'date'}),
        }
    
    def __init__(self, *args, **kwargs):
        super(AlumnoForm, self).__init__(*args,**kwargs)
        self.fields['carnet'].widget.attrs.update({'placeholder': 'Ejemplo: 1234-20-7890'})
        self.fields['nombres'].widget.attrs.update({'placeholder': 'Ejemplo: Juan'})
        self.fields['apellidos'].widget.attrs.update({'placeholder': 'Ejemplo: Pérez'})
        self.fields['correoElectronico'].widget.attrs.update({'placeholder': 'Ejemplo: juan.perez@example.com'})
        self.fields['fechaNacimiento'].widget.attrs.update({'placeholder': 'AAAA-MM-DD'})
        
        self.fields['carnet'].widget.attrs.update({'autocomplete': 'off'})
        self.fields['nombres'].widget.attrs.update({'autocomplete': 'off'})
        self.fields['apellidos'].widget.attrs.update({'autocomplete': 'off'})
        self.fields['correoElectronico'].widget.attrs.update({'autocomplete': 'off'})
        self.fields['fechaNacimiento'].widget.attrs.update({'autocomplete': 'off'})
        
    def clean_carnet(self):
        carnet = self.cleaned_data.get('carnet')
        
        alumno_qs = Alumno.objects.filter(carnet=carnet)
        if self.instance.pk:  
            alumno_qs = alumno_qs.exclude(pk=self.instance.pk) 

        if alumno_qs.exists():
            raise ValidationError('Un alumno con este carnet ya existe.')

        return carnet