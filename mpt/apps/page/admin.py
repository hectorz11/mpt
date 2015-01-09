from django.contrib import admin
from mpt.apps.page.models import Locacion,Departamento,Persona,Tipo,Equipo,Movimiento

class LocacionAdmin(admin.ModelAdmin):
	list_display = ('descripcion','control')

class DepartamentoAdmin(admin.ModelAdmin):
	list_display = ('descripcion','locacion','control')
	fields = ('descripcion',('locacion','control'))

class PersonaAdmin(admin.ModelAdmin):
	list_display = ('apellidos','nombres','cargo','departamento','control')
	fields = (('nombres','apellidos'),('departamento','cargo'),'control')

class EquipoAdmin(admin.ModelAdmin):
	list_display = ('codigo','tipo','estado','marca','serial','control','persona')
	fields = ('codigo',('tipo','estado'),('marca','serial'),'descripcion','persona','control')

admin.site.register(Locacion,LocacionAdmin)
admin.site.register(Departamento,DepartamentoAdmin)
admin.site.register(Persona,PersonaAdmin)
admin.site.register(Tipo)
admin.site.register(Equipo,EquipoAdmin)
admin.site.register(Movimiento)