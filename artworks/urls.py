from django.urls import path
from . import views
from .views import ArtworkView, HomeView , ArtworkDetailView, AddArtworkView, UpdateArtworkView, DeleteArtworkView , AddCategoryView, CategoryView, AllCategoryView
urlpatterns = [
    #path('', views.home , name="home"),
    path('', HomeView.as_view(), name="home"),
    path('artwork/<int:pk>', ArtworkDetailView.as_view(), name="artwork-detail"),
    path('artworks/', ArtworkView.as_view(), name="artworks"),
    path('add_artwork/' , AddArtworkView.as_view(), name="add-artwork"),
    path('artwork/edit/<int:pk>' , UpdateArtworkView.as_view(), name="update-artwork"),
    path('artwork/<int:pk>/delete' , DeleteArtworkView.as_view(), name="delete-artwork"),
    path('all_categories/' , AllCategoryView.as_view(), name="all-category"),
    path('add_category/' , AddCategoryView.as_view(), name="add-category"),
    path('category/<str:cats>/' , CategoryView, name="category"),

]