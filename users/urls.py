from django.urls import path
from users import views

urlpatterns = [
    path("", views.users_index, name="users_index"),
    path("<int:id>/", views.users_show, name="users_detail"),
]