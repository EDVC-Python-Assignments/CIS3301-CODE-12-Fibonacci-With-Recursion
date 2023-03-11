import os,sys
from mock_input_tests import *
from code_12 import main
import random

def check_if_file_exists():
    try:
        exists = os.path.exists("code_12.py")
        assert exists == True
    except:
        sys.exit()

def test_get_fibonacci_number_sequence():
    check_if_file_exists()
    