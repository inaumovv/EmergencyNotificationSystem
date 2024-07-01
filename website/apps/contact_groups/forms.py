import uuid

from django import forms
from django.core.exceptions import ValidationError
from django.core.files import File
from django.utils.deconstruct import deconstructible

from apps.contact_groups.models import ContactGroup
from services.repositories.contact_groups_repository import ContactGroupsRepository


@deconstructible
class FileValidator:
    code = 'russian'

    def __call__(self, value: File):
        filename: str = value.name
        self.validate_file_format(filename)

    def validate_file_format(self, filename: str):
        if not filename.endswith('.xlsx') and not filename.endswith('.xls'):
            raise ValidationError('Поддерживаются только .xlsx и .xls файлы.', code=self.code)

    # ToDo сделать проверку содержимого файла, наличие всех нужных полей


class ContactGroupForm(forms.ModelForm):
    file = forms.FileField(validators=[FileValidator()])
    filename = forms.CharField(required=False)

    def save(self, commit=True):
        instance = super().save(commit=False)
        file = self.cleaned_data['file']
        instance.filename = file.name
        if commit:
            instance.save()
        return instance

    class Meta:
        model = ContactGroup
        fields = ('group_name', )
