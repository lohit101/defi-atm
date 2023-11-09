from django.shortcuts import render, HttpResponse, redirect
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
import base64
import json
from .models import Server1, Server2

# Create your views here.

def home(request):
    return render(request, "home.html")

def signup(request):
    if request.method == "POST":
        name = request.POST.get("name")
        pin = request.POST.get("pin")
        card = request.POST.get("card")

        s = Server1(name=name, card=card, pin=pin, balance=0)
        s.save()

        context = {
            "user": user
        }

        return render(request, "signup.html")
    else:
        return render(request, "signup.html")

@csrf_exempt
def login(request, data):
    response = base64.b64decode(data).decode()
    response = response.split("|")

    try:
        if getattr(Server1.objects.get(card=str(response[0])), 'card') and getattr(Server1.objects.get(pin=str(response[1])), 'pin'):
            res = {
                'name' : Server1.objects.get(card=str(response[0])).name,
                'card' : Server1.objects.get(card=str(response[0])).card,
                'pin' : Server1.objects.get(card=str(response[0])).pin,
                'balance' : Server1.objects.get(card=str(response[0])).balance
            }

            return HttpResponse(json.dumps(res))
    except:
        res = {
            "name": "This value does not exist in Server 1"
        }
        return HttpResponse(json.dumps(res))

    print(response)
    return HttpResponse("OK")