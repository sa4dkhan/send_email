from django.urls import path
from ajax_app import views

urlpatterns = [
    path('', views.ajax_form, name='ajax_form')
]