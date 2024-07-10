from django.contrib.auth import get_user_model
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase, Client
from rest_framework.test import APIClient

User = get_user_model()


class Settings(TestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.invalid_file = SimpleUploadedFile('testfile.xlsx.txt', b'test content')
        cls.valid_file = SimpleUploadedFile('testfile.xlsx', b'test content')
        cls.valid_file_2 = SimpleUploadedFile('testfile2.xlsx', b'test')

    def setUp(self):
        super().setUp()
        self.user = User.objects.create_user(username='Name', password='Password')
        self.authorized_client = Client()
        self.authorized_client.force_login(self.user)
        self.api_client = APIClient()
