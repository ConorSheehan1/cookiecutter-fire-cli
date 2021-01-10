# Standard Library
import unittest
from unittest.mock import call, patch

# Third party
from termcolor import colored

# {{cookiecutter.repo_name}}
from {{cookiecutter.repo_name}} import {{cookiecutter.repo_name}}


class Test{{cookiecutter.repo_name}}(unittest.TestCase):
    def test_default_args(self):
        assert {{cookiecutter.repo_name}}() == "bar"

    def test_foo(self):
        assert {{cookiecutter.repo_name}}(foo=True) == "foo"
