#!/usr/bin/env python3

""" Module to test papers.py  """

__author__ = 'Piaoyao Shi & Zixiao Yang & Ming Fu '
__email__ = "piaoyao.shi@mail.utoronto.ca & zeke.yang@mail.utoronto.ca & mm.fu@mail.utoronto.ca"
__copyright__ = "2015 Piaoyao Shi & Zixiao Yang & Ming Fu"

__status__ = "Prototype"

# imports one per line

# import pytest       # the import statement exists in the original file, but not used here
from exercise2 import *
import os

DIR = os.getcwd()         # define DIR as a string representing the current working directory.
DIR += '/test_jsons'      # change 'test_jsons/' into '/test_jsons', otherwise the test isn't working.
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
    # case 6: requires a visa; visa is valid

    assert decide("test_visiting.json", "countries.json") \
        == ["Accept", "Reject", "Quarantine", "Reject", "Reject", "Accept"]


def test_our_returning():
    """
    Travellers are returning to KAN.
    """
    # case 1: home country is Kanadia
    # case 2: has a invalid visa.
    # case 3: traveller is coming from a country with a medical advisory
    # case 4: entry_info_incomplete
    # case 5: from unknown location
    # case 6: not case sensitive

    assert decide("test_our_citizen.json", "countries.json") \
        == ["Accept", "Accept", "Quarantine", "Reject", "Reject", "Accept"]


def test_mix_citizen_and_visitor():
    """
    Travellers are either returning to or visiting KAN.
    """
    # case 1: citizen
    # case 2: visitor, from a country doesn't require visa
    # case 5: citizen, from a country with a medical advisory
    # case 7: visitor, from a country requires visa and with medical advisory, no valid visa

    assert decide("test_mix_citizen_visitor.json", "countries.json") == ["Accept", "Accept", "Quarantine", "Reject"]

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

    assert_false(check_entry_info(cases[0]))      # Passport Number is missing
    assert_false(check_entry_info(cases[1]))      # First Name is missing
    assert_false(check_entry_info(cases[2]))      # Last Name is missing
    assert_false(check_entry_info(cases[3]))      # Birth Date is missing
    assert_false(check_entry_info(cases[4]))      # Home (Location) is missing
    assert_false(check_entry_info(cases[5]))      # Reason for Entry is missing
    assert_false(check_entry_info(cases[6]))      # From (Location) is missing
    assert check_entry_info(cases[7])             # visa is not a required field
    assert check_entry_info(cases[8])             # visa is not a required field
    assert check_entry_info(cases[9])             # Has all required information

# ================================ check_visa function ==================================


def test_check_visa():
    """
    Test check_visa function.
    Return True if visa check is passed, False otherwise.
    """

    countries = read_file("countries.json")
    cases = read_file("test_check_visa.json")

    assert check_visa(cases[0], countries)          # visa is not required, doesn't have visa
    assert check_visa(cases[1], countries)          # visa is not required, has valid visa
    assert check_visa(cases[2], countries)          # visa is required, has valid visa
    assert_false(check_visa(cases[7], countries))   # no home country information
    assert_false(check_visa(cases[3], countries))   # visa is required, visa is expired
    assert_false(check_visa(cases[4], countries))   # visa is required, code is invalid
    assert_false(check_visa(cases[5], countries))   # visa is required, doesn't have visa
    assert_false(check_visa(cases[6], countries))   # visa is not required, no entry reason
    
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
    # via unknown
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
    assert_false(valid_passport_format(''))                               # empty str
    assert_false(valid_passport_format('1-2-3-4-5'))                      # only one number for each group
    assert_false(valid_passport_format('a-b-c-d-e'))                      # only one letter for each group
    assert_false(valid_passport_format('a1234 bacee cadsf dadfe ezxce'))  # incorrect delimiters
    assert valid_passport_format('12345-12345-12345-12345-12345')         # all valid.
    assert valid_passport_format('Hello-World-Hello-Susan-Hello')         # case insensitive
    assert valid_passport_format('9768e-ab1de-8bc14-a3c4e-b12de')         # all valid.
    assert_false(valid_passport_format('9768e-ab1de-8bc14-a3c4e!-b12de'))  # one group has more than 5 characters

# ============================= valid_visa_format function =====================================


def test_valid_visa_format():
    """
    Checks whether a visa code is two groups of five alphanumeric characters
    """

    assert_false(valid_visa_format(''))                   # empty str
    assert_false(valid_visa_format('1234567890'))         # no delimiter, all numbers
    assert_false(valid_visa_format('12345-678901'))       # has more than 5 alphanumeric characters
    assert_false(valid_visa_format('abcdefghij'))         # no delimiter, all letters
    assert_false(valid_visa_format('12345-abcd!'))        # not all characters are alphanumeric
    assert_false(valid_visa_format('1a2b3-c4d5e-abcde'))  # has more than 2 groups of five alphanumeric characters
    assert valid_visa_format('12345-67890')               # all numbers
    assert valid_visa_format('Hello-World')               # all letters, case insensitive
    assert valid_visa_format('1a2b3-c4D5e')               # mix with numbers and letters, case insensitive

# =========================== valid_date_format function =========================================


def test_valid_date_format():
    """
    Checks whether a date has the format yyyy-mm-dd in numbers
    """

    assert_false(valid_date_format(''))                   # empty str
    assert_false(valid_date_format('15-12-16'))           # year is invalid
    assert_false(valid_date_format('12-16-2015'))         # wrong order
    assert_false(valid_date_format('2015.12.16'))         # incorrect delimiters
    assert_false(valid_date_format('2015/12/16'))         # incorrect delimiters
    assert_false(valid_date_format('2015 12 16'))         # incorrect delimiters
    assert_false(valid_date_format('2015-December-16'))   # incorrect month type
    assert_false(valid_date_format('2015-13-16'))         # month out of range
    assert_false(valid_date_format('2015-12-32'))         # day out of range
    assert_false(valid_date_format('2015-11-31'))         # November has 30 days only
    assert_false(valid_date_format('2015-02-29'))         # 2015 is not leap year
    assert valid_date_format('2008-02-29')                # Feb in leap year has 29 days
    assert valid_date_format('2015-12-16')                # year, month, day all valid
    assert valid_date_format('2016-01-01')                # year, month, day all valid
