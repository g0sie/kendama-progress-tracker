from django.urls import path

from .views import register, email_verification


urlpatterns = [
    path('', register, name='register'),
    path('activate/<uidb64>/<token>', email_verification, name='activate')
]
