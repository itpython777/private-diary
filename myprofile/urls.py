from django.urls import path
from . import views

app_name = 'myprofile'

urlpatterns = [
    path('top', views.top, name='top'),
]