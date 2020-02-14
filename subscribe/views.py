from django.shortcuts import render, reverse, redirect
from .models import Subscribe
from .forms import SubscribeForm

# Create your views here.

def create_subscribe(request):
    """
    Create a view that subscribes user to mailing list
    """
    subscribe_form = SubscribeForm(request.POST or None)
    if request.method=="POST":
        
        if subscribe_form.is_valid():
            email = subscribe_form.cleaned_data['email']
            first_name = subscribe_form.cleaned_data['first_name']
            last_name = subscribe_form.cleaned_data['last_name']
            date_of_birth = subscribe_form.cleaned_data['date_of_birth']
            return redirect('/')
    else:
        
        return render(request, 'subscribe.html', {'subscribe_form': subscribe_form})