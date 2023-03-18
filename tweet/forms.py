from django import forms
from .models import Tweets


class TweetForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(
        attrs={
            'rows': 3,
            'placeholder': "What's happening?"
        }
    ))

    class Meta:
        model = Tweets
        fields = ('content',)
