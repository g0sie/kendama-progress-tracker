from django.contrib import admin

from .models import Trick, UserTrick


@admin.register(Trick)
class TrickAdmin(admin.ModelAdmin):
    list_display = ['name', 'difficulty', 'official', 'created', 'modified']
    search_fields = ['name']
    list_filter = ['official', 'difficulty']


@admin.register(UserTrick)
class UserTrickAdmin(admin.ModelAdmin):
    list_display = ['user', 'trick', 'land_count', 'added', 'passed']
    search_fields = ['user', 'trick']
