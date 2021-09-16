from django.urls import path

from .views import *


urlpatterns = [
    path('', Index.as_view(), name="Homepage"),
    path('login/register', Login.as_view(), name="Login/register")
]
