from django.urls import path
from .views import user_tricks

app_name = "tricks"
urlpatterns = [
    path('', user_tricks, name="user_tricks"),
]
