from django import forms
from app1.models import RouterApp

class RouterAppForm(forms.ModelForm):
	class Meta:
		fields = '__all__'
		model = RouterApp
