#!/usr/bin/env python3

""" Module to test papers.py  """

__author__ = 'Piaoyao Shi & Zixiao Yang & Ming Fu '
__email__ = "piaoyao.shi@mail.utoronto.ca & zeke.yang@mail.utoronto.ca & mm.fu@mail.utoronto.ca"
__copyright__ = "2015 Piaoyao Shi & Zixiao Yang & Ming Fu"

__status__ = "Prototype"

# imports one per line
import json

DIR = "test_jsons/"
os.chdir(DIR)


def test_returning():
    """
    Travellers are returning to KAN.
    """
    assert decide("test_returning_citizen.json", "countries.json") ==\
           ["Accept", "Accept", "Quarantine"]

#========== Accept Case ===========

def test_accept():
 """Travellers are accepted

"""
    assert decide('test_accept_citizen.json', "countries.json")==\
           ["Accept", "Accept", "Accept"]


 #========== Quarantine Case ===========
def test_quarantine():
 """test quarantine:

 1. citizen: coming from or travelling through a country with a medical advisory
 2. visitor: coming from or travelling through a country with a medical advisory

 """
#=========== Reject Case ============
 def test_reject():
 """test reject

 Visitor:
 1. entry record is incomplete
 2. entry record is unknown
 4. invalid visa
 5. A valid visa is less than two years old


 """

