from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(CrawlerData)
admin.site.register(Category)
admin.site.register(DJItem)
admin.site.register(Manufacturer)
admin.site.register(Website)

admin.site.register(AdditionalImage)
