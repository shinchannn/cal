from django.urls import path

from . import views

urlpatterns = [
    path('', views.RecordsView.as_view(), name='index'),
]