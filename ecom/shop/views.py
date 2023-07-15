from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
    return render(request, 'shop/index.html')


def contact(request):
    return HttpResponse("Clicked ABOUTUS")


def tracker(request):
    return HttpResponse("Clicked tracker")


def search(request):
    return HttpResponse("Clicked search ")


def productView(request):
    return HttpResponse("Clicked productview")


def checkout(request):
    return HttpResponse("Clicked checkout")