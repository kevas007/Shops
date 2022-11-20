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