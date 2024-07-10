from django import forms
from django.core.exceptions import ValidationError
from django.core.files import File
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.utils.deconstruct import deconstructible

from apps.contact_groups.models import ContactGroup


@deconstructible
class FileValidator:
    code = 'russian'

    def __call__(self, value: File):
        filename: str = value.name
        self.validate_file_format(filename)

    def validate_file_format(self, filename: str):
        if not filename.endswith('.xlsx'):
            raise ValidationError('Поддерживаются только .xlsx файлы.', code=self.code)


class ContactGroupForm(forms.ModelForm):
    file = forms.FileField(validators=[FileValidator()])
    filename = forms.CharField(required=False)

    def save(self, commit=True):
        instance = super().save(commit=False)
        file: InMemoryUploadedFile = self.cleaned_data['file']
        instance.filename = file.name
        if commit:
            instance.save()
        return instance

    class Meta:
        model = ContactGroup
        fields = ('group_name', )
