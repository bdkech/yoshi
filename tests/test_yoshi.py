"""
For testing
"""

from yoshi import environment_profile
import pytest


def test_parse_function():
    """
    For testing generation of ProfiledFunctions
    """
    assert environment_profile.parse_function('my_func()').function_id == 'my_func'
    assert environment_profile.parse_function('yes') is None
    assert environment_profile.parse_function(0) is None
    #assert environment_profile.parse_function('my_func(a,b.c)').args == ['a', 'b.c']
    assert environment_profile.parse_function(
        'my_func(a,some_keyword="blarg")').keywords == ['some_keyword']
