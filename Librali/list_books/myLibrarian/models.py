from django.db import models
#
# class Books(models.Model):
#     id = models.AutoField(primary_key=True)
#     image = models.CharField(max_length=1287)
#     title = models.CharField(56)
#     author = models.CharField(100)
#     description = models.TextField()
#     status = models.BooleanField()
#     quantity = models.IntegerField()
#
#
# class User(models.Model):
#     id = models.AutoField(primary_key=True)
#     cellPhoneNumber = models.IntegerField(max_length=10)
#
# class Rent(models.Model):
#     id = models.AutoField(primary_key=True)
#     rentStart = models.DateTimeField(null=True,blank=True)
#     rentEnd = models.DateTimeField(null=True,blank=True)
#     status = models.CharField(max_length=25)
#     user = models.OneToOneField(User)
#     books = models.ManyToManyField(Books)

