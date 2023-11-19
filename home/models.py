from django.db import models

class users(models.Model):
    name = models.CharField(max_length=40)
    account = models.CharField(max_length=40)
    password = models.CharField(max_length=40)
    lc_number = models.CharField(max_length=40)
    age = models.IntegerField()
    email = models.EmailField()

class parking_lot(models.Model):
    name = models.CharField(max_length=40)
    status = models.IntegerField()


