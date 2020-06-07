from django.db import models
from django.urls import reverse
from django.core.validators import MinLengthValidator
# Create your models here.
class RouterApp(models.Model):
	sapid = models.CharField(max_length =18, validators=[MinLengthValidator(18)],unique = True)
	hostname = models.CharField(max_length=14,unique = True)
	loopback = models.GenericIPAddressField(unique=True)
	macaddress = models.CharField(max_length=17, validators=[MinLengthValidator(17)],unique=True)

	def get_absolute_url(self,**kwargs):
		return reverse('detail',kwargs ={'pk':self.pk})
