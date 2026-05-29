import pytest
from main import clean_code


def test_remove_trailing_whitespace():
    assert clean_code("hello   \nworld  ") == "hello\nworld"


def test_collapse_multiple_blank_lines():
    assert clean_code("a\n\n\n\nb") == "a\n\nb"


def test_empty_string():
    assert clean_code("") == ""


def test_already_clean():
    code = "def foo():\n    return 1"
    assert clean_code(code) == code
