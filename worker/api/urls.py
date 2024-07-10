from django.urls import path

from api import views

app_name = 'api'

urlpatterns = [
    path('check/', views.CheckResponseView.as_view(), name='check')
]