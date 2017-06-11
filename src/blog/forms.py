from django import forms
from django.forms import Textarea
from .models import Comment


class PostCommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('comment',)
        widgets = {
            'comment': Textarea(attrs={'class': 'materialize-textarea'})
        }
