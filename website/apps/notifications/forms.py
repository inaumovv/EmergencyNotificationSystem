from django import forms

from apps.notifications.models import NotificationTemplate


class NotificationTemplateForm(forms.ModelForm):
    class Meta:
        model = NotificationTemplate
        fields = ('name', 'contact_group', 'message_template')

