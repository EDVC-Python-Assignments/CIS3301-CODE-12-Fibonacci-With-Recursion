import os,sys
from code_12 import get_fibonacci_number
from code_12 import get_fibonacci_number_sequence

import random

def check_if_file_exists():
    try:
        exists = os.path.exists("code_12.py")
        assert exists == True
    except:
        sys.exit()

def test_get_fibonacci_number():
    check_if_file_exists()

def test_get_fibonacci_number_sequence():
    check_if_file_exists()
    