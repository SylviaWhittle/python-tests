# Python has a built-in unit testing module, unittest, however this is cumbersome and doesn't scale well. 
# Pytest is a feature-rich, plugin-based ecosystem for testing your Python code. 

# Most functional tests follow the Arrange-Act-Assert model:
# 1 - Arrange the conditions for the test
# 2 - Act by calling some function or method
# 3 - Assert that some end condition is true

# Here is how one would do it in unittest:

# from unittest import TestCase

# class TryTesting(TestCase):
#     def test_always_passes(self):
#         self.assertTrue(True)

#     def test_always_fails(self):
#         self.assertTrue(False)

# These tests can be run using the discover option of unittest:
# (venv) sylvi@Sylvias-MacBook-Pro Pytest % python -m unittest discover
# F.
# ======================================================================
# FAIL: test_always_fails (testing.TryTesting)
# ----------------------------------------------------------------------
# Traceback (most recent call last):
#   File "/Users/sylvi/Documents/GitKraken/python-tests/Pytest/testing.py", line 18, in test_always_fails
#     self.assertTrue(False)
# AssertionError: False is not true

# ----------------------------------------------------------------------
# Ran 2 tests in 0.000s

# FAILED (failures=1)

# This is a rather cumbersome method for doing the tests, in all, we had to:
# - Import the TestCase class from unittest
# - Create TryTesting, a subclass of TestCase
# - Write a method in TryTesting for each test
# - Use one of the self.assert* methods from unittest.TestCase to make assertions

# This is significant becuase it is the MINIMUM amount of code that needs to be written for any test. 
# This results in a lot of boilerplate code. 
# Pytest simplifies this workflow by allowing you to use normal function and Python's assert keyword directly:

# test with pyttest

# def test_always_passes():
#     assert True

# def test_always_fails():
#     assert False

# Requirements:
# testing functions must start with "test_"
# files that contain the tests must start with "test_"

# Because you can use the assert keyword, you don't need to learn or remember all the different self.assert* methods in unittest either. 
# If you can write an expression that you expect to evaluate to True, pytest can test it. 
# Pytest also provides a much better output:

# (venv) sylvi@Sylvias-MacBook-Pro Pytest % pytest
# ===================================================================================================== test session starts ======================================================================================================
# platform darwin -- Python 3.10.4, pytest-7.1.2, pluggy-1.0.0
# rootdir: /Users/sylvi/Documents/GitKraken/python-tests/Pytest
# collected 2 items                                                                                                                                                                                                              

# test_.py .F                                                                                                                                                                                                              [100%]

# =========================================================================================================== FAILURES ===========================================================================================================
# ______________________________________________________________________________________________________ test_always_fails _______________________________________________________________________________________________________

#     def test_always_fails():
# >       assert False
# E       assert False

# test_.py:52: AssertionError
# =================================================================================================== short test summary info ====================================================================================================
# FAILED test_.py::test_always_fails - assert False
# ================================================================================================= 1 failed, 1 passed in 0.01s ==================================================================================================



# Easier to manage State and Dependencies 

# With unittest, you might extract dependencies into .setUp() and .tearDown() methods so that each test in the class can make use of them. Using these methods gets very large very quickly.
# This method also introduces a lot of implicit dependencies - hidden dependencies that are hard to notice. 

# Pytest takes a different approach, it leads you to explicit dependency declarations that are still reusable thanks to the availability of fixtures.
# Fixtures are functions that can create data, test doubles, or initialize system sate for the test suite. Any test that wants to use a fixture must explicitly use this fixture function as an argument to the test function so depencencides are always stated up front.:

# import pytest

# @pytest.fixture
# def example_fixture():
#     return 1

# def test_with_fixture(example_fixture):
#     assert example_fixture == 1

# This allows us to see immediately that it depends on a fixture without needing to check the whole file for fixture definitions. 


# Easy to filter tests

# As the test suite grows, you may find that you want to run just a few tests on a feature and save the full suite for later. Pytest allows a few ways of doing this:

