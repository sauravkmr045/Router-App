from django.contrib import admin
from django.urls import path,include
from app1 import views

urlpatterns = [
    path('admin/', admin.site.urls),
  #  path('', views.EmployeeListCreateModelmixins.as_view()),
   # path('rud/<int:pk>', views.EmployeeRetrieveUpdateDestroyModelMixins.as_view()),
    
    
    path('api-auth/', include('rest_framework.urls')),
    path('', views.ListRouterAPIView.as_view()),# for displaying list of record
    path('create/',views.CreateRouterAPIView.as_view()), # for creating a record
    path('retrieve/<int:pk>', views.RetrieveRouterAPIView.as_view()), # for reterieval of specific record
    path('update/<str:macaddress>', views.UpdateRouterAPIView.as_view()),
    path('delete/<int:pk>', views.DestroyRouterAPIView.as_view()),
  

    
]
