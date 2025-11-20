from django.contrib import admin
from django.urls import path, include
from flights.views import *

urlpatterns = [
    path('flight',Airlines.as_view())
]