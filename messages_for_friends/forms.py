from django import forms
from .models import FriendsMessages, Comment

class FriendsNewMessageForm(forms.ModelForm):
    text = forms.CharField(widget=forms.Textarea(
    attrs={"rows":13, "placeholder":"Расскажи мне"},
    ),
    max_length=4000,
    help_text="Максимальный размер записи: 4000 символов",)

    class Meta:
        model = FriendsMessages
        fields = ["name", "text"]

class CommentForm(forms.ModelForm):
    text = forms.CharField(widget=forms.Textarea(
    attrs={"rows":13, "placeholder":"Напиши комментарий"},
    ),
    max_length=4000,
    help_text="Максимальный размер записи: 1000 символов",)

    class Meta:
        model = Comment
        fields = ['text'] 
