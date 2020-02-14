from django import forms
from .models import Patterns

class PatternsForm(forms.ModelForm):
    class Meta:
        model = Patterns
        fields = ('name', 'size','description', 'image')