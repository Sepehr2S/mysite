from django.contrib.auth.models import User
from django.db import models

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    image = models.ImageField(upload_to='profiles/', default='profiles/default.jpg')
    name = models.CharField(max_length=255, blank=True)
    email = models.EmailField(blank=True)

    def save(self, *args, **kwargs):
        # هماهنگی ایمیل و نام با مدل User
        if self.email:
            self.user.email = self.email
        if self.name:
            self.user.first_name = self.name
        self.user.save()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Profile of {self.user.username}"
