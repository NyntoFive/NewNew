from django.urls import path
from pages.views import HomepageView, DroneView, CrawlView

urlpatterns = [
    path('', HomepageView.as_view(), name="home"),
    path('crawl/<int:pk>/', CrawlView.as_view(), name='crawl'),
    path('drone/', DroneView.as_view(), name="drone"),
]