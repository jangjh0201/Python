from django.urls import path
from myapp.Crawler import views

urlpatterns = [
    path('', view=views.score_board, name='score_board')
]