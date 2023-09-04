from django.db import models
from pydantic import BaseModel, Field
from itemadapter import ItemAdapter
import re
from datetime import datetime 
from typing import Dict
from bs4 import BeautifulSoup
from django_extensions.db.models import TimeStampedModel

class Spider(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name
    
class Website(models.Model):
    name = models.CharField(max_length=155)
    homepage = models.URLField()
    sitemap_url = models.URLField()
    first_crawl = models.DateTimeField(auto_now=True)
    last_crawl = models.DateTimeField(blank=True)

    def __str__(self):
        return self.homepage

class Category(models.Model):
    name = models.CharField(max_length=155)
    description = models.TextField(blank=True)



    def __str__(self):
        return self.name

class Manufacturer(models.Model):
    name = models.CharField(max_length=255)
    website = models.ForeignKey(Website, blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class PageData(models.Model):
    name = models.CharField(max_length=50)
    selector = models.CharField(max_length=300)
    value = models.TextField(blank=True)
    
    def __str__(self):
        return f"{self.name} | {self.selector}"
    
class CrawlerData(models.Model):
    data = models.JSONField()

    def __str__(self):
        self.id
        

class AdditionalImage(models.Model):
    link = models.URLField()
    name = models.CharField(max_length=100, blank=True)
    image = models.ImageField(blank=True)

    

        
    def __str__(self):
        return self.name
    

class DJItem(TimeStampedModel, models.Model):
    name = models.CharField(max_length=255)
    link = models.URLField()
    sku = models.CharField(max_length=150, blank=True, default='')
    name = models.CharField(max_length=255, blank=True, default='')
    main_image = models.URLField()
    products_id = models.IntegerField(default=0, blank=True, null=True)
    title = models.CharField(max_length=255, blank=True, default='')
    keywords = models.CharField(max_length=255, blank=True, default='')
    short_desc = models.TextField(blank=True, default='')
    manufacturer = models.CharField(max_length=100, blank=True)
    # manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE, blank=True, default=0)
    price = models.CharField(max_length=255, blank=True, default='')
    description = models.TextField(blank=True, default='')
    cleaned_description = models.TextField(blank=True, default='')

    # image_urls = models.ForeignKey(AdditionalImage, on_delete=models.CASCADE, blank=True)
    image_urls = models.TextField(blank=True, default='[]')
    breadcrumbs = models.TextField(blank=True, default='[]')
    discount_tiers = models.CharField(max_length=100, blank=True, default='[]')
    discount_amount = models.CharField(max_length=100, blank=True,  default='[]')

    def __str__(self):
        return self.name

    def clean_images(self):
        p = re.compile(r'https://www.knifekits.com/vcom/images/\S+\.jpg', re.UNICODE)
        m = p.findall(self.image_urls)
        return m
    
    
    
    class Exportable:
        """Returns all fields data for export."""        
        @property
        def data(self) -> Dict:
            return {
                field.name: getattr(self, field.name, None)
                for field in self._meta.fields
            }
 

def remove_html_tags(input):
    soup = BeautifulSoup(input, 'html.parser')
    return soup.get_text()

