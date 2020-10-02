from django.contrib import admin
from .models import Contact, Subscribe
# Register your models here.


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject', 'message', 'contact_date']
    list_filter = ['contact_date']


@admin.register(Subscribe)
class SubscribeAdmin(admin.ModelAdmin):
    list_display = ['email', 'date']
    list_filter = ['date']