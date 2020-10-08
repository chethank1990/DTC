from objects.Account import Account
from objects.CommonActions import CommonActions
from objects.GlobalNavigation import GlobalNavigation
from objects.HomePage import HomePage
from objects.SearchLandingPage import SearchLandingPage
from objects.ShowBrowse import ShowBrowse
from tests.test_wclogin import TestWCLogin
from tests.test_wcskip import TestWCSkip


class TestGlobalNav(TestWCSkip):


    def test_globalnav(self,test_wcskip):
        log = self.getLogger()
        globalnav = GlobalNavigation(self.driver)
        homepage = HomePage(self.driver)
        showbrowse = ShowBrowse(self.driver)
        searchbrowse = SearchLandingPage(self.driver)
        account = Account(self.driver)

        assert homepage.gethomeherocarousel().is_displayed()
        log.info("Home page loaded successfully")

        globalnav.getmylistbutton().click()
        #pending to add page load

        globalnav.getbrowsebutton().click()
        assert showbrowse.gettrednding().is_displayed()
        log.info("Search page loaded successfully")

        globalnav.getsearchbutton().click()
        trendingshows = searchbrowse.gettrendingshows()
        assert trendingshows[0].text == "Trending Shows"
        log.info("Show Browse page loaded successfully")


        globalnav.getaccountbutton().click()
        myaccount = account.getitemlistinaccount()
        assert myaccount[0].text == "Manage Account"
        log.info("Account page loaded successfully")


        globalnav.gethomebutton().click()
        assert homepage.gethomeherocarousel().is_displayed()
        log.info("Home page loaded successfully again")


