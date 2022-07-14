from django.urls import path
from .views import add_tutorials

app_name = "tutorials"
urlpatterns = [
    path('add/<int:number>', add_tutorials, name="add"),
]
