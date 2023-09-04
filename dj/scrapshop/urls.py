from django.urls import path
from scrapshop.views import ShopView



urlpatterns = [
    path('', ShopView.as_view(), name="shop"),
]