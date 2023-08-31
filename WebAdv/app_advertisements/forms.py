from typing import Any, Dict
from  django import forms
from .models import Advertisement
from django.core.exceptions import ValidationError


# Create the form class
class AdvertisementForm(forms.ModelForm):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['title'].widjet.attrs['class']='form-control form-control-lg'
        self.fields['description'].widjet.attrs['class']='form-control form-control-lg'
        self.fields['image'].widjet.attrs['class']='form-control form-control-lg'
        self.fields['price'].widjet.attrs['class']='form-control form-control-lg'
        self.fields['auction'].widjet.attrs['class']='form-control-input'
    
    
    
    class Meta:
        model = Advertisement
        fields = ["title", "description", "image", "price","auction"]
        
    def clean_title(self):
        title=self.cleaned_data['title']
        if title.startswith('?'):
            raise ValidationError('название недолжно начинаться с ?. ')
        else:
            return title