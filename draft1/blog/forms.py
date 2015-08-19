from django.forms import ModelForm
from blog.models import Contact, Apply


class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'sender', 'phone', 'message']


class ApplyForm(ModelForm):
    class Meta:
        model = Apply
        fields = ('name', 'content')
