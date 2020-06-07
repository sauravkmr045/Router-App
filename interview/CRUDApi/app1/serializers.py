from rest_framework.serializers import ModelSerializer
from app1.models import RouterApp

class RouterAppSerializer(ModelSerializer):
	class Meta:
		model = RouterApp
		fields = '__all__'