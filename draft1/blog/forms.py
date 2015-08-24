from django.forms import ModelForm
from blog.models import Contact, Post, Apply


class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'sender', 'phone', 'message']


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['name', 'content', 'photo']

class ApplyForm(ModelForm):
    class Meta:
        model = Apply
        exclude = ('user', 'final_submit', )
