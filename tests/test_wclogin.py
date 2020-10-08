import pytest

from objects.Login import Login
from objects.WelcomeScreen import WelcomeScreen
from testdata.LoginData import LoginData
from utilities.BaseClass import BaseClass


class TestWCLogin( BaseClass ):


    @pytest.fixture()
    def test_wclogin(self,getlogindata):
        log = self.getLogger()
        wclogin = WelcomeScreen( self.driver )
        login = Login(self.driver)
        wclogin.getwelcomesignin().click()
        login.getloginemail().click()
        log.info("email id is "+getlogindata["email"])
        login.getloginemail().send_keys(getlogindata["email"])
        login.getloginpassword().click()
        log.info("Password is "+getlogindata["password"])
        login.getloginpassword().send_keys(getlogindata["password"])
        self.driver.back()
        login.getlogincontinue().click()

    @pytest.fixture(params=LoginData.test_logindata)
    def getlogindata(self,request):
        return request.param



