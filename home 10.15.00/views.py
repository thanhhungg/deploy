from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics
from .models import users
from .serializes import UserSerializer

# Create your views here.

def hello(request):
    return HttpResponse("Hello World")

def user_list(request):
    user = users.objects.all()
    return render(request, 'home/index.html', {'users': user})

class CreateUserView(generics.CreateAPIView):
    queryset = users.objects.all()
    serializer_class = UserSerializer
