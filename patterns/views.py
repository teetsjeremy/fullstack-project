from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.utils import timezone
from .models import Patterns
from .forms import PatternsForm

# Create your views here.

def get_patterns(request):
    """
    Create a view that will return a list
    of Patterns that were published prior to 'now'
    and render them to the 'blogposts.html' template
    """
    posts = Patterns.objects.filter('-name').order_by('-size')
    return render(request, "patterns.html", {'posts': posts})

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
            return redirect('products.html', {'products_form'})
    else:
        
        return render(request, 'patterns.html', {'patterns_form': patterns_form})