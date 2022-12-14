from django.contrib import admin
from .models import Controllers, OneWire, Rele


@admin.register(Controllers)
class ControllersAdmin(admin.ModelAdmin):
    list_display = ['contr_name', 'id']


@admin.register(OneWire)
class OneWireAdmin(admin.ModelAdmin):
    list_display = ['onewire_time', 'onewire_name', 'onewire_value']


@admin.register(Rele)
class ReleAdmin(admin.ModelAdmin):
    list_display = ['rele_time', 'rele_num', 'rele_satus']
