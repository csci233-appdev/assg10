import os
import sys
import django

# add in PYTHONPATH to location of the polls application, so we can import
os.environ['DJANGO_SETTINGS_MODULE'] = 'djangotutorial.mysite.settings'
sys.path.append('djangotutorial')
django.setup()
from polls.models import Question
from polls.models import Choice
from django.contrib.auth.models import User
import polls.admin
from polls.admin import QuestionAdmin
import mysite.settings

def test_admin_models_registered_and_customized():
    #assert file_has_line('djangotutorial/polls/admin.py', 'admin.site.register(Question)')
    assert getattr(polls.admin, 'QuestionAdmin')
    assert getattr(polls.admin, 'ChoiceInline')
    assert issubclass(polls.admin.ChoiceInline, django.contrib.admin.TabularInline)

def test_admin_change_list_customized():
    assert "question_text" in QuestionAdmin.list_display
    assert "pub_date" in QuestionAdmin.list_display    
    assert "was_published_recently" in QuestionAdmin.list_display
    assert "question_text" in QuestionAdmin.search_fields    

def test_customize_project_templates():
    assert 'templates' in str(mysite.settings.TEMPLATES[0]['DIRS'])
    assert os.path.exists('djangotutorial/templates')
    assert os.path.exists('djangotutorial/templates/admin')
    assert os.path.exists('djangotutorial/templates/admin/base_site.html')
    # This was mentioned as extra in tutorial part 07
    assert os.path.exists('djangotutorial/templates/admin/index.html') 
