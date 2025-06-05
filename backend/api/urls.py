from django.urls import path
from .views import RoomView, CreateRoomView, index, getRoomView

urlpatterns = [
    path('room/', RoomView.as_view()), # Endpoint to create a room
    path('', index),
    path('create-room/', CreateRoomView.as_view()), # Endpoint to create a room
    path('get-room/', getRoomView.as_view()), # Endpoint to get a room by code
  ]
