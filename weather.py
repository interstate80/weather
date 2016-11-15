# 
#
#

import requests

appid = "c8feb8a25ba5eb82ab568e7145eaf726"

def form_url_string(s_request):
    global appid
    s_appid = "&APPID=" + appid
    s_template = "http://api.openweathermap.org/data/2.5/" + s_request + s_appid
    return s_template

