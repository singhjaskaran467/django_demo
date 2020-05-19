from django.shortcuts import render, redirect
from .models import Destination
from django.contrib.auth.models import User, auth
from django.contrib import messages
from accounts.views import login


# Create your views here.

def index(request):
    dests = Destination.objects.all()
    return render(request, 'index.html', {'dests': dests})


def show(request, id):
    if request.user.is_authenticated:
        print(id)
        dest = Destination.objects.get(id=id)
        print (dest)
        return render(request, 'destination.html', {'dest': dest})
    else:
        messages.info(request, 'Please Login first')
        return redirect('login')

