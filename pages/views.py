from django.shortcuts import render
from pages.models import Team

# Create your views here.

def home(request):
    teams = Team.objects.all()
    data = {
        'teams': teams,
    }
    return render(request, 'pages/home.html', data)

def about(request):
    teams = Team.objects.all()
    data = {
        'teams': teams,
    }
    return render(request, 'pages/about.html', data)

def services (requst):
    return render(requst, "pages/services.html")

def contact (requst):
    return render(requst, "pages/contact.html")