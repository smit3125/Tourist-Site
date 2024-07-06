from django import forms
from .models import user

# class ImageForm(forms.ModelForm):
#  class Meta:
#   model = Image
#   fields = '__all__'
#   labels = {'photo':''}
class UserSignupForm(forms.ModelForm):
    class Meta:
        model = user
        fields = ['firstname', 'lastname', 'email', 'mobile_NO', 'address', 'password']

