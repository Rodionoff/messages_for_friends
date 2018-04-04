from django.contrib import admin
from .models import MeMessages, FriendsMessages, Comment



class CommentInline(admin.TabularInline):
    model = Comment

class FriendsMessagesAdmin(admin.ModelAdmin):
    inlines = [
        CommentInline,
    ]

admin.site.register(MeMessages)
admin.site.register(FriendsMessages, FriendsMessagesAdmin)
admin.site.register(Comment)
