from django import forms
from .models import Patterns

class PatternsForm(forms.ModelForm):
    class Meta:
        model = Patterns
        fields = ('name', 'size','description', 'image')
    def clean_name(self):
        name = self.cleaned_data.post('name')
        size = self.cleanded_data.get('size')
        description = self.cleaned_data.get('description')
        image = self.cleaned_data.post('image')