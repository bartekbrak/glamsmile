# -*- coding: utf8 -*-

from django.conf import settings
from django.core.mail import send_mail
from django.db import models


class EmailInquiry(models.Model):
    """
    Stores e-mail inquires, so nothing is lost on the wire
    """

    name = models.CharField(max_length=50, verbose_name='Imię')
    surname = models.CharField(max_length=50, verbose_name='Nazwisko')
    company = models.CharField(max_length=50, verbose_name='Firma')
    content = models.CharField(max_length=10240, verbose_name='Treść')
    email = models.EmailField(verbose_name='E-mail')
    created = models.DateTimeField(auto_now_add=True, editable=False)

    def send(self):
        message = u"""%(content)s

%(name)s %(surname)s
%(company)s
%(email)s

--
Wiadomość została wygenerowana automatycznie, prosimy nie odpowiadać.
        """ % {
            'content': self.content,
            'name': self.name,
            'surname': self.surname,
            'company': self.company,
            'email': self.email,
        }
        send_mail('glamsmile formularz', message,
                  settings.SERVER_EMAIL,
                  settings.MANAGERS)
