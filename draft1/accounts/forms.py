from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.core import validators


class QuizAuthenticationForm(AuthenticationForm):
    question = forms.CharField(label = '주인장 이름은?')
    # email = forms.EmailField()


    # def clean_email(self):
    #     email = self.cleaned_data.get("email",'')
    #     if email:
    #         if not User.objects.filter(email=email).exists():
    #             raise forms.ValidationError('등록되지 않은 메일입니다.')

    def clean_question(self):
        answer = self.cleaned_data.get('question','')
        if answer != '박근우':
            raise forms.ValidationError('이름이 틀렸어요ㅠㅠ')

class UserSignUpForm(UserCreationForm):
    email = forms.EmailField()


    def clean_email(self):
        email = self.cleaned_data.get("email",'')
        if email:
            if User.objects.filter(email=email).exists():
                raise forms.ValidationError('이미 등록된 이메일입니다.')
        return email

    def save(self,commit=True):
        user = super(UserSignUpForm,self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.is_active = False
            user.save()
        return user

    def __init__(self, *args, **kwargs):
        super(UserSignUpForm, self).__init__(*args, **kwargs)

        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None
