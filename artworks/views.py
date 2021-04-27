from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Artwork #, Category
#from .forms import PaintingForm, EditPaintingForm
from django.urls import reverse_lazy

# Create your views here.
def home(request):
    return render(request, 'home.html' , {})

class HomeView(ListView):
    model = Artwork
    template_name = 'home.html'


class ArtworkView(ListView):
    model = Artwork
    template_name = 'artworks.html'
    #ordering = ['-id']
    ordering = ['-artwork_date']