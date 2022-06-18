from django.urls import path
from .views import *

urlpatterns = [
    path('', Welcome.as_view()),
    
    path('pingpong/', PingPong.as_view()),
]