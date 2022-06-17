from django.urls import path
from .views import *

urlpatterns = [
    # Base URL
    path('pingpong', PingPong.as_view()),
]