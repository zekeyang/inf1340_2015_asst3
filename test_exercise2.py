#!/usr/bin/env python3

""" Module to test papers.py  """

__author__ = 'Piaoyao Shi & Zixiao Yang & Ming Fu '
__email__ = "piaoyao.shi@mail.utoronto.ca & zeke.yang@mail.utoronto.ca & mm.fu@mail.utoronto.ca"
__copyright__ = "2015 Piaoyao Shi & Zixiao Yang & Ming Fu"

__status__ = "Prototype"

# imports one per line

from exercise2 import *
import os

DIR = os.getcwd()
DIR += '/test_jsons'
os.chdir(DIR)


def test_returning():
    """
    #Travellers are returning to KAN.
    """
    assert decide("test_returning_citizen.json", "countries.json") == ["Accept", "Accept", "Quarantine"]


def assert_false(exp):
    assert not exp

######################
# Test main function #
######################

# ========== Accept Case =====================================

# scenario 1 :

# scenario 2:


# ========== Quarantine Case =================================

# scenario x

# =========== Reject Case ====================================

# scenario x

# scenario x

# scenario x


########################
# Test Helper function #
########################

# =========== field_complete function =======================

# =========== check_entry_info function =====================


# =========== check_visa function =====================
def test_check_visa():
    countries = read_file("countries.json")
    cases = read_file("test_check_visa.json")


# =========== location_known function =======================

def test_location_known():
    countries = read_file("countries.json")

    l1 = {"city": "Eureka", "region": "NU","country": "KRA"}
    assert location_known(l1, countries)

    l2 = {"city": "UNKNOWN", "region": "UNKNOWN","country": "UNKNOWN"}
    assert_false(location_known(l2, countries))


# =========== check_location function ========================
def test_check_location():
    """
    Check if the locations in a given case case are known
    """
    cases = read_file('test_check_location.json')
    countries = read_file("countries.json")

    # home, from known
    assert check_location(cases[0], countries)
    # home unknown
    assert_false(check_location(cases[1], countries))
    # visa unknown
    assert_false(check_location(cases[2], countries))
    # all known
    assert check_location(cases[3], countries)


# =========== check_medical function ========================
def test_check_medical():
    cases = read_file('test_check_medical.json')
    countries = read_file("countries.json")

    # home medical
    assert check_medical(cases[0], countries)
    # from medical
    assert check_medical(cases[1], countries)
    # visa medical
    assert check_medical(cases[2], countries)
    # no medical
    assert_false(check_medical(cases[3], countries))


# =========== valid_passport_format function =================


def test_valid_passport_format():
    """
    Checks whether a passport number is five sets of five alpha-number characters separated by dashes
    """
    assert_false(valid_passport_format(''))
    assert_false(valid_passport_format('1-2-3-4-5'))
    assert_false(valid_passport_format('a-b-c-d-e'))
    assert_false(valid_passport_format('a1234 bacee cadsf dadfe ezxce'))
    assert valid_passport_format('12345-12345-12345-12345-12345')
    assert valid_passport_format('abcde-abcde-abcde-abcde-abcde')
    assert valid_passport_format('9768e-ab1de-8bc14-a3c4e-b12de')
    assert_false(valid_passport_format('9768e-ab1de-8bc14-a3c4e!b12de'))


# =========== valid_visa_format function =================


def test_valid_visa_format():
    """
    Checks whether a visa code is two groups of five alphanumeric characters
    """


# =========== valid_date_format function =====================


def test_valid_date_format():
    """
    Checks whether a date has the format yyyy-mm-dd in numbers
    """

