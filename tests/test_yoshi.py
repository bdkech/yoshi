from yoshi import environment_profile
import pytest

def test_parse_function():
    assert(environment_profile.parse_function('my_func()'))
    assert(environment_profile.parse_function('yes'))
    #assert(environment_profile.parse_function(0))
    assert(environment_profile.parse_function('my_func()'))
    assert(environment_profile.parse_function('my_func(a,b.c)'))
    assert(environment_profile.parse_function('my_func(a,some_keyword="blarg")'))
