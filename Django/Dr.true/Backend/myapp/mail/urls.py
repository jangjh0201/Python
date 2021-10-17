from django.urls import path
from myapp.mail import views

urlpatterns = [
    path('', view=views.getDriver, name='score_board')
]