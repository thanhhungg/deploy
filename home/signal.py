from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import *
from .consumer import ParkingLotConsumer
@receiver([post_save, post_delete], sender=parking_lot)
def parking_lot_changed(sender, instance, **kwargs):
    # Gửi sự kiện cho consumer khi có sự thay đổi trong trạng thái của bãi đỗ xe
    data = [{'name': lot.name, 'status': lot.status} for lot in parking_lot.objects.all()]
    ParkingLotConsumer().update_parking_lot_status({'data': data})
