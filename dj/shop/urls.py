from django.urls import path
from .views import *


urlpatterns = [
    path('', index, name='shop'),
    path('data/', some_view, name="data"),
    path('crawl/', last_crawl_view, name="crawl")
]
