from django.contrib import admin

from .models import Quotation, Source, Destination


# Register your models here.


@admin.register(Quotation)
class QuotationAdmin(admin.ModelAdmin):
    list_display = ['external_id', 'payer_id', 'mode', 'source', 'destination']


@admin.register(Source)
class SourceAdmin(admin.ModelAdmin):
    list_display = ['country_iso_code', 'currency', 'amount']


@admin.register(Destination)
class DestinationAdmin(admin.ModelAdmin):
    list_display = ['currency', 'amount']

