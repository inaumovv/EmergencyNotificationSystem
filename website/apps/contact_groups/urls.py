from django.urls import path

from apps.contact_groups import views

app_name = 'contact_groups'

urlpatterns = [
    path('', views.AddContactGroupView.as_view(), name='index'),
    path('add/', views.AddContactGroupView.as_view(), name='add'),
    path('delete/<int:pk>/', views.DeleteContactGroupView.as_view(), name='delete'),
    path('edit/<int:pk>/', views.EditContactGroupView.as_view(), name='edit'),
]