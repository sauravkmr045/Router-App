from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from app1.serializers import RouterAppSerializer
from app1.models import RouterApp
from rest_framework.authentication  import BasicAuthentication,SessionAuthentication
from rest_framework.permissions import IsAuthenticated #,IsAdminUser,IsAuthenticatedOrReadOnly,DjangoModelPermissions,DjangoModelPermissionsOrAnonReadOnly 
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import ListAPIView,CreateAPIView,RetrieveAPIView, RetrieveDestroyAPIView,RetrieveUpdateDestroyAPIView
from rest_framework.generics import UpdateAPIView,DestroyAPIView,ListCreateAPIView, RetrieveUpdateAPIView

start = input('enter the start range of ip')
end = input('enter the end range of ip')

class ListRouterAPIView(ListAPIView):
	queryset = RouterApp.objects.filter(loopback__range=(start, end)) 
	serializer_class= RouterAppSerializer


class DestroyRouterAPIView(DestroyAPIView):
	queryset = RouterApp.objects.filter(ip__startswith ='10')
	serializer_class= RouterAppSerializer
	#lookup_field =str(loopback)

class CreateRouterAPIView(CreateAPIView):
	queryset = RouterApp.objects.all()
	serializer_class= RouterAppSerializer

class UpdateRouterAPIView(UpdateAPIView):
	queryset = RouterApp.objects.all()
	serializer_class= RouterAppSerializer
	


class RetrieveRouterAPIView(RetrieveAPIView):
	queryset = RouterApp.objects.filter(sapid__lte =4556336366)
	serializer_class= RouterAppSerializer
	#lookup_field = str(loopback)
	


	#lookup_field = 'id'
	#authentication_classes = [BasicAuthentication,]
	#permissions_classes = [IsAuthenticated,]







	#AllforAdmin
	
	


	#authentication_classes = [TokenAuthentication,]
	#permissions_classes = [IsGETOrPatch,]#AllforAdmin

	#permissions_classes = [IsReadOnly,]

	#permissions_classes = [DjangoModelPermissions,]


	#permissions_classes = [IsAuthenticated,]

	# please look at the settings.py at the end we have globally configured authentication