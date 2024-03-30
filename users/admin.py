from django.contrib import admin
from users.models import User

# Register your models here.

class UsersAdmin(admin.ModelAdmin):
  list_display = ("first_name", "last_name", "password",)

admin.site.register(User, UsersAdmin)
