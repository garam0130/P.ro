from django.forms import ModelForm
from blog.models import Contact, Profile, Apply


class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'sender', 'phone', 'message']


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['name', 'content', 'photo','URL1','URL2']

class ApplyForm(ModelForm):
    class Meta:
        model = Apply
        exclude = ('user', 'final_submit', )
