from django.shortcuts import render

def main(request):
    return render(request,'main.html')

def redirect(request):
    return render(request,'main.html',)

def catalog(request):
    return render(request,'catalog.html')
