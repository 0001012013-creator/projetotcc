from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard_adm, name='dashboard_adm'),
]