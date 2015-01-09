from django import forms
from django.contrib.auth.models import User

class LoginForm(forms.Form):
	username = forms.CharField(widget=forms.TextInput())
	password = forms.CharField(widget=forms.PasswordInput(render_value=False))

class RegisterForm(forms.Form):
	nombres 	= forms.CharField(widget=forms.TextInput())
	apellidos 	= forms.CharField(widget=forms.TextInput())
	username 	= forms.CharField(label="Nombre de Usuario",widget=forms.TextInput())
	password_one	= forms.CharField(label="Password",widget=forms.PasswordInput(render_value=False))
	password_two	= forms.CharField(label="Confirmar password",widget=forms.PasswordInput(render_value=False))

	def clean_nombres(self):
		nombres = self.cleaned_data['nombres']
		try:
			u = User.objects.get(nombres=nombres)
		except User.DoesNotExist:
			return nombres
		raise forms.ValidationError('Los Nombres ya existen')

	def clean_apellidos(self):
		apellidos = self.cleaned_data['apellidos']
		try:
			u = User.objects.get(apellidos=apellidos)
		except User.DoesNotExist:
			return apellidos
		raise forms.ValidationError('Los apellidos ya existen')

	def clean_username(self):
		username = self.cleaned_data['username']
		try:
			u = User.objects.get(username=username)
		except User.DoesNotExist:
			return username
		raise forms.ValidationError('Nombre de usuario ya existe')

	def clean_password_two(self):
		password_one = self.cleaned_data['password_one']
		password_two = self.cleaned_data['password_two']
		if password_one == password_two:
			pass
		else:
			raise forms.ValidationError('Password no coiciden')