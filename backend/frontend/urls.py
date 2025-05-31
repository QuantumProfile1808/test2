from django.urls import path
from .views import index

urlpatterns = [
    path('', index),
    path('page2/', index),  # Example additional path
    path('page3/', index),  # Another example additional path
    
]