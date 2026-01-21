from django.contrib import admin
from .models import Contacts, ContactsLocation

@admin.register(Contacts)
class ContactsAdmin(admin.ModelAdmin):
	list_display = ['telephone', 'e_mail', 'image', 'details', 'name']

@admin.register(ContactsLocation)
class ContactsLocationAdmin(admin.ModelAdmin):
	list_display = ['title', 'name', 'map_url']