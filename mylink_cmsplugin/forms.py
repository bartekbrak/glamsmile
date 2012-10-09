from django.forms.models import ModelForm
from django.utils.translation import ugettext_lazy as _
from models import MyLink
from django import forms
from cms.models import Page


class MyLinkForm(ModelForm):
    page_link = forms.ModelChoiceField(label=_("page"), queryset=Page.objects.drafts(), required=True)

    def for_site(self, site):
        # override the page_link fields queryset to containt just pages for
        # current site
        self.fields['page_link'].queryset = Page.objects.drafts().on_site(site)

    class Meta:
        model = MyLink
        exclude = ('page', 'position', 'placeholder', 'language', 'plugin_type')