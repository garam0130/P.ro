from django.shortcuts import render, redirect
from blog.forms import ContactForm
from django.conf import settings
from django.contrib.auth import authenticate, login
from django.core.mail import send_mail
from django.http import HttpResponse
from django.http.response import HttpResponseRedirect


def index(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()

            name = form.cleaned_data['name']
            sender = form.cleaned_data['sender']
            phone = form.cleaned_data['phone']
            message = form.cleaned_data['message']
            from_email = settings.EMAIL_HOST_USER
            to_email = [from_email, ]

            contact_subject = "Message from %s is arrived" % name
            contact_message = "message: %s \nsender: %s \nEmail: %s \nphone: %s" %(message, name, sender, phone)

            send_mail(
                contact_subject,
                contact_message,
                from_email,
                to_email,
                fail_silently=False)

            return HttpResponseRedirect('/contact/')

    else:
        form = ContactForm()
        params = {
            'form': form,
        }

    return render(request, 'blog/index.html', params)


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('blog:index')

    else:
        return render(request, 'registration/login.html')






