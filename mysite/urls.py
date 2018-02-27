from django.conf.urls import url
from django.contrib import admin
from messages_for_friends import views
from accounts import views as accounts_views
from django.contrib.auth import views as auth_views


urlpatterns = [
    #url(r'^$', views.home, name = "home"),
    url(r'^hello_world/', views.hello_world, name = "hello_world"),
    url(r'^admin/', admin.site.urls),
    url(r'^current_time/', views.current_time, name = "current_time"),
    url(r'^me/$', views.me, name="me"),
    url(r'^me/(?P<pk>\d+)/$', views.me_message_detail, name="me_message_detail"),
    #url(r'^me/(?P<pk>\d+)/new/$', views.me_new_message, name="me_new_message"),
    url(r'^$', views.friends, name="friends"),
    url(r'^new_message/$', views.friends_new_message, name="friends_new_message"),
    url(r'^(?P<pk>\d+)/$', views.friends_message_detail, name="friends_message_detail"),
    url(r'^(?P<pk>\d+)/comment/$', views.add_comment_to_message, name="add_comment_to_message"),
    url(r'^signup/$', accounts_views.signup, name="signup"),
    url(r'^logout/$', auth_views.LogoutView.as_view(template_name="logout.html"), name="logout"),
    url(r'^login/$', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    url(r'^reset/$', auth_views.PasswordResetView.as_view(
        template_name='password_reset.html',
        email_template_name='password_reset_email.html',
        subject_template_name='password_reset_subject.txt'
    ),
    name='password_reset'),
url(r'^reset/done/$',
    auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'),
    name='password_reset_done'),
url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
    auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'),
    name='password_reset_confirm'),
url(r'^reset/complete/$',
    auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'),
    name='password_reset_complete'),
]
url(r'^settings/password/$', auth_views.PasswordChangeView.as_view(template_name='password_change.html'),
    name='password_change'),
url(r'^settings/password/done/$', auth_views.PasswordChangeDoneView.as_view(template_name='password_change_done.html'),
    name='password_change_done'),

    #url(r'^you/', views.you, name="you"),
