from app1.views import *
from django.urls import path

app_name='app1_urls'

urlpatterns=[
    path('index/',index,name='index')
]