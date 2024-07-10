from rest_framework import serializers

from apps.notifications.models import SentNotification


class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = SentNotification
        fields = ('status', 'delivery_time',)
