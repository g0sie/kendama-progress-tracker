from django.contrib import admin

from .models import Trick, Tutorial, UserTrick


@admin.register(Tutorial)
class TutorialAdmin(admin.ModelAdmin):
    list_display = ['trick', 'author', 'created', 'modified']
    list_filter = ['author']


@admin.register(Trick)
class TrickAdmin(admin.ModelAdmin):
    list_display = ['name', 'difficulty', 'official', 'created', 'modified']
    search_fields = ['name']
    list_filter = ['official', 'difficulty']


@admin.register(UserTrick)
class UserTrickAdmin(admin.ModelAdmin):
    list_display = ['user', 'trick', 'land_count', 'added', 'passed']
    search_fields = ['user', 'trick']
