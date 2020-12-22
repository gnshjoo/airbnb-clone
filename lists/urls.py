from django.urls import path
from . import views

app_name = "lists"


urlpatterns = [
    path("add/<int:room_pl>", views.save_room, name="save-room")
]