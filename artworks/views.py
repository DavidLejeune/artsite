from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
#from .models import Painting, Category
#from .forms import PaintingForm, EditPaintingForm
from django.urls import reverse_lazy

# Create your views here.
def home(request):
    return render(request, 'home.html' , {})

#class HomeView(ListView):
#    model = Painting
#    template_name = 'home.html'