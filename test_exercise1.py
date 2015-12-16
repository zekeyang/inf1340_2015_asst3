#!/usr/bin/env python

""" Assignment 3, Exercise 1, INF1340, Fall, 2015. DBMS

Test module for exercise3.py

"""

__author__ = 'Piaoyao Shi & Zixiao Yang & Ming Fu '
__email__ = "piaoyao.shi@mail.utoronto.ca & zeke.yang@mail.utoronto.ca & mm.fu@mail.utoronto.ca"
__copyright__ = "2015 Piaoyao Shi & Zixiao Yang & Ming Fu"

from exercise1 import *


###########
# TABLES ##
###########

EMPLOYEES = [["Surname", "FirstName", "Age", "Salary"],
             ["Smith", "Mary", 25, 2000],
             ["Black", "Lucy", 40, 3000],
             ["Verdi", "Nico", 36, 4500],
             ["Smith", "Mark", 40, 3900]]


R1 = [["Employee", "Department"],
      ["Smith", "sales"],
      ["Black", "production"],
      ["White", "production"]]

R2 = [["Department", "Head"],
      ["production", "Mori"],
      ["sales", "Brown"]]

HEADER_ONLY = [["Surname", "FirstName", "Age", "Salary"]]

MANAGERS = [["Surname", "FirstName", "Age"],
            ["O'Malley", "Jack", 56],
            ["Verdi", "Nico", 36]]

EMPTY_TABLE = []


#####################
# HELPER FUNCTIONS ##
#####################
def is_equal(t1, t2):

    t1.sort()
    t2.sort()

    return t1 == t2


#####################
# FILTER FUNCTIONS ##
#####################
def filter_employees(row):
    """
    Check if employee represented by row
    is AT LEAST 30 years old and makes
    MORE THAN 3500.
    :param row: A List in the format:
        [{Surname}, {FirstName}, {Age}, {Salary}]
    :return: True if the row satisfies the condition.
    """
    return row[-2] >= 30 and row[-1] > 3500


def filter_employees_surname_start_with_s(row):
    """
    Check if employee's start with S
    :param row: A List in the format:
        [{Surname}, {FirstName}, {Age}, {Salary}]
    :return: True if the row satisfies the condition.
    """
    return row[0].startswith("S")

###################
# TEST FUNCTIONS ##
###################


def test_selection():
    """
    Test select operation with a normal table
    """

    result = [["Surname", "FirstName", "Age", "Salary"],
              ["Verdi", "Nico", 36, 4500],
              ["Smith", "Mark", 40, 3900]]

    assert is_equal(result, selection(EMPLOYEES, filter_employees))


def test_selection_empty():
    """
    Test select operation with an empty table
    As required, the function shall return None
    """
    assert selection(EMPLOYEES_EMPTY, filter_employees) is None


def test_projection():
    """
    Test projection operation with normal table
    """

    result = [["Surname", "FirstName"],
              ["Smith", "Mary"],
              ["Black", "Lucy"],
              ["Verdi", "Nico"],
              ["Smith", "Mark"]]

    assert is_equal(result, projection(EMPLOYEES, ["Surname", "FirstName"]))


def test_projection_empty():
    """
    Test projection operation with an empty table
    As required, the function shall return None
    """
    assert projection(R3, ["Title_3"]) is None


def test_projection_unknown_attribute_exception():
    """
    Test projection operation with raising UnknownAttributeException
    """

    try:
        projection(EMPLOYEES, ["No_Such_Name"])
    except UnknownAttributeException:
        assert True


def test_cross_product():
    """
    Test cross product operation, with two normal tables
    """

    result = [["Employee", "Department", "Department", "Head"],
              ["Smith", "sales", "production", "Mori"],
              ["Smith", "sales", "sales", "Brown"],
              ["Black", "production", "production", "Mori"],
              ["Black", "production", "sales", "Brown"],
              ["White", "production", "production", "Mori"],
              ["White", "production", "sales", "Brown"]]

    assert is_equal(result, cross_product(R1, R2))


def test_cross_product_empty():
    """
    Test cross product operation with one empty table
    As required, the function shall return None
    """
    assert cross_product(R1, R3) is None