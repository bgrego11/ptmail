from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
import requests

# Create your views here.
@csrf_exempt
def index(request):
    try:
        data = json.loads(request.body)
        fname = data['fname']
        lname = data['lname']
        email = data['email']
        msg = data['msg']
        requests.post(
            "https://api.mailgun.net/v3/piranhatechnologies.com/messages",
            auth=("api", "key-774f995362ec727cc4819fa705c1313d"),
            data=({"from": "P Tech <mailgun@piranhatechnologies.com>",
                "to": [ "benja.gregory2@gmail.com","snydzllc@gmail.com"],
                "subject": "Hello",
                "text": fname + ' ' +lname + ' sent a message. They say '+ msg + 'reply at '+email}))
        return HttpResponse("email sent")
    except:
        return HttpResponse("send failed")
