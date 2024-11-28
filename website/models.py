from django.db import models

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=254)
    subject = models.CharField(max_length=50)
    message = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return '{}---{}'.format(self.subject, self.email)
    

class Newsletter(models.Model):
    email = models.EmailField(max_length=254)
    
    def __str__(self):
        return self.email