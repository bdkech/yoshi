# Author : Bobak Kechavarzi
"""
This is for gathering information about the python environment and
determining function scope and calls
"""

import ast
import types
import builtins


def get_arg_label(my_arg):
    """
    Get arguments from ast parsing and their type
    return their text representation, either a variable
    or string
    """

    # Args can either be named objects or inputted
    # strings determine which and give back the their name
    # This is an object, has an id for a label
    if hasattr(my_arg, "id"):
        return my_arg.id
    # This is a string, use the text as the label
    elif hasattr(my_arg, "s"):
        return my_arg.s


# pylint: disable=too-few-public-methods
class ProfiledFunction(object):
    """
    Profiled function class for easily handing information
    and checks to see if it is in scope/what module
    the function could belong to.
    """

    def __init__(self, args, keywords, function_id):
        self.args = [get_arg_label(arg) for arg in args]
        # check if args are strings or names, then store them
        # as necessary
        kword_tup = [(x.arg, x.value.s) for x in keywords]
        self.keywords = dict((x, y) for x, y in kword_tup)
        self.function_id = function_id


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
            if hasattr(call.func, 'id'):
                function_id = call.func.id
            elif hasattr(call.func, 'attr'):
                function_id = call.func.attr

            return ProfiledFunction(args, keywords, function_id)
