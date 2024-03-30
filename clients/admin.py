from django.contrib import admin
from clients.models import Client

# Register your models here.
class ClientsAdmin(admin.ModelAdmin):
  list_display = ("name", "address", "phone_no", 'gst_no')

admin.site.register(Client, ClientsAdmin)
