from django.contrib import admin

from .models import Trick


@admin.register(Trick)
class TrickAdmin(admin.ModelAdmin):
    list_display = ['name', 'difficulty', 'official']
    search_fields = ['name']
    list_filter = ['official', 'difficulty']
