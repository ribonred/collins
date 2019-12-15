from django import forms
from .models import pengembangan
from ckeditor_uploader.widgets import CKEditorUploadingWidget

class Artikeledit(forms.ModelForm):
    isi2 = forms.CharField(widget=CKEditorUploadingWidget())
    class Meta:
        model = pengembangan
        fields = ('__all__')
        exclude = ('author','slug')