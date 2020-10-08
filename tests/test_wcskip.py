import pytest

from utilities.BaseClass import BaseClass
from objects.WelcomeScreen import WelcomeScreen


class TestWCSkip( BaseClass ):
    @pytest.fixture()
    def test_wcskip(self):
        wcskip = WelcomeScreen( self.driver )
        wcskip.getdebugskip().click()
