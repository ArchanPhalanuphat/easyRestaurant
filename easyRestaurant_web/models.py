from django.db import models

# Create your models here.
class Post(models.Model):
    name = models.CharField(max_length=200)
    desc = models.TextField()

class Menu(models.Model):
    name = models.CharField(max_length=20)
    genre = models.CharField(max_length=20)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    status = models.BooleanField(default=False)
    image = models.ImageField(upload_to='image_menu', null=True, blank=True)
