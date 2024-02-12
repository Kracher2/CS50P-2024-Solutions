from um import count


def test_all():
    assert count("um") == 1
    assert count("Album") == 0
    assert count("house") == 0
    assert count("Um, hey") == 1
    assert count("Um, hey, um...") == 2
    assert count(" um ") == 1
