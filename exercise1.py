#!/usr/bin/env python3

""" Assignment 3, Exercise 2, INF1340, Fall, 2015. DBMS

This module performs table operations on database tables
implemented as lists of lists. """

__author__ = 'Piaoyao Shi & Zixiao Yang & Ming Fu '
__email__ = "piaoyao.shi@mail.utoronto.ca & zeke.yang@mail.utoronto.ca & mm.fu@mail.utoronto.ca"
__copyright__ = "2015 Piaoyao Shi & Zixiao Yang & Ming Fu"


#####################
# HELPER FUNCTIONS ##
#####################

def remove_duplicates(l):
    """
    Removes duplicates from l, where l is a List of Lists.
    :param l: a List
    :return result: the resulting table
    """

    d = {}
    result = []
    for row in l:
        if tuple(row) not in d:
            result.append(row)
            d[tuple(row)] = True

    return result


class UnknownAttributeException(Exception):
    """
    Raised when attempting set operations on a table
    that does not contain the named attribute
    """
    pass


def check_is_empty(res):
    """
    Assign None value to res if the table res is empty or only has a header.
    :param res: a list
    :return:res: None object
    """
    if len(res) <= 1:
        res = None
    return res

##################
# Main Functions #
##################


def selection(t, f):
    """
    Return the result of performing operation f on table t.
    Return None if the resulting table res is an empty (or only has the header).
    :param t: a list
    :param f: a function
    :return res: the resulting table

    Example:
    > R = [["A", "B", "C"], [1, 2, 3], [4, 5, 6]]
    ># Define function f that returns True iff
    > # the last element in the row is greater than 3.
    > def f(row): row[-1] > 3
    > select(R, f)
    [["A", "B", "C"], [4, 5, 6]]
    """

    res = None
    if t and t[0]:               # The if statement will execute if the table is not empty and has a header.
        res = [t[0]]
        for i in xrange(1, len(t)):
            # xrange() is intended to be simple and fast, when the range is large or range elements are never used.
            if f(t[i]):          # The if statement will execute if the function return True.
                res.append(t[i])
        res = remove_duplicates(res)
        res = check_is_empty(res)
    return res


def projection(t, r):
    """
    Perform projection operation on table t, using the attributes subset r.
    Return None if the resulting table res is empty.

    :param  t: a list
    :param  r: a list
    :return res: the resulting table
    :raise: MismatchedAttributesException:
            when attempting set operations on a table that does not contain the named attribute

    Example:
    > R = [["A", "B", "C"], [1, 2, 3], [4, 5, 6]]
    > projection(R, ["A", "C"])
    [["A", "C"], [1, 3], [4, 6]]

    """

    res = None

    if (not t) or (not t[0]):  # As required,if the testing table is empty or the header is empty, raise an error.
        raise UnknownAttributeException

    if t and t[0]:        # The if statement will execute if the table is not empty and has a header
        # Create check table and insert "UnknownColumn" element if t does not contain the attr in r for each attr in r.
        check = ["UnknownColumn" for attr in r if attr not in t[0]]
        if check:         # The if statement will execute if the check table is not empty
            raise UnknownAttributeException

        # Create indices table, add index in t for each attribute in r
        indices = [t[0].index(attr) for attr in r]
        res = []
        for k in xrange(len(t)):
            res.append([t[k][i] for i in indices])
        if not res:
            res = None
        else:
            res = remove_duplicates(res)
            res = check_is_empty(res)
    return res


def cross_product(t1, t2):
    """
    Return the cross-product of tables t1 and t2.
    Return None if the resulting table res is an empty.
    :param t1: a list
    :param t2: a list
    :return res: the resulting table

    Example:
    > R1 = [["A", "B"], [1,2], [3,4]]
    > R2 = [["C", "D"], [5,6]]
    [["A", "B", "C", "D"], [1, 2, 5, 6], [3, 4, 5, 6]]

    """

    res = None

    if t1 and t2:                    # The if statement will execute if the tables t1 and t1 are not empty.
        res = []
        for n in xrange(1, len(t1)):        # if t1 only has the header, the for loop will not execute.
            for i in xrange(1, len(t2)):    # if t2 only has the header, the for loop will not execute.
                res.append(t1[n] + t2[i])

        res.insert(0, t1[0] + t2[0])  # insert header at the beginning of the list.
        res = remove_duplicates(res)
        res = check_is_empty(res)

    return res
