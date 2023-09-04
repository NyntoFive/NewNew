from django import forms
from django.core.validators import MinValueValidator, MaxValueValidator
from django.forms import ModelForm


from shop.models import Data

class DataForm(ModelForm):
    class Meta:
        model = Data
