from django.urls import path
from clients import views

urlpatterns = [
    path("", views.clients_index, name="client_index"),
    path("<int:id>/", views.clients_show, name="client_detail"),
]