from django.shortcuts import render
from .serializers import UserSerializer, CoffeeSerializer
from django.contrib.auth.models import User
from .models import Menu
from rest_framework import viewsets

# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class MenuViewSet(viewsets.ModelViewSet):
    queryset = Menu.objects.all()
    serializer_class = CoffeeSerializer