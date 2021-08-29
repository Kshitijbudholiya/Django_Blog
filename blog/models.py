from django.db.models.base import Model
from django.db.models.fields import DateField
from os import name
from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class blog(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100 ,default="")
    desc = RichTextField(default="")
    image = models.ImageField(default="")
    date = models.DateTimeField()
    posted_by = models.CharField(max_length=100, default="Kshitij Budholiya")
    # Display the title in admin page
    def __str__(self):
        return self.title

class contact(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100 ,default="")
    desc = models.TextField(default="")
    email = models.EmailField(max_length=200, default="")
    phone = models.CharField(max_length=20, default="")
    #display name in admin page
    def __str__(self):
        return self.name

class comme(models.Model):
    id = models.AutoField(primary_key=True)
    postid = models.CharField(max_length=1000, default="")
    name = models.CharField(max_length=100, default="")
    comment = models.TextField(default="")
    #display name in admin panel
    def __str__(self):
        return self.name