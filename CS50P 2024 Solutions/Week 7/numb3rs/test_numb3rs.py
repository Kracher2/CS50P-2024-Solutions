from numb3rs import validate


def test_all():
    assert validate("0.0.0.0") == True
    assert validate("55.55.55.55") == True
    assert validate("-1.0.-99.0") == False
    assert validate("350.350.350.350") == False
    assert validate("259.259.259.259") == False
    assert validate("255.259.259.259") == False
    assert validate("259.25.25.25") == False
