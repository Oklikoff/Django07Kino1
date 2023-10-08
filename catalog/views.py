from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import *
from catalog.models import Animal


# Create your views here.
def index(req):
    return render(req,'index.html')


from django.views import generic
class AnimalListView(generic.ListView):
    model = Animal
    template_name = 'catalogs/animal_list.html'

class AnimalDetailView(generic.DetailView):
    model = Animal
    template_name = 'catalogs/animal_detail.html'



# from django.http import HttpResponse
# def info(req,id):
#     animal=Animal.objects.get(id=id)
#     return HttpResponse(animal.name)