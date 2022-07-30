from django.urls import path

from . import views

app_name = "tricks"
urlpatterns = [
    path('', views.user_tricks, name="user_tricks"),
    path('add', views.add_new_trick, name="add_new_trick"),
    path('add/list', views.add_from_list, name="add_from_list"),
    path('draw', views.draw_a_trick, name="draw"),
    path('<int:user_trick_id>/delete', views.delete_trick, name="delete"),
]
