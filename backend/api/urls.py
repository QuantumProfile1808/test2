from django.urls import path
from .views import RoomView, CreateRoomView, index

urlpatterns = [
    path('room/', RoomView.as_view()), # Endpoint to create a room
    path('', index),
    path('create-room/', CreateRoomView.as_view()) # Endpoint to create a room
      # Main and Void view of the StockSys API 
]
