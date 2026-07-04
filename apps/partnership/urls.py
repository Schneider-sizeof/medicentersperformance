from django.urls import path
from . import views

app_name = 'partnership'

urlpatterns = [
    path('', views.partnership_page, name='partnership'),
    path('merci/', views.partnership_success, name='success'),
]
