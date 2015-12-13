#!/usr/bin/env python3

""" Assignment 3, Exercise 2, INF1340, Fall, 2015. Kanadia

Computer-based immigration office for Kanadia

"""

__author__ = 'Piaoyao Shi & Zixiao Yang & Ming Fu '
__email__ = "piaoyao.shi@mail.utoronto.ca & zeke.yang@mail.utoronto.ca & mm.fu@mail.utoronto.ca"
__copyright__ = "2015 Piaoyao Shi & Zixiao Yang & Ming Fu"

import re
import datetime
import json

######################
# global constants  #
######################
REQUIRED_FIELDS = ["passport", "first_name", "last_name",
                   "birth_date", "home", "entry_reason", "from"]

######################
# global variables  #
######################
'''
countries:
dictionary mapping country codes (lowercase strings) to dictionaries
containing the following keys:
"code","name","visitor_visa_required",
"transit_visa_required","medical_advisory"
'''
COUNTRIES = None

#####################
# HELPER FUNCTIONS ##
#####################


def is_more_than_x_years_ago(x, date_string):
    """
    Check if date is less than x years ago.

    :param x: int representing years
    :param date_string: a date string in format "YYYY-mm-dd"
    :return: True if date is less than x years ago; False otherwise.
    """

    now = datetime.datetime.now()
    x_years_ago = now.replace(year=now.year - x)
    date = datetime.datetime.strptime(date_string, '%Y-%m-%d')

    return (date - x_years_ago).total_seconds() < 0


def read_file(filename):
    """
    Read the content of file given by filename

    :param filename: The name of the JSON formatted file
    :return: the content of file named filename in a list of dictionaries
    """

    with open(filename) as data_file:
        data = json.load(data_file)
    return data


def field_complete(case, field):
    """
    Check if field field is in case case.

    :param case: dictionary representation of case to be checked
    :param field: string
    :return: True if field in case, False otherwise
    """

    fields = case.keys()
    res = False

    if field in fields and len(case[field]) != 0:
        res = True

        if field == 'birth_date':
            res = valid_date_format(case[field])
        elif field == 'passport':
            res = valid_passport_format(case[field])
        elif field == 'entry_reason':
            res = case[field] in ['visit', 'returning']

    return res


def check_entry_info(case):
    """
    Check if the given case case has complete information

    :param case: the dictionary representation of the case to be checked
    :return: True if given case has all required information, False otherwise
    """

    for required_field in REQUIRED_FIELDS:
        if not field_complete(case, required_field):
            return False
    return True


def location_known(location, countries):
    """
    Check if location location is known from countries

    :param location: the dictionary representation of a location to be checked
    :param countries: known countries given by the ministry
    :return: True if location is known, False otherwise
    """
    return location["country"] in countries.keys() or location['country'].upper() == 'KAN' \
        or location['country'].upper() == 'KANADIA'


def check_location(case, countries):
    """
    Check if the locations in a given case case are known

    :param case: the dictionary representation of the case to be checked
    :param countries: the dictionary representation of the countries info
    :return: True if all locations are known, False otherwise
    """

    location_fields = ['home', 'from']
    # Home and From exist, need to check if there is a visa
    if field_complete(case, 'via'):
        location_fields.append('via')

    for field in location_fields:
        if not location_known(case[field], countries):
            return False
    return True


def check_home_country(case):
    """"
    Check

    :param case: the dictionary representation of the case to be checked
    :return: True if the home country associated with case is name: Kanadia code: KAN
    """

    res = False
    home = {}

    if field_complete(case, 'home'):
        home = case['home']
    if 'country' in home:
        return home['country'].upper() == 'KAN' or home['country'].upper() == 'KANADIA'
    return res


def check_visa(case, countries):
    """
    Return True if visa check is passed, False otherwise

    """
    res = False
    if field_complete(case, 'entry_reason') and field_complete(case, 'from') and \
       location_known(case['from'], countries):
        if case['entry_reason'].upper() == 'VISIT':
            from_country_code = case['from']['country']
            visa_required = countries[from_country_code]['visitor_visa_required']
            if int(visa_required) > 0:
                res = field_complete(case, 'visa') and valid_date_format(case['visa']['date']) \
                    and not is_more_than_x_years_ago(2, case['visa']['date'])
        else:
            # entry reason returning, visa check passed
            res = True

    return res


def check_medical(case, countries):
    """
    Pre-condition: all locations known
    Return True if the case needs to send to quarantine, False otherwise.
    """

    # list of code with medical_advisory
    medical_countries = [x for x in countries if countries[x]['medical_advisory']]

    # list of codes
    countries_codes = [case[x]['country'] for x in case if x in ['home', 'via', 'from']]
    medical = [x for x in countries_codes if x in medical_countries]
    return medical != []


def valid_passport_format(passport_number):
    """
    Checks whether a passport number is five sets of five alpha-number characters separated by dashes
    :param passport_number: alpha-numeric string
    :return: Boolean; True if the format is valid, False otherwise
    """
    p = re.compile("^\w{5}-\w{5}-\w{5}-\w{5}-\w{5}$")
    return bool(p.match(passport_number))


def valid_visa_format(visa_code):
    """
    Checks whether a visa code is two groups of five alphanumeric characters
    :param visa_code: alphanumeric string
    :return: Boolean; True if the format is valid, False otherwise

    """
    p = re.compile("^\w{5} \w{5}$")
    return bool(p.match(visa_code))


def valid_date_format(date_string):
    """
    Checks whether a date has the format yyyy-mm-dd in numbers
    :param date_string: date to be checked
    :return: Boolean True if the format is valid, False otherwise
    """

    p = re.compile("^\d{4}-\d{2}-\d{2}$")
    return bool(p.match(date_string))
