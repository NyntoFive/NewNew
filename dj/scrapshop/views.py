from django.shortcuts import render
from django.shortcuts import reverse
from PIL import Image
from django import forms
from django.core.files.uploadedfile import SimpleUploadedFile
from django.views.generic import TemplateView, ListView, DetailView

class ImageForm(forms.Form):
    img = forms.ImageField()

class ShopView(TemplateView):
    template_name = "scrapshop/landing.html"
    
    