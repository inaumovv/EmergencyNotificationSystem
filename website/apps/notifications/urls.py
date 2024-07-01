from django.urls import path

from apps.notifications import views

app_name = 'notifications'

urlpatterns = [
    path('', views.AddNotificationTemplateView.as_view(), name='templates_index'),
    path('add/', views.AddNotificationTemplateView.as_view(), name='templates_add'),
    path('delete/<int:pk>/', views.DeleteNotificationTemplateView.as_view(), name='templates_delete'),
    path('edit/<int:pk>/', views.EditNotificationTemplateView.as_view(), name='templates_edit'),
    path('send/', views.SendNotificationsView.as_view(), name='templates_send'),
    path('sent-notifications/', views.SentNotificationsView.as_view(), name='sent_index'),
]
