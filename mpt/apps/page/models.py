from django.db import models
from mpt.apps.home.models import UserProfile

class Locacion(models.Model):
	descripcion = models.CharField(max_length=50,verbose_name='Locacion')
	control = models.BooleanField(default=True)

	def __unicode__(self):
		return self.descripcion

class Departamento(models.Model):
	descripcion = models.CharField(max_length=50,verbose_name='Departamento')
	control = models.BooleanField(default=True)
	locacion = models.ForeignKey(Locacion)

	def __unicode__(self):
		return self.descripcion

class Persona(models.Model):
	nombres = models.CharField(max_length=40,verbose_name='Nombre(s)')
	apellidos = models.CharField(max_length=40)
	cargo = models.CharField(max_length=40)
	control = models.BooleanField(default=True)
	departamento = models.ForeignKey(Departamento)

	def __unicode__(self):
		nombreCompleto = "%s %s"%(self.nombres,self.apellidos)
		return nombreCompleto

class Tipo(models.Model):

	descripcion = models.CharField(max_length=40,verbose_name='Tipo')
	control = models.BooleanField(default=True)

	def __unicode__(self):
		return self.descripcion

class Equipo(models.Model):

	STATUS_CHOICES = (
		('Bueno',('Bueno')),
		('Regular',('Regular')),
		('Malogrado',('Malogrado')),)

	codigo = models.CharField(max_length=15,verbose_name='Codigo Patrimonial')
	tipo = models.ForeignKey(Tipo)
	estado = models.CharField(max_length=15,choices=STATUS_CHOICES,default=1)
	marca = models.CharField(max_length=20,null=True)
	serial = models.CharField(max_length=20,verbose_name='Serie',null=True)
	descripcion = models.TextField(max_length=750,null=True)
	control = models.BooleanField(default=True)
	persona = models.ForeignKey(Persona)

	def __unicode__(self):
		return self.codigo

class Movimiento(models.Model):
	fecha = models.DateTimeField(auto_now_add=True)
	tipo_movimiento = models.CharField(max_length=40)
	observacion = models.TextField(max_length=750)
	control = models.BooleanField(default=True)
	equipo = models.ForeignKey(Equipo)

	def __unicode__(self):
		return self.observacion