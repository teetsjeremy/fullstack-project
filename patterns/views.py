from django.shortcuts import render, reverse, redirect, get_object_or_404
from .models import Patterns
from .forms import PatternsForm

# Create your views here.

def patterns(request):
    """
    Create a view that users can upload thier own quilt patterns
    """
    post = get_object_or_404(Patterns)
    patterns_form = PatternsForm(request.POST, request.FILES, instance=post)
    if request.method=="POST":
        
        if Patterns.form.is_valid():
            name = patterns_form.cleaned_data['name']
            size = patterns_form.cleaned_data['size']
            description = patterns_form.cleaned_data['description']
            image = patterns_form.cleaned_data['image']
            return redirect('products.html', {'products_form': products_form})
    else:
        
        return render(request, 'patterns.html', {'patterns_form': patterns_form})