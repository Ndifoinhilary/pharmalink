from django.contrib import admin

from base.models import Contact, Pharmacy, Drug, Event, Staff

# Register your models here.

admin.site.site_header = 'SheiPharmalink'


@admin.register(Pharmacy)
class PharmacyAdmin(admin.ModelAdmin):
    list_display = ['name_of_pharmacy',
                    'pharmacy_phone_number', 'address_or_location']


@admin.register(Drug)
class DrugAdmin(admin.ModelAdmin):
    list_display = ['name_of_drug',
                    'price', 'is_available']


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_at']


admin.site.register(Staff)

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'email']