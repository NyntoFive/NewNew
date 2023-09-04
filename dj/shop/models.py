from django.db import models
from django_extensions.db.models import CreationDateTimeField, ModificationDateTimeField, AutoSlugField
from taggit.managers import TaggableManager
import re



class Category(models.Model):
    name = models.CharField(max_length=155)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class AdditionalImage(models.Model):
    link = models.URLField()
    name = models.CharField(max_length=100, blank=True)
    image = models.ImageField(blank=True)
    item = models.ForeignKey("Data", on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Manufacturer(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Data(models.Model):
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
    price = models.DecimalField(decimal_places=2, max_digits=6, default=0.0)
    description = models.TextField(blank=True, default='')
    cleaned_description = models.TextField(blank=True, default='')
    # image_urls = models.ForeignKey(AdditionalImage, on_delete=models.CASCADE, blank=True)
    image_urls = models.TextField(blank=True, default='')
    breadcrumbs = models.TextField(blank=True, default='')
    discount_tiers = models.CharField(max_length=100, blank=True, default='')
    discount_amount = models.CharField(max_length=100, blank=True,  default='')
    
    tags = TaggableManager()

    def __str__(self):
        return f"{self.pk}: {self.sku}"
    
