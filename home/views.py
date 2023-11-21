
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics
from .models import *
from .serializes import UserSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from channels.layers import get_channel_layer
from .consumer import ParkingLotConsumer
import json
# Create your views here.

def hello(request):
    return HttpResponse("Hello World")

def user_list(request):
    user = users.objects.all()
    return render(request, 'home/index.html', {'users': user})

def manage(request):
    return render(request, 'home/manage.html')

class CreateUserView(generics.ListCreateAPIView):
    queryset = users.objects.all()
    serializer_class = UserSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

class LoginView(APIView):
    def post(self, request, format=None):
        username = request.data.get('username')
        password = request.data.get('password')
        user = users.objects.filter(account=username, password=password).first()
        if user:
            serializer = UserSerializer(user)
            return Response(serializer.data, status=200)
        else:
            return Response({'error': 'Invalid credentials'}, status=400)

class update_parkinglot(APIView):
    def post(self, request, format=None):
        name = request.data.get('name') 
        status = request.data.get('status')
        # return HttpResponse("OK")
        try:
            pl = parking_lot.objects.get(name=name)
            pl.status = status
            pl.save()
            # data = [{'name': lot.name, 'status': lot.status} for lot in parking_lot.objects.all()]
            # ParkingLotConsumer().update_parking_lot_status({'data': data})
            return Response({'success': 'Done'}, status=200)
            # return render(request, 'home/manage.html')
            # return JsonResponse({'message': 'Cập nhật trạng thái thành công'})
        except parking_lot.DoesNotExist:
            return Response({'error': 'Yêu cầu không hợp lệ'}, status=400)
            # return JsonResponse({'error': 'Không tìm thấy lớp thực thể ParkingLot với tên đã cho'}, status=404)
