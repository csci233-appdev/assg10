---
title: 'Assignment 10: Django Web Framework Tutorial'
author: 'CSci 233: Application Program Development w/ Python'
date: ''
---

# Objectives

- Become familiar with web frameworks and some of the basics of creating
  web based applications.
- Learn the basics of the Django web framework and how it works.
- Become familiar with the model-view-controller pattern in practice.
- See how object-relational mapping works in a application that uses
  Python OOP to map to a relational database.

# Description



## Assignment Prerequisites and Setup

Before performing any assignment in this class, you need to have
the following tasks already completed.

1. You need to have `git` tools installed on your system so that you
   can successfully clone repositories and create commits.
2. You need to have a GitHub account created.
   - You need to have successfully created a ssh key so that you can
     authenticate with and push commits back to git.
3. You need a working Python 3 distribution installed on the system you
   will work on these assignments with, that you can run Python scripts
   and the Python IDLE interface within.

See our class 
[Getting Started with Python and Git for Class Assignments](https://github.com/etamu-class/python-git)
for links on setting up these needed development environment tools and configuration.


# Assignment Questions

Start by cloning the assignment repository that was created for
you when you accepted the assignment.  This assignment is a bit different
from our previous ones, you will be completing the most recent tutorial
for the Django framework.  See the description below for some more details.

You should answer each of the following questions by writing appropriate
Python code to solve the stated task.  Once you are satisfied with
your answer, you should create a commit and push it back to your
GitHub repository for grading.  In general you should do each
question as a separate commit 
(see [Git Best Practices](https://gist.github.com/luismts/495d982e8c5b1a0ced4a57cf3d93cf60)).

Each commit you push to GitHub will create a release that will be
graded.  Look at the `Releases` on the right hand side of your `Code`
page to see a summary of your grade results.  Also the instructor
will give feedback for all assignments in your `Feedback` Pull request.
See the `Feedback` pull request listed on GitHub on the `Pull requests`
tab.

You can and should test your code locally before creating commits
and submitting it to GitHub.  As mentioned, since you are now writing
functions for your assignments, we are now using the `pytest` unit
testing module in your autograder and to run tests against your work.
So for example, to run the tests for question 01, from the command line you
can do:

```bash
$ python3 -m pytest -v -s test/test_part01.py 
======================================== test session starts =========================================
platform linux -- Python 3.14.10, pytest-9.2.0, pluggy-1.7.0 -- /opt/base/bin/python3
cachedir: .pytest_cache
rootdir: /workspaces/assg10-solution
collected 3 items                                                                                    

test/test_part01.py::test_project_created PASSED
test/test_part01.py::test_polls_app_created PASSED
test/test_part01.py::test_polls_view_added PASSED

========================================= 3 passed in 0.02s ==========================================
```

There should be tests for each tutorial part in the `test` subdirectory,
named `test_part01.py`, `test_part02.py`, etc. for the Django tutorial.
These will be (some of) the same `pytest` tests that are run by the autograder
when you submit your work.

## Writing your first Django app, Install Django

The tutorial and other documentation you need can be found on the
[Django web framework project Documentation](https://docs.djangoproject.com/en/6.1/).

You should start by reading the Overview and the Installation instructions
given as links in the Django project documentation.

You will need to install the Django framework.  See the 
[Installation](https://docs.djangoproject.com/en/6.1/intro/install/)
link in the documentation form more information.  If you are using
the class development environment, and/or the python pip package manager
you ought to be able to install Django doing something like:

```bash
$ python3 -m pip install Django
```

**Note**: You may need to use `sudo` if you are on a Linux / MacOS environment and your
Python environment is set up being managed by the root user.

As mentioned in the Installation instructions, make sure that Django is
successfully installed and available in the environment where you are
doing your assignment before proceeding

```bash
$ python3
Python 3.14.10 (main, Nov  5 2026, 09:34:56) [GCC 14.2.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
Ctrl click to launch VS Code Native REPL (https://aka.ms/python-native-repl)
>>> import django
>>> print(django.__version__)
6.1.3
```


## Writing your first Django app, Tutorial parts 1-8

You are required to complete all 8 parts of the
[Django Tutorial](https://docs.djangoproject.com/en/6.1/intro/tutorial01/)
starting with the first part.  The assignment has
tests to be run on successful completion of each part, which will also
be run in the autograder:

```bash
$ python3 -m pytest -v -s test/test_part01.py 
======================================== test session starts =========================================
platform linux -- Python 3.14.10, pytest-9.2.0, pluggy-1.7.0 -- /opt/base/bin/python3
cachedir: .pytest_cache
rootdir: /workspaces/assg10-solution
collected 3 items                                                                                    

test/test_part01.py::test_project_created PASSED
test/test_part01.py::test_polls_app_created PASSED
test/test_part01.py::test_polls_view_added PASSED

========================================= 3 passed in 0.02s ==========================================

```

As with our past assignments in the class, you are required to
demonstrate incremental progress on the tutorial.  So you should create
a commit on the successful completion of each part of the tutorial, and
push it to your GitHub classroom for autograding.

# Assignment Conclusion / Checklist

Hopefully you have created commits after completing each question and pushed
them successfully to your assignment repository.  Make sure that you
do the following for this and all class assignments.

- Check your autograder results after pushing your commits.  Look
  in your `Feedback` pull request, and in the detailed autograder
  report generated for your release(s) made for each commit.
- You should never close or merge your `Feedback` pull request, as is
  mentioned in the comment.  The instructor will evaluate your assignments,
  and may give you feedback about your code or work.  Check here after
  the assignment is returned for a code review and assignment comments.
- In general this class will ask you to follow and use good Python
  style as specified by the official
  [Python PEP 8 Style guide](https://peps.python.org/pep-0008/).
  You should at least pay attention to
  - All indentation is required to be 4 spaces with no tabs in files.
  - Maximum line lengths should be usually observed, do not generally
    extend code past the 79 character column in a file.
  - Follow the suggestions for breaking long lines in code (e.g. line
    break before binary operators in a long expressions).
  - Prefer single quotes for all string in code for class assignments,
    unless you need a string with a single quote, for example to
    add an apostrophe 's.
  - Follow Pep8 style for whitespace in expressions and statements.  
    For example, usually a single space should go before and after
    all binary operators in expressions.
  - We encourage the use of function annotations in Python code.
- Also in general in this class we will ask you to follow
  [Git Commit Best Practices](https://gist.github.com/luismts/495d982e8c5b1a0ced4a57cf3d93cf60)
- Strive to use 
  [Meaningful Names](https://www.freecodecamp.org/news/how-to-write-better-variable-names/)
  for variables, constants and functions in your code.  You are required
  to follow Pep8 naming guidelines, which means `snake_case` names
  for variables and functions and `SCREAMING_SNAKE_CASE` for 
  constants.  Python style switches to `PascalCase` for 
  class names.

Make sure you are checking review comments and code review given
for your class assignments.  We may start by making suggestions where your
style or practices could be improved.  As the class progresses, some
of these suggestions may become requirements, especially for students who
are repeatedly making the same style or practice error and are not
following feedback to correct a noted issue in future assignments.
Assignments may be left ungraded in some cases for style or practice
issues until corrected, and/or may have points removed or receive
a 0 grade if issues continue after receiving multiple feedback that
are repeatedly ignored and not corrected.

# Additional Information

The following are suggested online materials you may use to help you understand
the tools and topics we have introduced in this assignment.

- [Python PEP 8 Style guide](https://peps.python.org/pep-0008/)
- [Git Commit Best Practices](https://gist.github.com/luismts/495d982e8c5b1a0ced4a57cf3d93cf60)
- [Git Best Practices](https://gist.github.com/pandeiro/1552496)
- [Best Practices to Write Readable and Maintainable Code: Choosing meaningful names](https://dev.to/pacheco/how-do-you-name-things-3jae)
- [How to Write Better Names for your Variables, Functions and Classes](https://www.freecodecamp.org/news/how-to-write-better-variable-names/)