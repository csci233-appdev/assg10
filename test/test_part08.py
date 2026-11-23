import os
import sys
import django

from utils import file_has_line
from utils import table_exists

# add in PYTHONPATH to location of the polls application, so we can import
os.environ['DJANGO_SETTINGS_MODULE'] = 'djangotutorial.mysite.settings'
sys.path.append('djangotutorial')
django.setup()
from polls.models import Question
from polls.models import Choice
from django.contrib.auth.models import User
import mysite.settings


def test_mysite_settings_configured():
    # test the debug toolbar was added in part 08
    assert 'debug_toolbar' in mysite.settings.INSTALLED_APPS 
    assert 'debug_toolbar.middleware.DebugToolbarMiddleware' in mysite.settings.MIDDLEWARE
    assert '127.0.0.1' in mysite.settings.INTERNAL_IPS
