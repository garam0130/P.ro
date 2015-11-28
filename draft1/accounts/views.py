from django.shortcuts import render
from django.contrib.auth.views import login as auth_login
from accounts.forms import QuizAuthenticationForm
from django.shortcuts import redirect,get_object_or_404,render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from .forms import UserSignUpForm
from django.core.context_processors import csrf
from django.core.mail import send_mail
import hashlib, datetime, random
from django.utils import timezone
from django.contrib.auth.models import User
from .models import *
from django.contrib import messages
from uuid import uuid4



# Create your views here.

def login(request):

    return auth_login(request,authentication_form=QuizAuthenticationForm)


def signup(request):
    if request.method == 'POST':
     form = UserSignUpForm(request.POST)
     if form.is_valid():
        form.save()
        username = form.cleaned_data['username']
        email = form.cleaned_data['email']
        token = str(uuid4())
        # EmailToken.objects.filter(email=email).delete()
        key_expires = datetime.datetime.today() + datetime.timedelta(2)


        user=User.objects.get(username=username)
        TOKEN = EmailToken(user=user,token=token, key_expires=key_expires)

        TOKEN.save()



        email_subject = 'Account confirmation'
        email_body = "안녕하세요 %s, 가입해주셔서 감사합니다. 계정을 활성화시키기 위해서는 48시간 이내에"+"<a href = http://52.68.64.186/accounts/confirm/%s>링크</a>"+"를 클릭해주세요." % (email, TOKEN.token)
        send_mail(email_subject, email_body, 'p.rogramming3k@gmail.com',
    [email], fail_silently=False)
        return HttpResponseRedirect('/accounts/signup/complete')

    else:
     form = UserSignUpForm()

    tokens = {}
    tokens.update(csrf(request))
    tokens['form'] = form

    return render_to_response('registration/signup_form.html', tokens)

def signup_complete(request):
     return render_to_response('registration/signup_complete.html')


def signup_confirm(request, token):
    #check if user is already logged in and if he is redirect him to some other url, e.g. home
    if request.user.is_authenticated():
        HttpResponseRedirect('/contact')

    # check if there is UserProfile which matches the activation key (if not then display 404)
    user_token = get_object_or_404(EmailToken, token=token)

    #check if the activation key has expired, if it hase then render confirm_expired.html
    if user_token.key_expires < timezone.now():
        return render_to_response('registration/confirm_expired.html')
    #if the key hasn't expired save user and set him as active and render some template to confirm activation
    user = user_token.user
    user.is_active = True
    user.save()
    messages.success(request,'Confirmed. You can login now.')
    return redirect('blog:index')


