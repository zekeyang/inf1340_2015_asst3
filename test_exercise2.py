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

# ========================================= Our test cases ===========================================================

######################
# Test main function #
######################


def test_visitor():
    """
    Travellers are visiting KAN.
    """
    # case 1: traveller is from a country not require a visa
    # case 2: requires a visa; visa is not valid
    # case 3: traveller is coming from a country with a medical advisory
    # case 4: entry_info_incomplete
    # case 5: country unknown

    assert decide("test_visiting.json", "countries.json") == ["Accept", "Reject", "Quarantine", "Reject", "Reject"]


def test_our_returning():
    """
    Travellers are returning to KAN.
    """
    # case 1: traveller is from a country not require a visa
    # case 2: has a invalid visa.
    # case 3: traveller is coming from a country with a medical advisory
    # case 4: entry_info_incomplete
    # case 5: from unknown location
    # case 6: not case sensitive

    assert decide("test_our_returning.json", "countries.json") \
        == ["Accept", "Accept", "Quarantine", "Reject", "Reject", "Accept"]

########################
# Test Helper function #
########################

# =============================== check_entry_info function ===========================


def test_check_entry_info():
    """
    Test check_entry_info function.
    True if given case has all required information, False otherwise.
    """

    cases = read_file("test_check_entry_info.json")

    assert_false(check_entry_info(cases[0]))
    assert_false(check_entry_info(cases[1]))
    assert_false(check_entry_info(cases[2]))
    assert_false(check_entry_info(cases[3]))
    assert_false(check_entry_info(cases[4]))
    assert_false(check_entry_info(cases[5]))
    assert_false(check_entry_info(cases[6]))
    assert_false(check_entry_info(cases[7]))
    assert_false(check_entry_info(cases[8]))
    assert check_entry_info(cases[9])

# ================================ check_visa function ==================================


def test_check_visa():
    """
    Test check_visa function.
    Return True if visa check is passed, False otherwise.
    """

    countries = read_file("countries.json")
    cases = read_file("test_check_visa.json")

    assert check_visa(cases[0], countries)
    assert check_visa(cases[1], countries)
    assert check_visa(cases[2], countries)
    assert_false(check_visa(cases[7], countries))
    assert_false(check_visa(cases[3], countries))
    assert_false(check_visa(cases[4], countries))
    assert_false(check_visa(cases[5], countries))
    assert_false(check_visa(cases[6], countries))
    
# ================================ location_known function ===============================


def test_location_known():
    countries = read_file("countries.json")

    l1 = {"city": "Eureka", "region": "NU", "country": "KRA"}
    assert location_known(l1, countries)

    l2 = {"city": "UNKNOWN", "region": "UNKNOWN", "country": "UNKNOWN"}
    assert_false(location_known(l2, countries))

# =============================== check_location function ===============================


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

# ============================== check_medical function ===================================


def test_check_medical():
    cases = read_file('test_check_medical.json')
    countries = read_file("countries.json")

    # home medical
    assert check_medical(cases[0], countries)
    # from medical
    assert check_medical(cases[1], countries)
    # via medical
    assert check_medical(cases[2], countries)
    # no medical
    assert_false(check_medical(cases[3], countries))

# ============================= valid_passport_format function ===============================


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

# ============================= valid_visa_format function =====================================


def test_valid_visa_format():
    """
    Checks whether a visa code is two groups of five alphanumeric characters
    """

    assert_false(valid_visa_format(''))
    assert_false(valid_visa_format('1234567890'))
    assert_false(valid_visa_format('12345678901'))
    assert_false(valid_visa_format('abcdefghij'))
    assert_false(valid_visa_format('abcdefghijk'))
    assert_false(valid_visa_format('12345abcd!'))
    assert_false(valid_visa_format('1a2b3c4d5e'))
    assert valid_visa_format('12345-abcde')
    assert valid_visa_format('1234a-bcde5')
    assert valid_visa_format('1a2b3-c4d5e')

# =========================== valid_date_format function =========================================


def test_valid_date_format():
    """
    Checks whether a date has the format yyyy-mm-dd in numbers
    """

    assert_false(valid_date_format(''))
    assert_false(valid_date_format('15-12-16'))
    assert_false(valid_date_format('12-16-2015'))
    assert_false(valid_date_format('12-16-15'))
    assert_false(valid_date_format('16-12-2015'))
    assert_false(valid_date_format('16-12-15'))
    assert_false(valid_date_format('2015.12.16'))
    assert_false(valid_date_format('2015/12/16'))
    assert_false(valid_date_format('2015 12 16'))
    assert_false(valid_date_format('December 16,2015'))
    assert_false(valid_date_format('Dec.16, 2015'))
    assert_false(valid_date_format('2015-December-16'))
    assert_false(valid_date_format('2015-Dec.16'))
    assert valid_date_format('2015-12-16')
    assert valid_date_format('2016-01-01')
