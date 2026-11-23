import os
import subprocess


def test_polls_application_tests_run_successfully():
    # run the tests added in part 05 using the django manager.py to execute them
    # a bit strange, but we want to test the basic Python unit tests were actually
    # added and run using the django framework setup
    os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'
    command = ['python3', 'djangotutorial/manage.py', 'test', 'polls']
    result = subprocess.run(command, capture_output=True)
    assert result.returncode == 0
    # if tutorial part 05 is followed, we expect 10 tests were found and run
    assert "Found 10 test(s)" in str(result.stdout)

