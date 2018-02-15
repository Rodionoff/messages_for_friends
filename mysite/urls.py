from django.conf.urls import url
from django.contrib import admin
from messages_for_friends import views

urlpatterns = [
    url(r'^$', views.home, name = "home"),
    url(r'^hello_world/', views.hello_world, name = "hello_world"),
    url(r'^admin/', admin.site.urls),
    url(r'^current_time/', views.current_time, name = "current_time"),
    url(r'^me/$', views.me, name="me"),
    url(r'^me/(?P<pk>\d+)/$', views.message_detail, name='message_detail'),
    url(r'^you/$', views.you, name="you"),
    url(r'^you/(?P<pk>\d+)/$', views.message_detail, name="message_detail")

    #url(r'^you/', views.you, name="you"),

]
