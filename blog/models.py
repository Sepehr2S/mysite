from django.db import models
from django.contrib.auth.models import User
from taggit.managers import TaggableManager
from accounts.models import Profile
# Create your models here.

class Location(models.Model):
    name = models.CharField(max_length=255)
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=255)
    content = models.TextField()
    tags = TaggableManager()
    counted_views = models.IntegerField(default=0)
    status = models.BooleanField(default=False)
    published_date = models.DateTimeField(null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    category = models.ManyToManyField(Category)
    locations = models.ManyToManyField(Location, related_name='posts',blank=True)
    image = models.ImageField(upload_to='blog/', default="blog/default.jpg")

    class Meta:
        ordering = ['-created_date']

    def __str__(self):
        return self.title

class GalleryPic(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='gallery_pics')
    image = models.ImageField(upload_to='gallery/')
    title = models.CharField(max_length=255)
    content = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=255)
    email = models.EmailField() 
    subject = models.CharField(max_length=255)  
    message = models.TextField(max_length=255)
    created_date = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)
    
    def __str__(self):
        return self.name
