from wsgiref.simple_server import demo_app
from django.urls import path
from .views import *

urlpatterns = [
    path('', showDemoPage, name='demoapp')
]
