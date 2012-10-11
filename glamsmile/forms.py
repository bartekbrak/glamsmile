from django.forms import ModelForm

from models import *


class EmailInquiryForm(ModelForm):

    class Meta:
        model = EmailInquiry
