from django.urls import path
from .views import *

urlpatterns = [
    path('pingpong/', PingPong.as_view()),
]