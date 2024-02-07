from django.shortcuts import render
from django.views import generic
from .models import Ask

# Create your views here.
class AskList(generic.ListView):
    queryset = Ask.objects.all()
    template_name = "askit_list.html"
