import pytest


#@pytest.mark.smoke
@pytest.mark.xfail
def test_firstprogram():
    msg = "Hello"
    assert msg == "Hi", "Test failed because strings do not match"


def test_secondCreditcard():
    a = 4
    b = 6
    assert a + 2 == 6, "Addition do not match"
