from django.contrib import admin
from django.contrib.admin import ModelAdmin


from .models import Data, AdditionalImage, Category, Manufacturer
from taggit_bulk.actions import tag_wizard

class DataModelAdmin(ModelAdmin):
    


    def get_queryset(self, request):
        return super().get_queryset(request).prefetch_related('tags')

    def tag_list(self, obj):
        return u", ".join(o.name for o in obj.tags.all())

    actions = [
        tag_wizard,
    ]


admin.site.register(Data, DataModelAdmin)
admin.site.register(AdditionalImage)
admin.site.register(Category)
admin.site.register(Manufacturer)

