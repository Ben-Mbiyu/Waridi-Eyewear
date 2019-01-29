from django.shortcuts import render
from django.contrib.auth.models import User, Group
from .models import *
from rest_framework import viewsets
from .serializers import UserSerializer,ProductSerializer

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed and edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ProductViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows products to be viewed and created.
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
