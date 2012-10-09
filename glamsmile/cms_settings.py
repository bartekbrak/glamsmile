from django.utils.translation import ugettext_lazy as _

CMS_TEMPLATES = (
    ('index.html', _('Index')),
    ('sub.html', _('Subpage')),
)

CMS_LANGUAGES = (
    ('pl', 'PL'),
    # ('en', 'EN'),
)

# 'name': _('Bubble Icons'),
# 'extra_context': {'css_class': 'bubble', 'more': 'yes'},
CMS_PLACEHOLDER_CONF = {
    'large_frame_placeholder': {
        'plugins': 'TextPlugin',
        'limits': {
            'TextPlugin': 1
        }
    },
    'last_small_frame': {
        'plugins': 'TextPlugin',
        'limits': {
            'TextPlugin': 1
        }
    },
    'three_smaller_frames': {
        'plugins': 'MyLPlugin',
        'limits': {
            'MyLPlugin': 3
        }
    },
    'col1': {
        'plugins': 'TextPlugin',
        'limits': {
            'TextPlugin': 1
        }
    },
    'col2': {
        'plugins': 'TextPlugin',
        'limits': {
            'TextPlugin': 1
        }
    },
    'keywords': {
        'plugins': 'LinkPlugin',
    },
    'languages': {
        'plugins': 'LinkPlugin',
        'extra_context': {'separator': ' - '},
    },

}
