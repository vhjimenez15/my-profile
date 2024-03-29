"""Posts forms."""

# Django
from django import forms

# Locals
from posts.models import Post


class PostForm(forms.ModelForm):
    """Post model form"""

    class Meta:
        """Form settings"""

        model = Post
        fields = ('user', 'profile', 'title', 'photo')
