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

EMPTY_HEADER = [[]]


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


######################
# Our test functions #
######################

# =========================================Test Function Selection  ===================================================

# with normal table


def test_selection_surname_one():
    """
    Test select operation with a normal table
    """

    result = [["Surname", "FirstName", "Age", "Salary"],
              ["Smith", "Mary", 25, 2000],
              ["Smith", "Mark", 40, 3900]]

    assert is_equal(result, selection(EMPLOYEES, filter_employees_surname_start_with_s))


def test_selection_surname_two():
    """
    Test select operation with a normal table; No surname starts with "S"
    """
    assert selection(MANAGERS, filter_employees_surname_start_with_s) is None

# with empty table


def test_selection_empty():
    """
    Test select operation with an empty table
    As required, the function shall return None
    """
    # The testing table is empty (only has the header)
    assert selection(HEADER_ONLY, filter_employees) is None
    assert selection(HEADER_ONLY, filter_employees_surname_start_with_s) is None
    # The testing table is empty
    assert selection(EMPTY_TABLE, filter_employees) is None
    assert selection(EMPTY_TABLE, filter_employees_surname_start_with_s) is None


# =========================================Test Function Projection ===================================================

# with normal table

def test_projection_managers():
    """
    Test projection operation with MANAGERS table
    """

    result1 = [["Surname", "Age"],
               ["O'Malley", 56],
               ["Verdi", 36]]

    result2 = [["Age", "Surname"],
               [56, "O'Malley"],
               [36, "Verdi"]]

    assert is_equal(result1, projection(MANAGERS, ["Surname", "Age"]))

    assert is_equal(result2, projection(MANAGERS, ["Age", "Surname"]))

# with empty table


def test_projection_empty():
    """
    Test projection operation with an empty table
    As required, the function shall return None
    """
    # The testing table is empty (only has the header)
    assert projection(HEADER_ONLY, ["Surname", "FirstName", "Age", "Salary"]) is None
    # Subset r is empty
    assert projection(EMPLOYEES, []) is None


# Test exception

def test_projection_unknown_attribute_exception_one():
    """
    Test projection operation with raising UnknownAttributeException
    """
    try:
        projection(EMPLOYEES, ["Position"])
    except UnknownAttributeException:
        assert True


def test_projection_unknown_attribute_exception_two():
    """
    Test projection operation with raising UnknownAttributeException.
    The testing table equals to [].
    """
    try:
        projection(EMPTY_TABLE, ["Surname", "FirstName", "Age", "Salary"])
    except UnknownAttributeException:
        assert True


def test_projection_unknown_attribute_exception_three():
    """
    Test projection operation with raising UnknownAttributeException.
    The testing table equals to [[]].
    """
    try:
        projection(EMPTY_HEADER, ["Surname", "FirstName", "Age", "Salary"])
    except UnknownAttributeException:
        assert True
# =========================================Test Function Cross_Product ================================================

# with normal table


def test_cross_product_managers_employees():
    """
    Test cross product operation, with MANAGERS and EMPLOYEES tables.
    """

    result = [["Surname", "FirstName", "Age", "Salary", "Surname", "FirstName", "Age"],
              ["Smith", "Mary", 25, 2000, "O'Malley", "Jack", 56],
              ["Smith", "Mary", 25, 2000, "Verdi", "Nico", 36],
              ["Black", "Lucy", 40, 3000, "O'Malley", "Jack", 56],
              ["Black", "Lucy", 40, 3000, "Verdi", "Nico", 36],
              ["Verdi", "Nico", 36, 4500, "O'Malley", "Jack", 56],
              ["Verdi", "Nico", 36, 4500, "Verdi", "Nico", 36],
              ["Smith", "Mark", 40, 3900, "O'Malley", "Jack", 56],
              ["Smith", "Mark", 40, 3900, "Verdi", "Nico", 36]]

    assert is_equal(result, cross_product(EMPLOYEES, MANAGERS))


def test_cross_product_r2_r1():
    """
    Test cross product operation, with R2 and R1 tables. Input order matters
    """

    result = [["Department", "Head", "Employee", "Department"],
              ["production", "Mori", "Smith", "sales"],
              ["sales", "Brown", "Smith", "sales"],
              ["production", "Mori", "Black", "production"],
              ["sales", "Brown", "Black", "production"],
              ["production", "Mori", "White", "production"],
              ["sales", "Brown", "White", "production"]]

    assert is_equal(result, cross_product(R2, R1))


# with empty table

def test_cross_product_empty():
    """
    Test cross product operation with empty tables
    As required, the function shall return None
    """
    assert cross_product(R1, EMPTY_TABLE) is None
    assert cross_product(EMPLOYEES, HEADER_ONLY) is None
    assert cross_product(EMPTY_TABLE, HEADER_ONLY) is None
