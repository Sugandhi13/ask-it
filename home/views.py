from django.shortcuts import render
from django.views import generic
from .models import Ask

# Create your views here.
class AskitList(generic.ListView):
    model = Ask
