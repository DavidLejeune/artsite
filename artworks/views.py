from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Artwork, Category
from .forms import ArtworkForm, EditArtworkForm
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

class ArtworkDetailView(DetailView):
    model = Artwork
    template_name = 'artwork_details.html'

class ArtworkView(ListView):
    model = Artwork
    template_name = 'artworks.html'
    #ordering = ['-id']
    ordering = ['-artwork_date']

class AddArtworkView(CreateView):
    model = Artwork
    form_class = ArtworkForm
    template_name = 'add_artwork.html'
    #fields = '__all__'
    #fields = ('title', 'author', 'body')


class UpdateArtworkView(UpdateView):
    model = Artwork
    form_class = EditArtworkForm
    template_name = 'update_artwork.html'
    #fields = '__all__'
    #fields = ('title', 'author', 'body')


class DeleteArtworkView(DeleteView):
    model = Artwork
    template_name = 'delete_artwork.html'
    #fields = '__all__'
    #fields = ('title', 'author', 'body')
    success_url = reverse_lazy('home')


class AddCategoryView(CreateView):
    model = Category
    #form_class = CategoryForm
    template_name = 'add_category.html'
    fields = '__all__'
    #fields = ('title', 'author', 'body')

def CategoryView(request, cats):
    category_artworks = Artwork.objects.filter(category=cats)
    return render(request, 'categories.html', {'cats':cats.title(), 'category_artworks':category_artworks})