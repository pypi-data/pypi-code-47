from django.contrib import admin

from .models import Track17Country, Track17Carrier

__all__ = (
    'Track17CountryAdmin',
    'Track17CarrierAdmin'
)


@admin.register(Track17Country)
class Track17CountryAdmin(admin.ModelAdmin):
    list_display = [
        'key',
        'title'
    ]
    search_fields = [
        'key',
        'title'
    ]


@admin.register(Track17Carrier)
class Track17CarrierAdmin(admin.ModelAdmin):
    list_display = [
        'key',
        'title',
        'country',
        'url',
        'can_track'
    ]
    list_filter = [
        'country',
        'can_track'
    ]
    list_select_related = [
        'country'
    ]
    search_fields = [
        'key',
        'title',
        'url'
    ]
