################################################################################
# Name: James A. Chase
# File: asserts.py
# Date: 27 May 2024
# Description:
#
# Holds custom assert functions that allow my code to be cleaner.
#
################################################################################

# imports
from typing import Any, Type, Iterable, Tuple
from os.path import exists

def assertType(e: Type, a: Type) -> None:
    '''
    Asserts if the types of two objects are equal.

    Parameters:
        - e: the expected value
        - a: the actual value

    Returns: None
    '''
    if e != a:
        raise AssertionError(f'Expected: {e} - Actual: {a}')
    
def assertTypes(e: Tuple[Type, ...], a: Type) -> None:
    '''
    Asserts if the type of an object is in an expected group of typing

    Parameters:
        - e: the expected value
        - a: the actual value

    Returns: None
    '''
    if a not in e:
        raise AssertionError(f'Expected: {e} - Actual: {a}')
    
def assertLength(e: int, a: Iterable) -> None:
    '''
    Asserts an iterable's length is the expected value

    Parameters:
        - e: the expected value
        - a: the actual value

    Returns: None
    '''
    if e != len(a):
        raise AssertionError(f'Expected: {e} - Actual: {a}')
    
def assertExists(path: str) -> None:
    '''
    Asserts that the given path exists

    Parameters:
        - path: a string containing the path to test

    Returns: None
    '''
    if not exists(path):
        raise AssertionError(f'Path does not exist: {path}')
    
def notMain(msg: str) -> None:
    '''
    Prevents user from running a class or module file.

    Parameters:
        - msg: a string containing the message to be printed when error is \
               thrown

    Returns: None
    '''
    raise AssertionError(msg)

if __name__ == '__main__':
    notMain('This is a module. Import its contents into another file.')
