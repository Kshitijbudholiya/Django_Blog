from os import name
from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class blog(models.Model):
    id = models.AutoField
    title = models.CharField(max_length=100 ,default="")
    desc = RichTextField(default="")
    image = models.ImageField(default="")
    date = models.DateTimeField()
    posted_by = models.CharField(max_length=100, default="")

    # Display the title in admin page
    def __str__(self):
        return self.title

class contact(models.Model):
    user_id = models.AutoField
    name = models.CharField(max_length=100 ,default="")
    desc = models.TextField(default="")
    email = models.EmailField(max_length=200, default="")
    phone = models.CharField(max_length=20, default="")

    #display name in admin page
    def __str__(self):
        return self.name