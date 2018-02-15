from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Messages
from django.contrib.auth.models import User
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
    #html = "<html><head><title>current time</title></head><body><p>It"s now {}</p></body></html>".format(now)
    #return HttpResponse(html)
    return render(request, "current_time.html", {"current_time": now_on})

def me(request):
    messages = Messages.objects.order_by("-publish_date")
    return render(request, "me.html", { "messages": messages })

def you(request):
    messages = Messages.objects.order_by("-publish_date")
    #messages1 = messages.filter(messages.author.!=admin)
    return render(request, "you.html", {"messages": messages})

def message_detail(request, pk):
    message = get_object_or_404(Messages, pk=pk)
    #message = Messages.objects.get(pk=pk)
    return render(request, "message_detail.html", {"message": message})

def new_message(request, pk):
    #new_message = get_object_or_404(Messages, pk=pk)
    #return render(request, "new_message.html", {"new_message": new_message})

    if request.method=="POST":
        name = request.POST['name']
        text = request.POST['message']

        author = User.objects.first()
        now = datetime.datetime.now()
        now_on = "%s" %now
        publish_date = now_on

        message = Messages.objects.create(
            name = name,
            text = text,
            author = author,
            publish_date = publish_date)

        return redirect('me')

    return render(request, "new_message.html")
