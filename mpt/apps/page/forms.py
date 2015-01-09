from django import forms
from mpt.apps.page.models import Locacion,Departamento,Persona,Equipo,Tipo,Movimiento

class addLocacionForm(forms.ModelForm):
	class Meta:
		model = Locacion

class addDepartamentoForm(forms.ModelForm):
	class Meta:
		model = Departamento

class addPersonaForm(forms.ModelForm):
	class Meta:
		model = Persona

class addEquipoForm(forms.ModelForm):
	class Meta:
		model = Equipo

class addTipoForm(forms.ModelForm):
	class Meta:
		model = Tipo

class addMovimientoForm(forms.ModelForm):
	class Meta:
		model = Movimiento