from django.shortcuts import render, redirect
from app1.forms import RouterAppForm
from app1.models import RouterApp

# Create your views here.
def display(request):

	data = RouterApp.objects.all()

	return render(request, 'index.html', {'form': data	})

def create(request):
	form = RouterAppForm()
	if request.method == 'POST':
		form = RouterAppForm(request.POST)
		if form.is_valid():
			form.save()
		return redirect('/')
	return render(request, 'add.html', {'form': form})

def delete(request,id):
	router = RouterApp.objects.get(id = id)
	router.delete()
	return redirect('/')

def update(request,id):
	router = RouterApp.objects.get(id = id)
	if request.method =='POST':
		form = RouterAppForm(request.POST, instance = router)
		if form.is_valid():
			form.save()
		return redirect('/')

	return render(request,'update.html', {'router': router})
