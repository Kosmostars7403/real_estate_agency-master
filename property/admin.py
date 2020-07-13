from django.contrib import admin
from .models import Flat, Сomplaint, Owner


class FlatAdmin(admin.ModelAdmin):
    search_fields = ['town', 'address', 'owner']
    readonly_fields = ['created_at']
    list_display = ['address', 'price', 'new_building', 'construction_year',
                    'town']
    list_editable = ['new_building']
    list_filter = ['new_building', 'has_balcony', 'rooms_number']
    raw_id_fields = ['liked_by']


class СomplaintAdmin(admin.ModelAdmin):
    raw_id_fields = ['user', 'flat']


class OwnerAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'phonenumber', 'phone_pure']
    raw_id_fields = ['own_flats']


admin.site.register(Flat, FlatAdmin)
admin.site.register(Сomplaint, СomplaintAdmin)
admin.site.register(Owner, OwnerAdmin)
