from seasons import date_to_minutes, get_birth, make_sentence
import pytest

def test_date_to_minutes():
    assert date_to_minutes(2023, 2, 11) == 525600

def test_make_sentence():
    assert make_sentence(525600) == "Five hundred twenty-five thousand, six hundred"
    assert make_sentence(0) == "Zero"
