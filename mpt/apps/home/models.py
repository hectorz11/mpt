from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
	username = models.CharField(max_length=20)
	password = models.CharField(max_length=20)
	nombres = models.CharField(max_length=40,verbose_name='Nombre(s)')
	apellidos = models.CharField(max_length=40)
	control = models.BooleanField(default=True)
	user = models.ForeignKey(User)

	def __unicode__(self):
		return self.username

	class Meta:
		ordering = ['-username']


class Backup(models.Model):
	fecha = models.DateTimeField(auto_now_add=True)
	observacion = models.TextField(max_length=750,null=True)
	userProfile = models.ForeignKey(UserProfile)

	def __unicode__(self):
		return self.observacion