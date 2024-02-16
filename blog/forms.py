"""
All the forms for the blog app.
"""
from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    """
    A form for creating a comment.

    This form is used to create comments on blog posts.
    It provides fields for the author's name and the comment body.
    The author's name is limited to a maximum of 70 characters.
    The comment body is a textarea allowing multi-line input.

    Attributes:
        author (CharField): A field for the author's name.
        body (CharField): A field for the actual comment.

    Meta:
        model (Comment): The model associated with this form (Comment).
        fields (list): The list of fields to include in the form (author, body).
    """
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
        """
        model (Comment): The model associated with this form (Comment).
            This indicates which model the form is based on for validation and saving.
        fields (list): The list of fields to include in the form (author, body).
            This specifies which fields from the associated model should be included in the form
        """
        model = Comment
        fields = ['author', 'body']
