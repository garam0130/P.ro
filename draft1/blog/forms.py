from django.forms import ModelForm
from blog.models import Contact, Post


class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'sender', 'phone', 'message']


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['name', 'content', 'photo']