#!/usr/bin/env python3

""" Module to test papers.py  """

__author__ = 'Piaoyao Shi & Zixiao Yang & Ming Fu '
__email__ = "piaoyao.shi@mail.utoronto.ca & zeke.yang@mail.utoronto.ca & mm.fu@mail.utoronto.ca"
__copyright__ = "2015 Piaoyao Shi & Zixiao Yang & Ming Fu"

__status__ = "Prototype"

# imports one per line

from exercise2 import *
import os

DIR = "test_jsons/"
os.chdir(DIR)


def test_returning():
    """
    Travellers are returning to KAN.
    """
    assert decide("test_returning_citizen.json", "countries.json") ==\
           ["Accept", "Accept", "Quarantine"]


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

# =========== is_more_than_x_years_ago ======================

# =========== field_complete function =======================

# =========== check_entry_info function =====================

# =========== location_known function =======================

# =========== check_location function ========================

# =========== valid_passport_format function =================

# =========== valid_passport_format function =================

# =========== valid_visa_format function =====================
