from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from .models import Profile

class signupform(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    repeat_password = forms.CharField(widget=forms.PasswordInput)
    no_tlp = forms.CharField(required=True,widget=forms.TextInput(attrs={'placeholder':'contoh: 6281233XXXX'}))
    foto_profile = forms.ImageField(required=True)
    class Meta:
        model = User
        fields = ('username','first_name','last_name','email','password',)

class LoginForm (forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class profiles(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('__all__')
        exclude = ('user',)
