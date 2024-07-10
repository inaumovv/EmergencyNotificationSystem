from apps.contact_groups.models import ContactGroup
from services.tests.test_settings import Settings


class TestContactGroupsViews(Settings):
    def setUp(self):
        super().setUp()
        self.contact_group = ContactGroup.objects.create(group_name='test edit', filename='test')

    def test_add_view(self):
        form_data = {'group_name': 'Test Group', 'file': self.valid_file}
        response = self.authorized_client.post('/contact-groups/add/', data=form_data)
        self.assertRedirects(response, '/contact-groups/')
        contact_group = ContactGroup.objects.filter(group_name='Test Group')
        self.assertTrue(contact_group.exists())

    def test_edit_view(self):
        form_data = {'group_name': 'updated group', 'file': self.valid_file_2}
        response = self.authorized_client.post(f'/contact-groups/edit/{self.contact_group.id}/', data=form_data)
        self.assertRedirects(response, '/contact-groups/')
        self.assertTrue(ContactGroup.objects.filter(group_name='updated group').exists())

    def test_delete_view(self):
        response = self.authorized_client.post(f'/contact-groups/delete/{self.contact_group.id}/')
        self.assertRedirects(response, '/contact-groups/')
        self.assertFalse(ContactGroup.objects.filter(group_name='updated group').exists())


