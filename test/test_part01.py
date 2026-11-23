import os
from utils import file_has_line


def test_project_created():
    # test project sturcture from $ django-admin startproject  mysite djangotutorial was
    # successfully completed
    assert os.path.exists('djangotutorial')
    assert os.path.exists('djangotutorial/manage.py')
    assert os.path.exists('djangotutorial/mysite')
    assert os.path.exists('djangotutorial/mysite/__init__.py')
    assert os.path.exists('djangotutorial/mysite/asgi.py')
    assert os.path.exists('djangotutorial/mysite/settings.py')
    assert os.path.exists('djangotutorial/mysite/urls.py')
    assert os.path.exists('djangotutorial/mysite/wsgi.py')

def test_polls_app_created():
    # test that the polls app was created using $ python manage.py startapp polls
    assert os.path.exists('djangotutorial/polls')
    assert os.path.exists('djangotutorial/polls/__init__.py')
    assert os.path.exists('djangotutorial/polls/admin.py')
    assert os.path.exists('djangotutorial/polls/apps.py')
    assert os.path.exists('djangotutorial/polls/models.py')
    assert os.path.exists('djangotutorial/polls/tests.py')
    assert os.path.exists('djangotutorial/polls/views.py')

def test_polls_view_added():
      # check that the URLConf patterns for the polls view have been added to
      # app and to the overall mysite
      # not sure if I want to check like this, probably just look at these by hand and confirm
      # the whole web app runs for students
      # the view function to call is modified in part 4
      #assert file_has_line('djangotutorial/polls/urls.py', 'path("", views.index, name="index")')
      assert file_has_line('djangotutorial/mysite/urls.py', 'path("polls/", include("polls.urls"))')
