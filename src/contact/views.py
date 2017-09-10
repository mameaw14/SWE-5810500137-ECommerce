from django.shortcuts import render
from .forms import contactForm
from django.core.mail import send_mail
from django.core.mail import EmailMessage
from django.conf import settings

def contact(request):
    form = contactForm(request.POST or None)
    title = 'Contact'
    confirm_message = None
    if form.is_valid():
        subject = 'Testing ECommerce Django'
        message = '%s %s'%(form.cleaned_data['comment'], form.cleaned_data['name'])
        emailFrom = form.cleaned_data['email']
        emailTo = [settings.EMAIL_HOST_USER]
        send_mail(subject, message, emailFrom, emailTo, fail_silently=False,)
        title = 'Thanks'
        confirm_message = 'Thanks for the message, We will get back to you'
        form = None
    context = {'title':title, 'form':form, 'confirm_message':confirm_message}
    template = 'contact.html'
    return render(request, template, context)