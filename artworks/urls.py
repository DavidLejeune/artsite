from django.urls import path
from . import views
#from .views import PaintingDetailView, PaintingView, HomeView, AddPaintingView, UpdatePaintingView, DeletePaintingView, AddCategoryView, CategoryView
urlpatterns = [
    path('', views.home , name="home"),
    #path('', HomeView.as_view(), name="home"),
    #path('painting/<int:pk>', PaintingDetailView.as_view(), name="painting-detail"),
    #path('paintings/', PaintingView.as_view(), name="paintings"),
    #path('add_painting/' , AddPaintingView.as_view(), name="add-painting"),
    #path('painting/edit/<int:pk>' , UpdatePaintingView.as_view(), name="update-painting"),
    #path('painting/<int:pk>/delete' , DeletePaintingView.as_view(), name="delete-painting"),
    #path('add_category/' , AddCategoryView.as_view(), name="add-category"),
    #path('category/<str:cats>/' , CategoryView, name="category"),

]