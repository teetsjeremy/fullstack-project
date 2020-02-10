from django import forms
from .subscribe import Subscribe

class SubscribeForm(forms.ModelForm):
    class Meta:
        
        fields = ('email', 'first name', 'last name', 'date of birth')