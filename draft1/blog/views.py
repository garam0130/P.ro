from django.shortcuts import render, redirect
from blog.forms import ContactForm
from django.conf import settings
from django.contrib.auth import authenticate, login
from django.core.mail import send_mail
from django.http import HttpResponse
from django.http.response import HttpResponseRedirect


def index(request):
    if request.method == 'POST':
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            contact_form.save()

            name = contact_form.cleaned_data['name']
            sender = contact_form.cleaned_data['sender']
            phone = contact_form.cleaned_data['phone']
            message = contact_form.cleaned_data['message']
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
        contact_form = ContactForm()
        params = {
            'contact_form': contact_form,
        }

    return render(request, 'blog/index.html', params)









