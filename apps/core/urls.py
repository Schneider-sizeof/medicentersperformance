from django.urls import path
from django.utils.translation import gettext_lazy as _
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.home, name='home'),
    path(_('about/'), views.about, name='about'),
]
