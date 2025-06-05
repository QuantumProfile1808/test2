from django.urls import path
from .views import index


urlpatterns = [
    path('', index),
    path('Page2/', index),  # Example additional path
    path('Page3/', index),  # Another example additional path
    path('room/<str:code>/', index), # Endpoint to get a room by code
    
]