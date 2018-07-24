from django.urls import path

from .views import *


urlpatterns = [

 path('add_rss', add_rss),
]