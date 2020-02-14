from django.http import HttpResponseRedirect
from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.contrib import auth, messages
from django.contrib.auth.models import User
from .models import Patterns
from .forms import PatternsForm


# Create your views here.

def index(request):
    """
    Returns a list of patterns to the index.html file
    """
    return render(request, 'index.html')

def patterns(request):
    """
    Create a view that users can upload thier own quilt patterns
    """
    
    patterns_form = PatternsForm(request.POST, request.FILES)    
    if request.method == 'POST':
        patterns_form.save()
        messages.success(request, "Pattern Uploaded! Thank You!!")
        return redirect('/')
    else:
        return render(request, 'patterns.html', {'patterns_form':patterns_form})