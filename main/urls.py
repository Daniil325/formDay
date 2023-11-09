from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='main_page'),
    path('success_page/', success_page, name='success_page'),
]
