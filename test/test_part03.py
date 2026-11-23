import os
import sys
import django
from utils import file_has_line


# add in PYTHONPATH to location of the polls application, so we can import
os.environ['DJANGO_SETTINGS_MODULE'] = 'djangotutorial.mysite.settings'
sys.path.append('djangotutorial')
django.setup()
import polls.views
import polls.urls

def test_polls_views_added():
    # test that all of the views were added for polls app in part 3
    # the view function names are replaced with generic view classes in part 4
    #assert callable(getattr(polls.views, 'index'))
    #assert callable(getattr(polls.views, 'detail'))
    #assert callable(getattr(polls.views, 'results'))
    assert callable(getattr(polls.views, 'vote'))

def test_templates_created():
    assert os.path.exists('djangotutorial/polls/templates')
    assert os.path.exists('djangotutorial/polls/templates/polls')
    assert os.path.exists('djangotutorial/polls/templates/polls/detail.html')
    assert os.path.exists('djangotutorial/polls/templates/polls/index.html')

def test_url_polls_app_namespacing():
    assert polls.urls.app_name == 'polls'
    assert file_has_line('djangotutorial/polls/templates/polls/index.html', "url 'polls:detail'")

