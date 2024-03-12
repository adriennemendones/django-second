from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    element = '<h1> Welcome to my django project<h1>'
    return HttpResponse(element)

def installation(request):
    context = {
        'title': "Installation",
        'skills': ["You're comfortable following instructions on:", "Writing boot images", "Installing an SD card or eMMC"],
        'tools': ["An Odroid device","MicroSD card or eMMC", "Ethernet connection"],
    }
    return render(request, 'installation.html', context)

def configuration(request):
    context = {
        'title': "Configuration",
    }
    return render(request, 'configuration.html', context)

def automation(request):
    context = {
        'title': "Automation",
        'skills': ["If you have got the hang of blueprints and would like to explore more, it’s time for the next step. But before you start creating automations, you will need to learn about the automation basics."]
    }
    return render(request, 'automation.html', context)

