from ..cache import get_hashed_mtime
# get_cache_key, get_hexdigest,
from ..settings import STYLUS_EXECUTABLE
#, STYLUS_USE_CACHE,\STYLUS_CACHE_TIMEOUT, STYLUS_OUTPUT_DIR
# from ..utils import URLConverter
# from django.conf import settings
# from django.core.cache import cache
from django.template.base import Library
# , Node
# import logging
# import shlex
# import subprocess
import os
import sys


# logger = logging.getLogger("stylus")
register = Library()


@register.simple_tag
def stylus(path):
    from django.contrib.staticfiles.finders import AppDirectoriesFinder
    finder = AppDirectoriesFinder()

    encoded_full_path = full_path = finder.find(path)
    if isinstance(full_path, unicode):
        filesystem_encoding = sys.getfilesystemencoding() or sys.getdefaultencoding()
        encoded_full_path = full_path.encode(filesystem_encoding)

    relative_path, filename = os.path.split(path)

    output_directory = os.path.split(full_path)[0]
    hashed_mtime = get_hashed_mtime(full_path)

    if filename.endswith(".styl"):
        base_filename = filename[:-5]
    else:
        base_filename = filename

    output_filename = "%s-%s.css" % (base_filename, hashed_mtime)
    output_path = os.path.join(output_directory, output_filename)
    if not os.path.exists(output_path):
        command = "%s < %s > %s" % (STYLUS_EXECUTABLE, encoded_full_path, output_path)
        os.system(command)

        # Remove old files
        compiled_filename = os.path.split(output_path)[-1]
        for old_filename in os.listdir(output_directory):
            if old_filename.startswith(base_filename) and old_filename != compiled_filename and old_filename != filename:
                os.remove(os.path.join(output_directory, old_filename))
                print "    stylus removed", os.path.join(output_directory, old_filename)

    return "%s/%s" % (relative_path, output_filename)
