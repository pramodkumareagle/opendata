from django.http import HttpResponse
from django.shortcuts import render

import urllib.request, json
from django.shortcuts import render
import requests
#
#
#
# def index(request):
#     url = "https://data.cityofnewyork.us/api/odata/v4/bnx9-e6tj"
#     response = urllib.request.urlopen(url)
#     data = json.loads(response.read().decode())
#     print(data)
#     return render(request, 'eagleapp/index.html', data)



# Create your views here.
def index(request):
    response=requests.get('https://data.cityofnewyork.us/resource/wvts-6tdf.json').json()
    return render(request,'eagleapp/data.html',{'response':response})


def manhattan(request):
    response=requests.get(url = "https://data.cityofnewyork.us/resource/wvts-6tdf.json?borough=Manhattan").json()
    return render(request,'eagleapp/index.html',{'response':response})

def bronx(request):
    response=requests.get(url = "https://data.cityofnewyork.us/resource/wvts-6tdf.json?borough=Bronx").json()
    return render(request,'eagleapp/index.html',{'response':response})

def broklyn(request):
    response=requests.get(url = "https://data.cityofnewyork.us/resource/wvts-6tdf.json?borough=Brooklyn").json()
    return render(request,'eagleapp/index.html',{'response':response})

def queens(request):
    response=requests.get(url = "https://data.cityofnewyork.us/resource/wvts-6tdf.json?borough=Queens").json()
    return render(request,'eagleapp/index.html',{'response':response})