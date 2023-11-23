from app2.views import *
from django.urls import path

app_name='app2_urls'

urlpatterns=[
    path('contact/',contact,name='contact')
]