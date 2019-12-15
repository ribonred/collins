from django import forms
from .models import imagePromo

class PromoForms(forms.ModelForm):

    class Meta:
        model = imagePromo
        fields = ('__all__')
        exclude = ('publisher',)