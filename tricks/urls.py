from django.urls import path
from .views import user_tricks, add_new_trick

app_name = "tricks"
urlpatterns = [
    path('', user_tricks, name="user_tricks"),
    path('add', add_new_trick, name="add_new_trick"),
]
