from django.urls import path
from . import views

urlpatterns = [

    path(
        '',
        views.dashboard_aluno,
        name='dashboard_aluno'
    ),

]