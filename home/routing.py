from django.urls import path, re_path
from . import consumer

websocket_urlpatterns = [
    # path('ws/sc/', consumer.ParkingLotConsumer.as_asgi()),
    re_path(r'ws/sc/(?P<groupid>\w+)/$', consumer.ParkingLotConsumer.as_asgi()),
]
