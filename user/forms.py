from django import forms
from user.models import User


class SearchForm(forms.ModelForm):
    username = forms.CharField(label="")
    username.widget.attrs.update(
        {
            "class": "form-control",
            "placeholder": "Search",
            "style": "border-radius: 50px; float: left;",
            "id": "search",
            "onkeypress": "return searchKeyPress(event);",
        }
    )

    class Meta:
        model = User
        fields = ("username",)
