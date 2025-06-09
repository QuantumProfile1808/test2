from django.urls import path
from .views import RoomView, CreateRoomView, index, getRoomView, JoinRoom, UserinRoom, LeaveRoom

urlpatterns = [
    path('room/', RoomView.as_view()), # Endpoint to create a room
    path('', index),
    path('create-room/', CreateRoomView.as_view()), # Endpoint to create a room
    path('get-room/', getRoomView.as_view()), # Endpoint to get a room by code
    path('join-room/', JoinRoom.as_view()), # Endpoint to join a room by code
    path('user-in-room/', UserinRoom.as_view()), # Endpoint to check if user is in a room
    path('leave-room/', LeaveRoom.as_view()), # Endpoint to leave a room
    
  ]
