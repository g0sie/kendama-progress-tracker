from django.contrib import admin

from .models import Trick, Tutorial


@admin.register(Tutorial)
class TutorialAdmin(admin.ModelAdmin):
    list_display = ['trick', 'author', 'created', 'modified']
    list_filter = ['author']


@admin.register(Trick)
class TrickAdmin(admin.ModelAdmin):
    list_display = ['name', 'difficulty', 'official', 'created', 'modified']
    search_fields = ['name']
    list_filter = ['official', 'difficulty']
