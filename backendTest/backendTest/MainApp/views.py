from django.shortcuts import render
from MainApp.models import *
def SomeFunc():
    return "Ivan"
def Main (request):
    notes = Note.objects.all()
    return render(request,'index.html',{"notes":notes,"isFirst":True})

def Main1(request,name):
    author = Author.objects.get(name=name)
    return render(request,"index.html",{"author":author,"isFirst":False})

