from django import forms
from .models import Bouquet

class BouquetForm(forms.ModelForm):
    class Meta:
        model = Bouquet
        fields = ['name', 'description', 'price', 'image']
