# any pytest file should start with test_ or end with _test
#pytest method name should always start with test
#Any code should always be wrapped in method only
import pytest


@pytest.mark.smoke
def test_firstprogram():
    print("Hello")


def test_secondgreetCreditcard():
    print("Good Morning")


def test_crossbrowser(crossbrowser):
    print(crossbrowser[1])
