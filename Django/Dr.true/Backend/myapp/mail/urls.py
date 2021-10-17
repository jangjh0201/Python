from django.urls import path
from myapp.mail import views

urlpatterns = [
    path('', view=views.main, name='main')
]