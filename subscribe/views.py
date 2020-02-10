from django.shortcuts import render, get_object_or_404, redirect
from .models import Subscribe
from .forms import SubscribeForm

# Create your views here.

def create_subscribe(request, pk):
    """
    Create a view that subscribes user to mailing list
    """
    subscribe = get_object_or_404(Subscribe, pk=pk)
    if request.method == "POST":
        subscribe_form = SubscribeForm(request.POST, request.FILES, instance=subscribe)
        if subscribe.form.is_valid():
            post = subscribe.form.save()
            return redirect(Subscribe.pk)
    else:
        form = SubscribeForm(instance=post)
    return redirect('/base.html')