from django.shortcuts import render, render_to_response

from django.http import HttpResponse, Http404
from django.template import Context
from django.template.loader import get_template


from django.contrib.auth.models import User
from django.utils import simplejso

# Create your views here.

def mainpage(request):
    return render_to_response(

    'mainpage.html',
    {
        'titlehead': 'BePitchAndPutt app',
        'pagetitle': 'Welcome to BePitchAndPutt app',
        'contentbody': 'Your best application to see your training results',
        'user': request.user
    })

def results(request):
    return render_to_response(

    'results.html',
    {
        'titlehead': 'results for' request.user + '-->' request.results



    })

def weather(request):
    return render_to_response(

    'weather.html',
    {



    })

def stadistics(request):
    return render_to_response(

    'stadistics.html',
    {


    })
