import os
import json
from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from .models import CrawlerData, DJItem

def get_data():
    with open('drone.txt') as f:
        txt = f.read()
    logs = txt.split('\n\n')
    return logs
def load_last_crawl(file="KK.json"):
    with open(file) as f:
        data = json.load(f)
    return data


class HomepageView(TemplateView):
    template_name = "pages/homepage.html"

class CrawlView(DetailView):
    template_name = "pages/crawl_detail.html"
    model = DJItem
    


class DroneView(TemplateView):
    template_name = "pages/drone.html"
