"""
This is for gathering information about the python environment and
determining function scope and calls

Todo:
    * Make a class for profiled functions
    * write function to validate if a function profiled
      is in scope
    * if a funciton isn't in scope find a module that has it (?)

"""

import ast
import types

# pylint: disable=too-few-public-methods
class ProfiledFunction(object):
    """
    Profiled function class for easily handing information
    and checks to see if it is in scope/what module
    the function could belong to

    Todo:
        - fix argument parsing
        - Write function for detecting if in scope
        - Write function to get module infomration
    """

    def __init__(self, args, keywords, function_id):
        self.args = [arg for arg in args]
        print(args)
        self.keywords = [x.arg for x in keywords]
        self.function_id = function_id


def imports():
    """
    Get a list of the currently imported modules
    """

    for _, val in globals().items():
        if isinstance(val, types.ModuleType):
            yield val.__name__


def parse_function(function_string):
    """
    Parse a function call to gather function name,
    args, and any keywords
    """

    if isinstance(function_string, str):
        call = ast.parse(function_string).body[0].value
        if isinstance(call, ast.Call):
            args = call.args
            keywords = call.keywords
            function_id = call.func.id

            return ProfiledFunction(args, keywords, function_id)
