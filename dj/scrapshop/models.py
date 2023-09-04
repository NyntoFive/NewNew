from django.db import models

from django_extensions.db.fields import AutoSlugField



class Product(models.Model):
    name = models.CharField(max_length=255)
    sku = models.SlugField()
    link = models.URLField()
    name = models.CharField(max_length=255, blank=True, default='')
    main_image = models.URLField()
    products_id = models.IntegerField(default=0, blank=True)
    title = models.CharField(max_length=255, blank=True, default='')
    keywords = models.CharField(max_length=255, blank=True, default='')
    short_desc = models.TextField(blank=True, default='')
    price = models.CharField(max_length=255, blank=True, default='')
    description = models.TextField(blank=True, default='')
    
    slug = AutoSlugField(populate_from='sku')
    
    
    def __str__(self):
        return self.name

class AdditionalImage(models.Model):
    name = models.CharField(max_length=155)
    image = models.ImageField()
    products = models.ForeignKey(Product, on_delete=models.CASCADE)
    
        

class Category(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    link = models.URLField(blank=True)
    
    def __str__(self):
        return self.name
    

    
    
        
    def __str__(self):
        return self.name

class Manufacturer(models.Model):
    name = models.CharField(max_length=200)
    website = models.URLField(blank=True, null=True)
    contact_info = models.JSONField()
