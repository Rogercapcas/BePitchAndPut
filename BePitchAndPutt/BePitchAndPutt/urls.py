"""BePitchAndPutt URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth.models import User

from iBePitchAndPutt.views import *

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^player/$',players),
    url(r'^player/(?P<pk>\d+)(?P<format>(\.json|\.xml|\.html)?)/$',player_info),
    url(r'^holes(?P<format>(\.json|\.xml|\.html)?)/$',holes),
    url(r'^holes/(?P<pk>\d+)(?P<format>(\.json|\.xml|\.html)?)/$',hole_info),
    url(r'^field/(?P<format>(\.json|\.xml|\.html)?)/$',field),
    url(r'^field/(?P<pk>\d+)(?P<format>(\.json|\.xml|\.html)?)/$',field_info),
    url(r'^rules/(?P<format>(\.json|\.xml|\.html)?)/$',rules),
    url(r'^actualWeather/(?P<format>(\.json|\.xml|\.html)?)/$',actualWeather),
    url(r'^results/(?P<pk>\d+)/(?P<pk>\d+)(?P<format>(\.json|\.xml|\.html)?)/$',player_results),
    url(r'^$', mainpage, name='home'),
    url(r'^login/$', 'django.contrib.auth.views.login'),
]
