from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),

    path(
        'recuperar-senha/',
        views.solicitar_recuperacao,
        name='solicitar_recuperacao'
    ),
]