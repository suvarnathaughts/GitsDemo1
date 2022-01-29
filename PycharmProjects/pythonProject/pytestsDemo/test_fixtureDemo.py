import pytest


@pytest.mark.usefixtures("setup")
class TestExample:

    def test_fixturedemo(self):
        print("i will be executing steps in fixture demo method")

    def test_fixturedemo1(self):
        print("i will be executing steps in fixture demo1 method")

    def test_fixturedemo2(self):
        print("i will be executing steps in fixture demo2 method")

    def test_fixturedemo3(self):
        print("i will be executing steps in fixture demo3 method")
