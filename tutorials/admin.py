from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from .models import Tutorial, Author, Playlist


class NullTrickFilter(admin.SimpleListFilter):
    title = _('to add')

    parameter_name = 'trick'

    def lookups(self, request, model_admin):
        return (
            ('null', _('tutorials to add')),
        )

    def queryset(self, request, queryset):
        if self.value() == 'null':
            return queryset.filter(
                trick__name='null'
            )


@admin.register(Tutorial)
class TutorialAdmin(admin.ModelAdmin):
    list_display = ['trick', 'yt_title', 'author', 'created', 'modified']
    list_filter = ['author', NullTrickFilter]


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    pass


@admin.register(Playlist)
class PlaylistAdmin(admin.ModelAdmin):
    list_display = ['author', 'name']
