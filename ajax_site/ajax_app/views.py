from django.conf import settings
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import ContactForm
from django.core.mail import send_mail




def ajax_form(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            sender =  settings.EMAIL_HOST_USER
            cc_myself = form.cleaned_data['cc_myself']

            recipients = ['sa4dkhan@gmail.com']
            if cc_myself:
                recipients.append(sender)
            send_mail(subject, message, sender, recipients, fail_silently=False)
            return HttpResponseRedirect('/thanks/')
    else:
        form = ContactForm()
    context = { 'form': form }
    return render(request, 'ajax_app/index.html', context)
