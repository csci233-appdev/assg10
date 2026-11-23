import os

def test_static_and_style_files_created():
    # created static files and css styles in part 6 of the tutorial
    assert os.path.exists('djangotutorial/polls/static')
    assert os.path.exists('djangotutorial/polls/static/polls')
    assert os.path.exists('djangotutorial/polls/static/polls/style.css')
    assert os.path.exists('djangotutorial/polls/static/polls/images')
    assert os.path.exists('djangotutorial/polls/static/polls/images/background.png')

