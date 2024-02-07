from . import views
from django.urls import path

urlpatterns = [
    path('', views.AskList.as_view(), name='home'),
]