# - Name-based filtering:
    # You can limit pytest to running only those tests whose fully qualified names match a particular expression. You can do this with the -k parameter.
# - Directory scoping 
    # By default, pytest will run only those tests that are in or under the current directory. 
# Test catergorization
    # Pytest can include or exclude tests from particlular categories that you define. You can do this with the -m parameter. 

# Test categorization is a particularly useful tool. Pytest enables you to create marks or custom labels for any test that you like. 
# A test may have mutlpile labels and you can use  them for granular control over which tests to run.


# Test parameterisation

# When testing functions that process data or perform generic transformations, you'll find yourself writing many similar tests. They may differ only in the input or output of the code being tested. 
# This requires ducplicating test code and doing so can sometimes obscure the behaviour that you're trying to test.
# Unittest offers a way of collecting several tests into one, but they don't show up as individual tests in result reports. If one test fails and the rest pass, then the entire group will still return a single failing result.
# Pytest offers its own solution in which each test can pass or fail independently. 

# Plugin-Based Architecture

# One of the most useful features of pytest is its openness to customization and new features. Almost every piece of the program can be opened and changed. As a result, pytest users have developed a rich ecosystem of helpful plugins. 
#  Although some pytest plugins focus on specific frameworks like Django, others are applicable to most test suites. 

# Fixtures in-depth

# Fixutures are a way of prividng data, test doubles or state setup to the tests. 
# Fixturs are function sthat can return a wide range of values. Each test that dpeends on a fixture must explicitly accept that fixture as an argument. 

# Simulating a typical test-driven-development (TDD) workflow

import pytest

def format_data_for_display(people):
    list = [f"{person['given_name']} {person['family_name']}: {person['title']}" for person in people]
    return list

# def test_format_data_for_display():
#     people = [
#         {
#             "given_name": "Alfonsa",
#             "family_name": "Ruiz",
#             "title": "Senior Software Engineer",
#         },
#         {
#             "given_name": "Sayid",
#             "family_name": "Khan",
#             "title": "Project Manager",
#         },
#     ]

#     assert format_data_for_display(people) == [
#         "Alfonsa Ruiz: Senior Software Engineer",
#         "Sayid Khan: Project Manager",
#     ]

def format_data_for_excel(people):
    string = """"""
    for person_index, person in enumerate(people):
        keys = person.keys()
        print(f'keys: {keys}')
        for index, key in enumerate(keys):
            if key not in string.split('\n')[0]:
                string += (key)
                if index < len(keys) - 1:
                    string += (',')
                else:
                    string += ('\n')
        for index, value in enumerate(person.values()):
            string += (value)
            if index < len(person.values()) - 1:
                string += (',')
        if person_index < len(people) - 1:
            string += ('\n')
    print(string)
    return string




# def test_format_data_for_excel():
#     people = [
#         {
#             "given_name": "Alfonsa",
#             "family_name": "Ruiz",
#             "title": "Senior Software Engineer",
#         },
#         {
#             "given_name": "Sayid",
#             "family_name": "Khan",
#             "title": "Project Manager",
#         },
#     ]

#     assert format_data_for_excel(people) == """given_name,family_name,title
# Alfonsa,Ruiz,Senior Software Engineer
# Sayid,Khan,Project Manager"""


# Both of these tests have to repeat the definition of the people variable. 
# We can re-use the people variable using a fixture:

@pytest.fixture
def example_people_data():
    return [
        {
            "given_name": "Alfonsa",
            "family_name": "Ruiz",
            "title": "Senior Software Engineer",
        },
        {
            "given_name": "Sayid",
            "family_name": "Khan",
            "title": "Project Manager",
        },
    ]

def test_format_data_for_display(example_people_data):
    assert format_data_for_display(example_people_data) == [
        "Alfonsa Ruiz: Senior Software Engineer",
        "Sayid Khan: Project Manager",
    ]

def test_format_data_for_excel(example_people_data):
    assert format_data_for_excel(example_people_data) == """given_name,family_name,title
Alfonsa,Ruiz,Senior Software Engineer
Sayid,Khan,Project Manager"""