from django.shortcuts import render
from .forms import contactForm
from django.core.mail import send_mail
from django.conf import settings
from django.http import HttpResponse


# Create your views here.

def contact(request):
    title = 'Contact us Today.'
    form = contactForm(request.POST or None)
    confirm_message = None

    if form.is_valid():
        name = form.cleaned_data['name']
        comment = form.cleaned_data['comment']
        email = form.cleaned_data['email']
        subject = 'Message from MYSITE.com'
        message = '%s %s' %(comment, email)
        emailFrom = email
        emailTo = [settings.EMAIL_HOST_USER]
        send_mail(subject, message, emailFrom, emailTo, fail_silently=True)
        title = "Thank you!"
        confirm_message = "Thanks for the messgae, we will get right back to you."
        form = None


    context = {'title': title, 'form': form, 'confirm_message': confirm_message, }
    template = 'contact.html'
    return render(request,template,context)
