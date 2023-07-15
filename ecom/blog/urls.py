# this file is not defualt. Contents are similar to urls.py from ecom folder
# link to this file is there in ecom.urls file which is default.

from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='BlogHome'),  # Here admin line is not there because admin is in ecom and not shop
]