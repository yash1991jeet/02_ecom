from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request, 'blog/index.html')  # blog/index.html is basically path of html file we need in tempelates folder

