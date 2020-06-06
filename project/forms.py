from django.contrib.auth.models import User
from django import forms
from .models import Profile,Project

class UpdateUser(forms.ModelForm):
    email=forms.EmailField()
    class Meta:
        model=User
        fields=['username', 'email']
        
class UpdateProfile(forms.ModelForm):
    class Meta:
        fields=['contact','location','bio','image']