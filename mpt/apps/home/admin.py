from django.contrib import admin
from mpt.apps.home.models import UserProfile,Backup

class UserAdmin(admin.ModelAdmin):
	list_display = ('username','nombres','apellidos','control')
	fields = (('username','password'),('nombres','apellidos'),'control','user')

admin.site.register(UserProfile,UserAdmin)
admin.site.register(Backup)