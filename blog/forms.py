from django import forms
from .models import *


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["content", "parent"]
        widgets = {
            "content": forms.Textarea(
                attrs={"row": 5, "placeholder": "Write your comment..."}
            ),
            "parent": forms.HiddenInput(),
        }
