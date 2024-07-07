from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name="home"),
    path('create/', create_page, name="create"),
    path('update/<int:id>/', update_page, name="update"),
    path('delete/<int:id>/', delete_page, name="delete"),
]