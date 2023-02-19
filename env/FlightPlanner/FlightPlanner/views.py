from django.shortcuts import render
from .forms import  AptForm
from .models import airportModel
from .getDistance import findDistance
import requests

def index(request):
    form = AptForm()

    if request.method == 'POST':
        #Have only 1 object at a time, delete all previous
        airportModel.objects.all().delete()
        #print(request.POST)
        form = AptForm(request.POST)
        if form.is_valid():
            form.save()
            
    #Get the start and ending airports
    startApt = request.POST.getlist('Starting Airport')
    endApt = request.POST.getlist('End Airport')
    #Get rid of the brackets and single quotes around to pass them into function
    cleanStartApt = ''.join(startApt)
    cleanEndApt = ''.join(endApt)
    context = {'form':form, 'Start Airport':cleanStartApt, 'End Airport':cleanEndApt, 'distance': findDistance}
    return render(request, 'index.html', context)
    #context = {'form':form}
    #return render(request, 'index.html', context)

def get_weather(request):
    url = "https://api.checkwx.com/metar/KJFK/decoded"

    response = requests.get("GET", url, headers = {'X-API-Key': '5df00ce5a84046e4ad91f3cca5'})

    print(response.text)

def CalcDistance(request):
    dis = findDistance()
    context = {'distance': dis}
    return render(request, 'index.html', context)

