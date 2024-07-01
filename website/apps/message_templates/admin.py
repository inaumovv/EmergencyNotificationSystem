from django.contrib import admin

from apps.message_templates.models import MessageTemplate


@admin.register(MessageTemplate)
class MessageTemplateAdmin(admin.ModelAdmin):
    list_display = ('name', 'text')
    search_fields = ('name',)
    list_filter = ('name',)
    list_editable = ('text',)
