from django.db import models

# Create your models here.
class User(models.Model):
  first_name = models.CharField(max_length=255)
  last_name = models.CharField(max_length=255)
  phone_no = models.IntegerField()
  password = models.CharField(max_length=255)
  otp = models.IntegerField()
