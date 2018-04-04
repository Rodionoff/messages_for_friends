from django.contrib import admin
from .models import MeMessages, FriendsMessages



class CommentInline(admin.TabularInline):
    model = Comment

class MeMessageAdmin(admin.ModelAdmin):
    inlines = [
        CommentInline,
    ]
    search_fields = ['name']

class FriendsMessagesAdmin(admin.ModelAdmin):
    inlines = [
        CommentInline,
    ]

admin.site.register(MeMessages, MeMessagesAdmin)
admin.site.register(FriendsMessages, FriendsMessagesAdmin)
