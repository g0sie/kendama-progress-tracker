from django.contrib import admin

from .models import Tutorial, Author, Playlist


@admin.register(Tutorial)
class TutorialAdmin(admin.ModelAdmin):
    list_display = ['trick', 'author', 'created', 'modified']
    list_filter = ['author']


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    pass


@admin.register(Playlist)
class PlaylistAdmin(admin.ModelAdmin):
    list_display = ['author', 'name']
