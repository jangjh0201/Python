from django.shortcuts import render
 
import requests
from bs4 import BeautifulSoup
from django.http import HttpResponse

def score_board(request):
    