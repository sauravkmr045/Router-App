from django.contrib import admin
from app1.models import RouterApp

# Register your models here.
class RouterAppAdmin(admin.ModelAdmin):
	list_display = ['sapid','hostname','loopback','macaddress']

admin.site.register(RouterApp,RouterAppAdmin)
