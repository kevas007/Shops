from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Category(models.Model):
    tile = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50)
    
    class Meta:
        verbose_name_plural = 'Categories'
    def __str__(self) :
        return  self.tile

class Product(models.Model):
    user = models.ForeignKey(User, related_name='products', on_delete=models.CASCADE,)
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    tile = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50)
    description= models.TextField(blank=True, max_length=255)
    price = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at=  models.DateTimeField(auto_now=True)
    def __str__(self) :
        return  self.tile