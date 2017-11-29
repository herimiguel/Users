from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User


# Create your views here.

def index(request):    
    return render(request, 'my_app/index.html')
