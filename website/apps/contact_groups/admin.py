from django.contrib import admin

from apps.contact_groups.models import ContactGroup


@admin.register(ContactGroup)
class ContactGroupAdmin(admin.ModelAdmin):
    list_display = ('group_name', 'filename')
    search_fields = ('group_name', 'filename')
    list_filter = ('group_name', 'filename')
