from jar import Jar
import pytest


def test_init():
    jar = Jar()
    assert jar.size == 0
    with pytest.raises(ValueError):
        jar.deposit(20)


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar()
    with pytest.raises(ValueError):
        jar.deposit(20)
    with pytest.raises(ValueError):
        jar.deposit(-2)
    jar.deposit(4)
    assert jar.size == 4


def test_withdraw():
    jar = Jar()
    with pytest.raises(ValueError):
        jar.withdraw(20)
    with pytest.raises(ValueError):
        jar.withdraw(-10)
    jar.deposit(3)
    jar.withdraw(1)
    assert jar.size == 2
