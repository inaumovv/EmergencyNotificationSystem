from django import forms

from apps.contact_groups.models import ContactGroup
from apps.message_templates.models import MessageTemplate
from apps.notifications.models import NotificationTemplate


class NotificationTemplateForm(forms.ModelForm):
    class Meta:
        model = NotificationTemplate
        fields = ('name', 'contact_group', 'message_template')

