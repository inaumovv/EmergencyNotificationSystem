from django.urls import path

from api import views

app_name = 'api'

urlpatterns = [
    path('update/<int:pk>/', views.NotificationUpdateAPIView.as_view(), name='update'),
    path('return-to-queue/', views.ReturnNotificationToQueueAPIView.as_view(), name='return')
]
