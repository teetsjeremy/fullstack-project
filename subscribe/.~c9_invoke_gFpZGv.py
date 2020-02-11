from django import forms
from .subscribe import Subscribe

class SubscribeForm(forms.ModelForm):
    class Meta:
        model = 
        fields = ('email', 'first name', 'last name', 'date of birth')