from django.shortcuts import render
from .models import City
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.
def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

##### CITY ######
def cities_index(request):
    cities = City.objects.all()
    return render(request, 'cities/index.html', { 'cities': cities })
    
