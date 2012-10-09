from django.db import models
from django.utils.translation import ugettext_lazy as _
from cms.models import CMSPlugin, Page


class MyLink(CMSPlugin):
    name = models.CharField(_("name"), max_length=256)
    page_link = models.ForeignKey(Page, verbose_name=_("page"), blank=False, null=False)
    section = models.CharField(_("section"), max_length=256)

    def __unicode__(self):
        return "%s#%s" % (self.name, self.section)

    # search_fields = ('name',)
