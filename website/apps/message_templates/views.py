from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, DeleteView, UpdateView

from apps.message_templates.forms import MessageTemplateForm
from apps.message_templates.models import MessageTemplate
from services.mixins import ContextDataMixin

PAGE = 'message_templates.html'


class AddMessageTemplateView(LoginRequiredMixin, CreateView):
    form_class = MessageTemplateForm
    template_name = PAGE
    success_url = reverse_lazy('message_templates:index')


class DeleteMessageTemplateView(LoginRequiredMixin, DeleteView):
    model = MessageTemplate
    template_name = PAGE
    success_url = reverse_lazy('message_templates:index')


class EditMessageTemplateView(LoginRequiredMixin, UpdateView):
    model = MessageTemplate
    fields = ('name', 'text')
    template_name = PAGE
    success_url = reverse_lazy('message_templates:index')
