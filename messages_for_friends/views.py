from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import MeMessages, FriendsMessages
from django.contrib.auth.models import User
from .forms import FriendsNewMessageForm, CommentForm
import datetime
from django.contrib.auth.decorators import login_required

#def hello_world(request):
    #return HttpResponse("hello there!")

def hello_world(request):
    hello = "hello_world"
    return render(request, "hello_world.html", {"hello": hello})

def home(request):
    messages_objects = MeMessages.objects.all()
    return render(request, "base.html", {"messages": messages_objects})

def current_time(request):
    now = datetime.datetime.now()
    now_on = "%s" %now
    #html = "<html><head><title>current time</title></head><body><p>It"s now {}</p></body></html>".format(now)
    #return HttpResponse(html)
    return render(request, "current_time.html", {"current_time": now_on})

def me(request):
    messages = MeMessages.objects.order_by("-publish_date")
    return render(request, "me.html", { "messages": messages })

def friends(request):
    messages = FriendsMessages.objects.order_by("-publish_date")
    #messages1 = messages.filter(messages.author.!=admin)
    return render(request, "friends.html", {"messages": messages})

def me_message_detail(request, pk):
    message = get_object_or_404(MeMessages, pk=pk)
    #message = Messages.objects.get(pk=pk)
    return render(request, "me_message_detail.html", {"message": message})

def friends_message_detail(request, pk):
    message = get_object_or_404(FriendsMessages, pk=pk)
    #comments = message.comments.order_by("-publish_date")
    return render(request, "friends_message_detail.html", {"message": message})

#ef friends_new_message(request):
    #new_message = get_object_or_404(Messages, pk=pk)
    #return render(request, "new_message.html", {"new_message": new_message
#    if request.method=="POST":
#        name = request.POST['name']
#        text = request.POST['message']
#
#        author = User.objects.first()
#        now = datetime.datetime.now()
#        now_on = "%s" %now
#        publish_date = now_on
#
#        message = FriendsMessages.objects.create(
#            name = name,
#            text = text,
#            author = author,
#            publish_date = publish_date)
#
#        return redirect('friends_message_detail', pk=message.id)
#
#    return render(request, "friends_new_message.html")
@login_required
def friends_new_message(request):

    if request.method == "POST":
        form = FriendsNewMessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.author = request.user
            now = datetime.datetime.now()
            now_on = "%s" %now
            message.publish_date = now_on
            message.save()

            return redirect("friends_message_detail", pk=message.id)
    else:
        form = FriendsNewMessageForm()
    return render(request, "friends_new_message.html", {"form": form})

@login_required
def add_comment_to_message(request, pk):
    message = get_object_or_404(FriendsMessages, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.message = message
            comment.author = request.user
            comment.save()
            return redirect('friends_message_detail', pk=message.pk)
    else:
        form = CommentForm()
    return render(request, 'add_comment_to_message.html', {'form': form})
