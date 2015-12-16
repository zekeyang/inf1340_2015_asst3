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
    True if field in case, False otherwise.

    :param case: dictionary representation of case to be checked
    :param field: string
    :return: Boolean
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
        elif field == 'visa':
            res = 'date' in case[field] and 'code' in case[field] \
                  and valid_date_format(case[field]['date']) \
                and valid_visa_format(case[field]['code'])
            print res

    return res


def check_entry_info(case):
    """
    True if given case has all required information, False otherwise

    :param case: the dictionary representation of the case to be checked
    :return: Boolean
    """

    for required_field in REQUIRED_FIELDS:
        if not field_complete(case, required_field):
            return False
    return True


def location_known(location, countries):
    """
    Return True if Check if location is known from countries, False otherwise.

    :param location: the dictionary representation of a location to be checked
    :param countries: known countries given by the ministry
    :return: Boolean
    """
    return location["country"] in countries.keys() or location['country'].upper() == 'KAN' \
        or location['country'].upper() == 'KANADIA'


def check_location(case, countries):
    """
    Return True if the locations in a given case are known, otherwise False.

    :param case: the dictionary representation of the case to be checked
    :param countries: the dictionary representation of the countries info
    :return: Boolean
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
    Return True if the home country is Kanadia, otherwise False.

    :param case: the dictionary representation of the case to be checked
    :return: Boolean
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
    Return True if visa check is passed, False otherwise.

    :param case: the dictionary representation of the case to be checked
    :param countries: the dictionary representation of the countries info
    :return Boolean
    """

    res = False
    if field_complete(case, 'entry_reason') and field_complete(case, 'home') and \
       location_known(case['home'], countries):
        if case['entry_reason'].upper() == 'VISIT':
            from_country_code = case['home']['country']
            visa_required = countries[from_country_code]['visitor_visa_required']
            if int(visa_required) > 0:
                res = field_complete(case, 'visa') \
                    and not is_more_than_x_years_ago(2, case['visa']['date'])
            else:
                # no visa required
                res = True
        else:
            # entry reason returning, visa check passed
            res = True

    return res


def check_medical(case, countries):
    """
    Return True if the case is coming from or travelling through a country with a medical advisory, False otherwise.
    :param case: the dictionary representation of the case to be checked
    :param countries: the dictionary representation of the countries info
    :return: boolean

    Pre-condition: all locations known
    """

    # list of code with medical_advisory
    medical_countries = [x for x in countries if countries[x]['medical_advisory']]

    # list of countries codes
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
    :return: Boolean; True if the format is valid, False otherwise
    """

    p = re.compile("^\d{4}-\d{2}-\d{2}$")
    return bool(p.match(date_string))

#################
# Main Function #
#################


def decide(input_file, countries_file):
    """
    Decides whether a traveller's entry into Kanadia should be accepted

    :param input_file: The name of a JSON formatted file that contains
        cases to decide
    :param countries_file: The name of a JSON formatted file that contains
        country data, such as whether an entry or transit visa is required,
        and whether there is currently a medical advisory
    :return: List of strings. Possible values of strings are:
        "Accept", "Reject", and "Quarantine"
    """

    # pre processing
    cases = read_file(input_file)  # list of dict
    countries = read_file(countries_file)  # dict of dict
    decisions = ['Reject', 'Accept', 'Quarantine']
    res = []

    for case in cases:
        case_decision = decisions[0]                                   # default decision equals to reject for everyone
        is_info_completed = check_entry_info(case)

        if is_info_completed:                                          # execute if file is complete
            is_location_known = check_location(case, countries)
            if is_location_known:                                      # execute if location is known
                is_home_country = check_home_country(case)
                if is_home_country:                                    # execute if home country is Kanadia
                    case_decision = decisions[1]
                is_valid_visa = check_visa(case, countries)
                if is_valid_visa:                               # execute if visa is valid (home country isn't Kanadia)
                    send_quarantine = check_medical(case, countries)
                    if send_quarantine:                                # execute if medical condition not pass
                        case_decision = decisions[2]                   # medical condition not pass, Quarantine
                    else:
                        case_decision = decisions[1]                   # meet all conditions, accept entry
        res.append(case_decision)

    return res


if __name__ == '__main__':
    decide('test_returning_citizen.json', 'countries.json')