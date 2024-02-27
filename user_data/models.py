from django.db import models

# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=20)
    year = models.IntegerField()
    slug = models.SlugField(default = None)

    def __str__ (self):
        return self.title


class User(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=20)
    age = models.IntegerField()
    location = models.CharField(max_length=100)
    slug = models.SlugField(default = None)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, blank=True, null=True)
    
    def __str__(self):
        return self.name