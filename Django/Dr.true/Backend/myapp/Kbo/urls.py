from django.urls import path
from myapp.kbo import views

urlpatterns = [
    path('', view=views.score_board, name='score_board')
]