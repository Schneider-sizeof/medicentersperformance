from django.urls import path
from . import views

app_name = 'recruitment'

urlpatterns = [
    path('', views.careers, name='careers'),
    path('merci/', views.application_success, name='success'),
]
