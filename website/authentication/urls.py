from django.urls import path
from . import views
urlpatterns = [
    path('register/', views.signup_view, name='register'),
    path('home/', views.home_view, name='home')
]