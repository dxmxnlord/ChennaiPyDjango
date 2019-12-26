from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'personal/header.html',{"file":"home.html"})

def aboutme(request):
    return render(request,'personal/header.html',{"file":"aboutme2.html"})

