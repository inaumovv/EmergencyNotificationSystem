from django.contrib import admin

from apps.notifications.models import SentNotification, NotificationTemplate


@admin.register(SentNotification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ('id', 'status',)


@admin.register(NotificationTemplate)
class NotificationTemplateAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'contact_group', 'message_template')
