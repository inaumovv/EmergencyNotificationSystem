from datetime import datetime

from api.serializers import NotificationSerializer
from services.tests.test_settings import Settings


class TestSerializers(Settings):
    time = datetime.now()

    def test_serializer_save(self):
        data = {'status': 'доставлено', 'delivery_time': self.time}
        serializer = NotificationSerializer(data=data)
        self.assertTrue(serializer.is_valid())
        instance = serializer.save()
        self.assertEqual(instance.status, 'доставлено')
        self.assertEqual(instance.delivery_time, self.time.strftime('%Y-%m-%d %H:%M:%S'))
