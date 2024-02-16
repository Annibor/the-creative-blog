from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    author = forms.CharField(
        max_length=70,
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': "Your Name"}
        ),
    )
    body = forms.CharField(
        widget=forms.Textarea(
            attrs={'class': 'form-control', 'placeholder':'Leave a comment!'}
        )
    )
    class Meta:
        model = Comment
        fields = ['author', 'body']
