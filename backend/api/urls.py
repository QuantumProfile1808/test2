from django.urls import path
from .views import index

urlpatterns = [
    path('', index), # Main and Void view of the StockSys API 
]
