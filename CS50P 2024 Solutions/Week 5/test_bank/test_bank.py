from test_bank.bank import value


def test_all():
    assert value("Hello") == 0
    assert value("hello") == 0
    assert value("Hey") == 20
    assert value("hey") == 20
    assert value("Bonjour") == 100
