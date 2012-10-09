from django.utils.translation import ugettext_lazy as _
from django.contrib.sites.models import Site
from django.conf import settings
from cms.plugin_pool import plugin_pool
from cms.plugin_base import CMSPluginBase
from forms import MyLinkForm
from models import MyLink


# short for, MyLinkPLugin, which could not be used due to django bug
class MyLPlugin(CMSPluginBase):
    model = MyLink
    form = MyLinkForm
    name = _("MyLink")
    render_template = "cms/plugins/mylink.html"

    def render(self, context, instance, placeholder):
        if instance.page_link:
            link = instance.page_link.get_absolute_url()
        else:
            link = ""
        context.update({
            'name': instance.name,
            'link': link,
            'section': instance.section,
            'placeholder': placeholder,
            'object': instance
        })
        return context

    def get_form(self, request, obj=None, **kwargs):
        Form = super(MyLPlugin, self).get_form(request, obj, **kwargs)

        # this is bit tricky, since i don't wont override add_view and
        # change_view
        class FakeForm(object):
            def __init__(self, Form, site):
                self.Form = Form
                self.site = site

                # base fields are required to be in this fake class, this may
                # do some troubles, with new versions of django, if there will
                # be something more required
                self.base_fields = Form.base_fields

            def __call__(self, *args, **kwargs):
                # instanciate the form on call
                form = self.Form(*args, **kwargs)
                # tell form we are on this site
                form.for_site(self.site)
                return form
        # TODO: Make sure this works
        if self.cms_plugin_instance.page and self.cms_plugin_instance.page.site:
            site = self.cms_plugin_instance.page.site
        elif self.page and self.page.site:
            site = self.page.site
        else:
            # this might NOT give the result you expect
            site = Site.objects.get_current()
        return FakeForm(Form, site)

plugin_pool.register_plugin(MyLPlugin)
