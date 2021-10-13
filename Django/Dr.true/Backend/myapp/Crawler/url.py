from django.urls import path
from django import views

urlpatterns = [
    path('', view=views.score_board, name='score_board')
]