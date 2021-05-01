from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date
from ckeditor.fields import RichTextField

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        #return reverse('painting-detail', args=(str(self.id)))
        return reverse('all-category')


class Artwork(models.Model):
    title = models.CharField(max_length=255)
    header_image = models.ImageField(null=True, blank=True, upload_to="images/")
    title_tag = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    #body = models.TextField()
    body = RichTextField(blank=True, null=True)
    snippet = models.CharField(max_length=255)
    artwork_date = models.DateField(auto_now_add=True)
    category = models.CharField(max_length=255, default='No category')
    likes = models.ManyToManyField(User, related_name='artwork_post')

    def total_likes(self):
        return self.likes.count()
    

    def __str__(self):
        return self.title + ' | ' + str(self.author)

    def get_absolute_url(self):
        return reverse('artwork-detail', args=[str(self.id)])

class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    bio = RichTextField(blank=True, null=True)
    #bio = models.TextField(blank=True, null=True)
    profile_pic = models.ImageField(null=True, blank=True, upload_to="images/profile/", default='images/profile/default-profile.png')
    website_url = models.CharField(max_length=255, blank=True, null=True)
    facebook_url = models.CharField(max_length=255, blank=True, null=True)
    instagram_url = models.CharField(max_length=255, blank=True, null=True)
    twitter_url = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return str(self.user)

    def get_absolute_url(self):
        return reverse('home')

