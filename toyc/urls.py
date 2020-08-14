from django.urls import path

from . import views

urlpatterns = [
    path('', views.dashboard, name='index'),
    path('records/', views.records, name='records'),
]