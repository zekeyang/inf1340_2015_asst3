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


def selection(t, f):
    """
    Return the result of performing operation f on table t.
    Return NONE if the result is an empty table.

    To do: +add param:

    Example:
    > R = [["A", "B", "C"], [1, 2, 3], [4, 5, 6]]
    ># Define function f that returns True iff
    > # the last element in the row is greater than 3.
    > def f(row): row[-1] > 3
    > select(R, f)
    [["A", "B", "C"], [4, 5, 6]]
    NOTE: NameError exception ?? why we need to name error ?
    """

    return_table = None
    if t and t[0]:
        # set header
        return_table = [t[0]]
        for i in xrange(1, len(t)):
            # adding one row at a time if applicable
            if f(t[i]):
                return_table.append(t[i])
        # check if the table is empty
        if len(return_table) == 1:
            # header only means empty, return nothing
            return_table = None
        else:
            return_table = remove_duplicates(return_table)
    return return_table


def projection(t, r):
    """
    Perform projection operation on table t, using the attributes subset r.
    Return NONE if the result is an empty table.

    To do: +add param:

    Example:
    > R = [["A", "B", "C"], [1, 2, 3], [4, 5, 6]]
    > projection(R, ["A", "C"])
    [["A", "C"], [1, 3], [4, 6]]

    """
    # check if each item in r exists in table t schema
    # return the position of each item
    # list all value in table t with the projected position


    res = None

    if t and t[0]:
        check = ["UnknownColumn" for attr in r if attr not in t[0]]
        # check if named column was exist in the table
        # if not then raise error
        if check:
            raise UnknownAttributeException

        indices = [t[0].index(attr) for attr in r]
        res = []
        # adding rows
        for k in range(len(t)):
            res.append([t[k][i] for i in indices])
        if not res:
            res = None
        else:
            res = remove_duplicates(res)
    # if empty table, return nothing
    if len(res) < 2:
        res = None
    return res


def cross_product(t1, t2):
    """
    Return the cross-product of tables t1 and t2.
    Return NONE if the result is an empty table.

    To do: +add param:

    Example:
    > R1 = [["A", "B"], [1,2], [3,4]]
    > R2 = [["C", "D"], [5,6]]
    [["A", "B", "C", "D"], [1, 2, 5, 6], [3, 4, 5, 6]]

    """
    return_list = None

    if t1 and t2:
        return_list = []
        for n in xrange(1, len(t1)):
            for i in xrange(1, len(t2)):
                return_list.append(t1[n] + t2[i])

        return_list.insert(0, t1[0] + t2[0])
        return_list = remove_duplicates(return_list)
        if len(return_list) < 2:
            return_list = None

    return return_list

