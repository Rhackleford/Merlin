from django.shortcuts import render


def home(request):
    return render(request, 'merlin/home.html')

def dashboard(request):
    return render(request, 'merlin/dashboard.html')
from django.shortcuts import render

# Create your views here.
