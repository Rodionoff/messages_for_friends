from django import forms
from .models import FriendsMessages

class FriendsNewMessageForm(forms.ModelForm):
    text = forms.CharField(widget=forms.Textarea(
    attrs={"rows":13, "placeholder":"Расскажи мне"},
    ),
    max_length=4000,
    help_text="Максимальный размер записи: 4000 символов",)

    class Meta:
        model = FriendsMessages
        fields = ["name", "text"]
