from test_twttr.twttr import shorten


def test_all():
    assert shorten("hello world") == "hll wrld"
    assert shorten("HELLO WORLD") == "HLL WRLD"
    assert shorten("H?LL0 W*rlD") == "H?LL0 W*rlD"
