from django.shortcuts import render, redirect
from blog.forms import ContactForm, ApplyForm
from blog.models import Apply
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
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
