from django.db import models

# Create your models here.
class Client(models.Model):
  name = models.CharField(max_length=255)
  address = models.CharField(max_length=255)
  phone_no = models.IntegerField()
  gst_no = models.CharField(max_length=255)
  
