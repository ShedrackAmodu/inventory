from django.urls import path
from . import views

urlpatterns = [
    path('', views.activity_list, name='activity_list'),
    path('add/', views.activity_add, name='activity_add'),
    path('complete/<int:activity_id>/', views.mark_completed, name='mark_completed'),
]

