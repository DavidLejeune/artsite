from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Artwork, Category
from .forms import ArtworkForm, EditArtworkForm
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect

# Create your views here.

class HomeView(ListView):
    model = Artwork
    template_name = 'home.html'

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context


class ArtworkDetailView(DetailView):
    model = Artwork
    template_name = 'artwork_details.html'

    
    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(ArtworkDetailView, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu

        likes_obj = get_object_or_404(Artwork, id=self.kwargs['pk'])
        total_likes = likes_obj.total_likes()
        context["total_likes"] = total_likes
        return context




class ArtworkView(ListView):
    model = Artwork
    template_name = 'artworks.html'
    #ordering = ['-id']
    ordering = ['-artwork_date']

    
    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(ArtworkView, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context

class AddArtworkView(CreateView):
    model = Artwork
    form_class = ArtworkForm
    template_name = 'add_artwork.html'
    #fields = '__all__'
    #fields = ('title', 'author', 'body')
    
    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(AddArtworkView, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context


class UpdateArtworkView(UpdateView):
    model = Artwork
    form_class = EditArtworkForm
    template_name = 'update_artwork.html'
    #fields = '__all__'
    #fields = ('title', 'author', 'body')
    
    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(UpdateArtworkView, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context


class DeleteArtworkView(DeleteView):
    model = Artwork
    template_name = 'delete_artwork.html'
    #fields = '__all__'
    #fields = ('title', 'author', 'body')
    success_url = reverse_lazy('home')
    
    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(DeleteArtworkView, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context


class AddCategoryView(CreateView):
    model = Category
    #form_class = CategoryForm
    template_name = 'add_category.html'
    fields = '__all__'
    #fields = ('title', 'author', 'body')

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(AddCategoryView, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context


class AllCategoryView(ListView):
    model = Category
    #form_class = CategoryForm
    template_name = 'all_categories.html'
    fields = '__all__'
    #fields = ('title', 'author', 'body')
    
    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(AllCategoryView, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context

    

def CategoryView(request, cats):
    category_artworks = Artwork.objects.filter(category=cats.replace('-',' '))
    return render(request, 'categories.html', {'cats':cats.title().replace('-',' '), 'category_artworks':category_artworks})

def LikeView(request, pk):
    post = get_object_or_404(Artwork, id=request.POST.get('artwork_id'))
    post.likes.add(request.user)
    return HttpResponseRedirect(reverse('artwork-detail', args=[str(pk)]))



    