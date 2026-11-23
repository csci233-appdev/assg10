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
    # check that the URLConf patterns for the polls view have been added to
    # app and to the overall mysite
    # not sure if I want to check like this, probably just look at these by hand and confirm
    # the whole web app runs for students
    # probably best not to search file for lines of code, import it and test directly
    #assert file_has_line('djangotutorial/mysite/settings.py', "TIME_ZONE = 'America/Chicago'")
    #assert file_has_line('djangotutorial/mysite/settings.py', "'polls.apps.PollsConfig',")
    assert mysite.settings.TIME_ZONE == 'America/Chicago'
    assert 'polls.apps.PollsConfig' in mysite.settings.INSTALLED_APPS 

def test_mysite_database_tables():
    # in part 2, before adding in additional Models / database tables,
    # the initial migration is done that creates the admin interface and other
    # app tables used in the tutorial app
    dbfile = 'djangotutorial/db.sqlite3'
    assert os.path.exists(dbfile)
    assert table_exists(dbfile, 'auth_group')
    assert table_exists(dbfile, 'auth_group_permissions')
    assert table_exists(dbfile, 'auth_permission')
    assert table_exists(dbfile, 'auth_user')
    assert table_exists(dbfile, 'auth_user_groups')
    assert table_exists(dbfile, 'auth_user_user_permissions')
    assert table_exists(dbfile, 'django_admin_log')
    assert table_exists(dbfile, 'django_content_type')
    assert table_exists(dbfile, 'django_migrations')
    assert table_exists(dbfile, 'django_session')

def test_polls_has_models():
    # probably shouldn't use direct search for line of code, instead
    # use introspection and import the actual Django files to test them
    #assert file_has_line('djangotutorial/polls/models.py', 'class Question(models.Model')
    #assert file_has_line('djangotutorial/polls/models.py', 'class Choice(models.Model')
    assert callable(getattr(Question, 'was_published_recently'))
    assert callable(getattr(Question, '__str__'))
    assert callable(getattr(Choice, '__str__'))


def test_polls_database_tables():
    dbfile = 'djangotutorial/db.sqlite3'
    assert os.path.exists(dbfile)
    assert table_exists(dbfile, 'polls_choice')
    assert table_exists(dbfile, 'polls_question')

def test_api_played_with():
    # Test that the Question and Choice where creaated by "Playing with the
    # API"
    # NOTE: not sure if we can keep these tests, the objects may change
    # as proceed through the tutorial...
    query_set = Question.objects.all()
    assert len(query_set) == 1
    q = query_set[0]
    assert q.id == 1
    assert q.question_text == "What's up?"

    choice_set = q.choice_set.all()
    assert len(choice_set) == 2
    c = choice_set[0]
    assert c.id == 1
    assert c.choice_text == 'Not much'
    c = choice_set[1]
    assert c.id == 2
    assert c.choice_text == 'The sky'

def test_admin_user_created():
    user_set = User.objects.all()
    u = user_set[0]
    assert u.id == 1
    assert u.username == 'admin'
    assert u.email == 'admin@example.com'

def test_admin_models_registered():
    # This is modifiedin part 07 when we start customizing the admin
    # forms
    #assert file_has_line('djangotutorial/polls/admin.py', 'admin.site.register(Question)')
    pass