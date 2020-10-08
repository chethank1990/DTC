from itertools import count

import pytest

from objects.GlobalNavigation import GlobalNavigation
from objects.SearchLandingPage import SearchLandingPage
from objects.ShowLandingPage import ShowLandingPage
from testdata.SearchData import SearchData
from tests.test_wclogin import TestWCLogin
from tests.test_wcskip import TestWCSkip
from utilities.BaseClass import BaseClass


class TestBasicVideoPlayer(TestWCSkip ):

    def test_basicvideoPlayer(self, test_wcskip , getsearchdata):
        globalnav = GlobalNavigation( self.driver )
        searchlandingpage = SearchLandingPage( self.driver )
        showlandingpage = ShowLandingPage( self.driver )

        globalnav.getsearchbutton().click()
        searchlandingpage.getsearchtextbox().click()
        searchlandingpage.getsearchtextbox().send_keys(getsearchdata["searchtext"])
        self.driver.hide_keyboard()
        self.driver.implicitly_wait( 15 )
        searchshowtitles = searchlandingpage.getshowtitles()
        for searchshowtitle in searchshowtitles:
            if searchshowtitle.text == getsearchdata["showtitle"]:
                searchshowtitle.click()
                break
        showlandingpage.getwatchnowbutton().click()

    @pytest.fixture(params=SearchData.test_searchdata)
    def getsearchdata(self,request):
        return request.param
