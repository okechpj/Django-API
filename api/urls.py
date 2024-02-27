from django.contrib import admin
from django.urls import path
from . import views
from .views import ApiUser

urlpatterns = [
    path('user/', ApiUser.as_view()),
    path('user/<int:id>/', views.one_user_api),
]