from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=120)
    mark = models.IntegerField(null=True)

class Note(models.Model):
    author = models.OneToOneField(Author,on_delete=models.CASCADE)
    name = models.CharField(max_length=120)
    text = models.TextField()