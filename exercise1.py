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
    Perform select operation on table t that satisfy condition f.

    Example:
    > R = [["A", "B", "C"], [1, 2, 3], [4, 5, 6]]
    ># Define function f that returns True iff
    > # the last element in the row is greater than 3.
    > def f(row): row[-1] > 3
    > select(R, f)
    [["A", "B", "C"], [4, 5, 6]]
    QUESTION:   ARE WE CONSIDERING OPERATOR "AND", "OR" AND COMBINATION OF "AND" AND "OR"?
                HOW TO PASS AND USE ARGUMENT LIKE row[-1] > 3 ?
    """

    return []


def projection(t, r):
    """
    Perform projection operation on table t
    using the attributes subset r.

    Example:
    > R = [["A", "B", "C"], [1, 2, 3], [4, 5, 6]]
    > projection(R, ["A", "C"])
    [["A", "C"], [1, 3], [4, 6]]

    """
    # check if each item in r exists in table t schema
    # return the position of each item
    # list all value in table t with the projected position
    projected_list = []
    return_list = []
    for i in xrange(len(t[0])):
        for n in xrange(len(r)):
            if r[n] == t[0][i]:
                projected_list.append(i)
    for x in xrange(len(t)):
        return_list.append([t[x][index] for index in projected_list])
    return return_list


def cross_product(t1, t2):
    """
    Return the cross-product of tables t1 and t2.

    Example:
    > R1 = [["A", "B"], [1,2], [3,4]]
    > R2 = [["C", "D"], [5,6]]
    [["A", "B", "C", "D"], [1, 2, 5, 6], [3, 4, 5, 6]]


    """
    return_list = []
    for n in xrange(1, len(t1)):
        for i in xrange(1, len(t2)):
            return_list.append(t1[n]+t2[i])
    return_list.insert(0, t1[0] + t2[0])

    return return_list


# BELOW CODES ARE FOR TESTING PURPOSE, WILL BE REMOVED BEFORE SUBMISSION
R1 = [["Employee", "Department"],
      ["Smith", "sales"],
      ["Black", "production"],
      ["White", "production"]]

R2 = [["Department", "Head"],
      ["production", "Mori"],
      ["sales", "Brown"]]

print cross_product(R1, R2)