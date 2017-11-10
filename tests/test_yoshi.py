"""
For testing
"""

from yoshi import environment_profile
import pytest
import pandas

def test_parse_function():
    """
    For testing generation of ProfiledFunctions
    """
    assert environment_profile.parse_function('my_func()').function_id == 'my_func'
    assert environment_profile.parse_function('yes') is None
    assert environment_profile.parse_function(0) is None
    assert environment_profile.parse_function('my_func(a,"doggie")').args == ['a', 'doggie']
    assert list(environment_profile.parse_function(
        'my_func(a,some_keyword="blarg")').keywords.keys()) == ['some_keyword']
    assert environment_profile.parse_function(
        'my_func(a,some_keyword="blarg")').keywords['some_keyword'] == 'blarg'
    assert environment_profile.parse_function('pandas.read_csv()').check_import_status() is True
