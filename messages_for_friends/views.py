from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Messages
import datetime

#def hello_world(request):
    #return HttpResponse("hello there!")

def hello_world(request):
    hello = "hello_world"
    return render(request, "hello_world.html", {"hello": hello})

def home(request):
    messages_objects = Messages.objects.all()
    return render(request, "base.html", {"messages": messages_objects})

def current_time(request):
    now = datetime.datetime.now()
    now_on = "%s" %now
    #html = "<html><head><title>current time</title></head><body><p>It's now {}</p></body></html>".format(now)
    #return HttpResponse(html)
    return render(request, 'current_time.html', {'current_time': now_on})

def me(request):
    messages = Messages.objects.order_by("-publish_date")
    return render(request, 'me.html', { 'messages': messages })

def you(request):
    messages = Messages.objects.order_by("-publish_date")
    #messages1 = messages.filter(messages.author.!=admin)
    return render(request, 'you.html', {'messages': messages})

def message_detail(request, pk):
    message = get_object_or_404(Messages, pk=pk)
    #message = Messages.objects.get(pk=pk)
    return render(request, 'message_detail.html', {"message": message})
