from django.shortcuts import render, get_object_or_404, redirect
from .models import Subscribe
from .forms import SubscribeForm

# Create your views here.

def create_subscribe(request):
    """
    Create a view that subscribes user to mailing list
    """
    subscribe = get_object_or_404(Subscribe)
    if request.method == "POST":
        subscribe_form = SubscribeForm(request.POST, request.FILES, instance=Subscribe)
        if Subscribe.form.is_valid():
            post = Subscribe.form.save()
            return redirect(Subscribe.pk)
    else:
        form = SubscribeForm(instance=post)
    return render(request, 'subscribe.html', {'form': form})