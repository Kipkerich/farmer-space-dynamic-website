from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request,'index.html')

def post(request):
    return render(request,'single-post.html')


def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')
