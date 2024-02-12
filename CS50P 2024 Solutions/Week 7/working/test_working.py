from working import convert
import pytest


def test_normal():
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("11:30 AM to 11:00 PM") == "11:30 to 23:00"
    assert convert("9:00 PM to 5:00 AM") == "21:00 to 05:00"
    assert convert("9 PM to 5 AM") == "21:00 to 05:00"
    assert convert("5 AM to 9:00 PM") == "05:00 to 21:00"


def test_corner():
    with pytest.raises(ValueError):
        convert("cat")
    with pytest.raises(ValueError):
        convert("9:60 AM to 5:00 PM")
    with pytest.raises(ValueError):
        convert("13:00 AM to 5:00 PM")
    with pytest.raises(ValueError):
        convert("9:00 AM to 5:60 PM")
    with pytest.raises(ValueError):
        convert("9:00 AM to 15:00 PM")
    with pytest.raises(ValueError):
        convert("-9:00 AM to -10:00 PM")
    with pytest.raises(ValueError):
        convert("9:-50 AM to 15:-20 PM")
