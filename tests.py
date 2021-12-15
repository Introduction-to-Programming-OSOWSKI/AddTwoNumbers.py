#DO NOT TAMPER WITH THIS FILE
#ANY EDITS YOU MAKE TO THIS FILE WILL BE SAVED TO YOUR PUBLIC GITHUB HISTORY
#TAMPERING WITH THIS FILE WILL BE OBVIOUS AND WILL RESULT IN A ZERO

import main;
import datetime;

year = 2021
month = 12
day = 30

def test_code():
    assert main.add(11,23) == 34, "11 + 23 == 34 failed"
    assert main.add(1,1) == 2, "1 + 1 == 2 failed"
    assert main.add(100,55) == 155, "100 + 55 == 155 failed"

def test_late():
    assert datetime.datetime.now() < datetime.datetime(year, month, day + 1, 4, 0), "Submitted Late"
