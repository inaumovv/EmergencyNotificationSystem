from django.core.exceptions import ValidationError

from apps.contact_groups.forms import FileValidator, ContactGroupForm
from services.tests.test_settings import Settings


class TestContactGroupsForm(Settings):
    validator = FileValidator()

    def test_file_validator(self):
        with self.assertRaises(ValidationError):
            self.validator.__call__(self.invalid_file)

    def test_form_save(self):
        form_data = {'group_name': 'Test Group'}
        post_data = {'file': self.valid_file}
        form = ContactGroupForm(data=form_data, files=post_data)
        self.assertTrue(form.is_valid())
        contact_group = form.save(commit=False)
        self.assertEqual(contact_group.group_name, 'Test Group')
        self.assertEqual(contact_group.filename, 'testfile.xlsx')
