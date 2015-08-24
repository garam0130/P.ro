from django.shortcuts import render, redirect
from blog.forms import ContactForm, ApplyForm
from blog.models import Apply
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.http.response import HttpResponseRedirect
from django.contrib import messages

def index(request):
    if request.method == 'POST':
        contact_form = ContactForm(request.POST)
        params = {
            'contact_form': contact_form,
        }
        if contact_form.is_valid():
            contact_form.save()

            name = contact_form.cleaned_data['name']
            sender = contact_form.cleaned_data['sender']
            phone = contact_form.cleaned_data['phone']
            message = contact_form.cleaned_data['message']
            from_email = settings.EMAIL_HOST_USER
            to_email = [from_email, ]

            contact_subject = "[%s] 에게서 메일이 왔습니다" % name
            contact_message = "[보낸이:%s] \n[이메일:%s] \n[연락처:%s] \n[내용:%s]" %(message, name, sender, phone)

            send_mail(
                contact_subject,
                contact_message,
                from_email,
                to_email,
                fail_silently=False)
            messages.success(request,'A mail has been sent to us.')

            return HttpResponseRedirect('/contact/')

    else:
        contact_form = ContactForm()
        params = {
            'contact_form': contact_form,
        }

    return render(request, 'blog/index.html', params)







@login_required
def apply(request):
    user = request.user
    apply_exist = Apply.objects.filter(user=user).exists()
    if request.method == "POST":


        if apply_exist:
            apply = Apply.objects.get(user=user)
            form = ApplyForm(request.POST, instance=apply)
        else:
            form = ApplyForm(request.POST)

        if form.is_valid():
            apply = form.save(commit=False)
            apply.user = request.user
            apply.save()
            return redirect('blog:index')

    else:
        if apply_exist:
            apply = Apply.objects.get(user=user)
            form = ApplyForm(instance=apply)
        else:
            form = ApplyForm()

    return render(request, 'blog/apply.html', {
        'form': form,
    })
