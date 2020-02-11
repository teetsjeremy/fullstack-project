from django import forms
from .models import Subscribe

class SubscribeForm(forms.ModelForm):
    class Meta:
        model = Subscribe
        fields = ('email', 'first_name', 'last_name', 'date_of_birth')