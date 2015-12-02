#!/usr/bin/env python3

""" Module to test papers.py  """

__author__ = 'Piaoyao Shi & Zixiao Yang & Ming Fu '
__email__ = "piaoyao.shi@mail.utoronto.ca & zeke.yang@mail.utoronto.ca & mm.fu@mail.utoronto.ca"
__copyright__ = "2015 Piaoyao Shi & Zixiao Yang & Ming Fu"

__status__ = "Prototype"

# imports one per line
import...

DIR = "test_jsons/"
os.chdir(DIR)


def test_returning():
    """
    Travellers are returning to KAN.
    """
    assert decide("test_returning_citizen.json", "countries.json") ==\
        ["Accept", "Accept", "Quarantine"]


def test_accept():
 """test accept:
 1. citizen
    a. A valid passport
    b. home country is Kanadia  (KAN)
    c. accept mismatch between uppercase and lowercase

 2. visitor
     a. complete entry record
     b. location mentioned in the entry record is known
     c. home country is not Kanadia  (KAN)
     d. has a passport from a country from which a visitor visa is required
     e. has a valid visa
     f. accept mismatch between uppercase and lowercase

 """
def test_quarantine():
 """test quarantine:

 1. citizen: coming from or travelling through a country with a medical advisory
 2. visitor: coming from or travelling through a country with a medical advisory

 """

 def test_reject():
 """test reject

 Visitor:
 1. entry record is incomplete
 2. entry record is unknown
 4. invalid visa
 5. A valid visa is less than two years old


 """

