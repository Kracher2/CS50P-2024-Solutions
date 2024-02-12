from test_plates.plates import is_valid


def test_valid():
    assert is_valid("AB123") == True


def test_start():
    assert is_valid("A1234") == False
    assert is_valid("1234") == False
    assert is_valid("1234A") == False
    assert is_valid("12A34") == False


def test_len():
    assert is_valid("ABC1234") == False
    assert is_valid("AB123346") == False
    assert is_valid("3") == False
    assert is_valid("0") == False


def test_num_punct():
    assert is_valid("AB123A") == False
    assert is_valid("AB1.34") == False
    assert is_valid("AB?123") == False
    assert is_valid("AB1 34") == False
    assert is_valid("AB12!4") == False
    assert is_valid("AB0123") == False
