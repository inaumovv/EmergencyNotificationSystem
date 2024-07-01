from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.urls import reverse_lazy
from django.views.generic import FormView, DeleteView, UpdateView, CreateView

from apps.contact_groups.forms import ContactGroupForm
from apps.contact_groups.models import ContactGroup
from apps.contact_groups.tasks import upload_file, delete_file, update_file
from services.repositories.contact_groups_repository import ContactGroupsRepository

PAGE = 'contact_groups.html'


class AddContactGroupView(CreateView, LoginRequiredMixin):
    template_name = PAGE
    form_class = ContactGroupForm
    success_url = reverse_lazy('contact_groups:index')

    def form_valid(self, form):
        new_object = form.save()
        file: InMemoryUploadedFile = form.cleaned_data['file']
        s3_object_name: int = new_object.id
        upload_file.delay(file=file.read(), s3_object_name=s3_object_name)
        return super().form_valid(form)


class DeleteContactGroupView(LoginRequiredMixin, DeleteView):
    repo: ContactGroupsRepository = ContactGroupsRepository
    template_name = PAGE
    success_url = reverse_lazy('contact_groups:index')
    model: ContactGroup = ContactGroup

    def form_valid(self, form):
        s3_object_name: int = self.object.id
        delete_file.delay(s3_object_name)
        return super().form_valid(form)


class EditContactGroupView(LoginRequiredMixin, UpdateView):
    model = ContactGroup
    repo: ContactGroupsRepository = ContactGroupsRepository
    template_name = PAGE
    success_url = reverse_lazy('contact_groups:index')
    form_class: ContactGroupForm = ContactGroupForm

    def form_valid(self, form):
        form.save()
        file: InMemoryUploadedFile = form.cleaned_data['file']
        s3_object_name: int = self.object.id
        update_file.delay(file.read(), s3_object_name)
        return super().form_valid(form)

