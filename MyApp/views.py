from django.http import HttpResponse
def home(request):
    return HttpResponse('bonjour à tous')


from django.shortcuts import render
from .models import Dht
def dht11(request):
    tab = Dht.objects.all()
    s = {'tab': tab}
    return render(request, 'Tables.html', s)

def dht12(request):
    tab = Dht.objects.all()
    s = {'tab': tab}
    return render(request, 'index.html',s)

def dht13(request):
    print(" ok t555")

    from twilio.rest import Client
    account_sid = 'AC10ed6a83bfa23043429f889b4bc0aa8f'
    auth_token = '7276ed8546bf457d6db26bc28ce9f158'
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body="hello",
        from_='+19297326785',
        to='+212637392064',
    )
    print(message.sid)
    print(" ok t1")
    tab = Dht.objects.all()
    s = {'tab': tab}
    return render(request, 'table.html', s)

