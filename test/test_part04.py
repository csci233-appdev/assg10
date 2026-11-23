import os
import sys
import django

# add in PYTHONPATH to location of the polls application, so we can import
os.environ['DJANGO_SETTINGS_MODULE'] = 'djangotutorial.mysite.settings'
sys.path.append('djangotutorial')
django.setup()
import polls.views

def test_templates_created():
    # results.html template is created in part 04 of the tutorial
    assert os.path.exists('djangotutorial/polls/templates')
    assert os.path.exists('djangotutorial/polls/templates/polls')
    assert os.path.exists('djangotutorial/polls/templates/polls/results.html')


def test_polls_views_added():
    # test that all of the views were added for polls app in part 3
    # the view function names are replaced with generic view classes in part 4
    assert getattr(polls.views, 'IndexView')
    assert getattr(polls.views, 'DetailView')
    assert getattr(polls.views, 'ResultsView')
    assert callable(getattr(polls.views, 'vote'))
