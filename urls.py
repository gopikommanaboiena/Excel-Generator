# xls_app/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('generate_xls/', views.generate_xls, name='generate_xls'),
]

