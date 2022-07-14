from django.contrib import admin

from .models import Tutorial, Author


@admin.register(Tutorial)
class TutorialAdmin(admin.ModelAdmin):
    list_display = ['trick', 'author', 'created', 'modified']
    list_filter = ['author']


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    pass
