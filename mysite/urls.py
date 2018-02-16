from django.conf.urls import url
from django.contrib import admin
from messages_for_friends import views

urlpatterns = [
    url(r'^$', views.home, name = "home"),
    url(r'^hello_world/', views.hello_world, name = "hello_world"),
    url(r'^admin/', admin.site.urls),
    url(r'^current_time/', views.current_time, name = "current_time"),
    url(r'^me/$', views.me, name="me"),
    url(r'^me/(?P<pk>\d+)/$', views.me_message_detail, name="me_message_detail"),
    url(r'^me/(?P<pk>\d+)/new/$', views.new_message, name="new_message"),
    url(r'^friends/$', views.friends, name="friends"),
    url(r'^friends/(?P<pk>\d+)/$', views.friends_message_detail, name="friends_message_detail"),

    #url(r'^you/', views.you, name="you"),

]
