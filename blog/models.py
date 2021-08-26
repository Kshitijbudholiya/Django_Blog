from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class blog(models.Model):
    title = models.CharField(max_length=100 ,default="")
    desc = RichTextField(default="")
    image = models.ImageField(default="")
    date = models.DateTimeField()
    posted_by = models.CharField(max_length=100, default="")

    # Display the title in admin page
    def __str__(self):
        return self.title
