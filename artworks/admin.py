from django.contrib import admin
from .models import Artwork , Category, Profile

# Register your models here.
admin.site.register(Artwork)
admin.site.register(Category)
admin.site.register(Profile)