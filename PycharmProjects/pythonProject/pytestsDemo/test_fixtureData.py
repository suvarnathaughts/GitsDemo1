import pytest

from pytestsDemo.Baseclass import BaseClass


@pytest.mark.usefixtures("dataLoad")
class TestExample2(BaseClass):

    def test_editprofile(self, dataLoad):
        log = self.getLogger()
        log.info(dataLoad[1])
        log.info(dataLoad[2])
