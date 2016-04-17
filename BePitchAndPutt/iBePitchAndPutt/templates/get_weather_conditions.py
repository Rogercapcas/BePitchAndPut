#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: set fileencoding=utf8 :
'''
Get weather from weather underground
Created on 11/22/2014
Using XML as format, minidom
@author: carlesm
'''

import sys
import requests
import json

api_key = None  # If assigned won't read argv[1]


class WeatherClient(object):

    
    """Will access wunderground to gather weather information
    Provides access to wunderground API
    (http://www.wunderground.com/weather/api)
    Provides methods:
        conditions
    """

    url_base = 'http://api.wunderground.com/api/'
    url_services = {
        "conditions": "/conditions/q/CA/"
    }

    def __init__(self, apikey):
        super(WeatherClient, self).__init__()
        self.api_key = apikey


    def conditions(self, location):
        """
        Accesses wunderground conditions information for the given location
        """
        resp_format = "json"
        url = WeatherClient.url_base + api_key + \
            WeatherClient.url_services[
                "conditions"] + location + "." + resp_format
        r = requests.get(url)

        jsondata = json.loads(r.text)
        return jsondata["conditions"]


def print_conditions(conditions):
    """
    Prints an conditions received as a dict
    """
    print "Wind conditions:"
    print "Wind direction", conditions["wind_dir"]

    print "Wind speed:"
    print "Average on this date", conditions["wind_kph"]


if __name__ == "__main__":
    if not api_key:
        try:
            api_key = sys.argv[1]
        except IndexError:
            print "Must provide api key in code or cmdline arg"

    weatherclient = WeatherClient(api_key)
    print_conditions(weatherclient.conditions("Guissona"))
