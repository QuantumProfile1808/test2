from django.shortcuts import render
from rest_framework import generics
from .serializers import RootSerializer
from .models import Room

def index(request, *args, **kwargs):
    return render(request, 'frontend/index.html')
