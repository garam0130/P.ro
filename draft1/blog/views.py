from django.shortcuts import get_object_or_404, render, redirect
from blog.forms import ContactForm, ApplyForm
from blog.models import Apply, Post
from django.conf import settings
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.http.response import HttpResponseRedirect
from django.contrib import messages

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

            contact_subject = "[%s] 에게서 메일이 왔습니다" % name
            contact_message = "[보낸이:%s] \n[이메일:%s] \n[연락처:%s] \n[내용:%s]" %(message, name, sender, phone)

            send_mail(
                contact_subject,
                contact_message,
                from_email,
                to_email,
                fail_silently=False)
            messages.success(request,'이메일이 보내졌습니다.')

            return HttpResponseRedirect('/contact/')
        else:
            messages.warning(request,'양식에 맞춰 다시 제출해주세요.')

    else:
        form = ContactForm()
        post_list = Post.objects.all()
        params = {
            'form': form, 'post_list': post_list,
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
            if '_save' in request.POST:
                apply.save()
                messages.success(request,'지원서가 임시저장 되었습니다.')
                return redirect('blog:index')
            if '_submit' in request.POST:
                apply.save()
                messages.success(request,'지원 감사합니다.')
                return redirect('blog:thanks')

    else:
        if apply_exist:
            apply = Apply.objects.get(user=user)
            if apply.final_submit:
                # form = ApplyForm(instance=apply)
                return redirect('blog:thanks')
            else:
                form = ApplyForm(instance=apply)
        else:
            form = ApplyForm()

    return render(request, 'blog/apply.html', {
        'form': form,
    })


@login_required
def thanks(request):
    user = request.user
    apply = get_object_or_404(Apply, user=user)
    just_now = not apply.final_submit
    apply.final_submit = True
    apply.save()
    return render(request, 'blog/thanks.html', {
        'just_now': just_now,
    })
