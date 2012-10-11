# -*- coding: utf8 -*-

from django.http import HttpResponse, HttpResponseBadRequest

from forms import EmailInquiryForm


def send_email_inquiry(request):
    if request.method == 'POST':
        form = EmailInquiryForm(request.POST)
        if form.is_valid():
            form.save().send()
            return HttpResponse('OK')
    return HttpResponseBadRequest('ERROR')
