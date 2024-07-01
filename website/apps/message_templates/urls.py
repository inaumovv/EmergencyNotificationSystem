from django.urls import path

from apps.message_templates import views

app_name = 'message_templates'

urlpatterns = [
    path('', views.AddMessageTemplateView.as_view(), name='index'),
    path('add/', views.AddMessageTemplateView.as_view(), name='add'),
    path('delete/<int:pk>', views.DeleteMessageTemplateView.as_view(), name='delete'),
    path('edit/<int:pk>', views.EditMessageTemplateView.as_view(), name='edit'),
]