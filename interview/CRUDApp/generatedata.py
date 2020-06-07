import os  
os.environ.setdefault('DJANGO_SETTINGS_MODULE','CRUDApp.settings')
import django
django.setup()   


from faker import Faker
f = Faker()
mac = input('enter 16 digit mac address')
lp = input('enter the loopback ip and skip the last digit')
sap = input('enter 17 digit sap id')


def routerinfo_generator(n):
    for i in range(n):

        sapid = sap + str(i)
        hostname = f.name()
        loopback= lp + str(i)
        macaddress =  mac +str(i)
	    router_record = RouterApp.objects.get_or_create(sapid=sapid,hostname=hostname,loopback=loopback,macaddress= macaddress) 
	    router_record.save()
                       
        
        
        
        


x = routerinfo_generator(2)
print(list(x))
