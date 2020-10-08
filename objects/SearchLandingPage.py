from selenium.webdriver.common.by import By


class SearchLandingPage:

    def __init__(self, driver):
        self.driver = driver

    searchtextbox = (By.ID, "searchTextView")
    showtitle = (By.ID,"title")
    trendingshows = (By.ID,'sectionTitle')

    def getsearchtextbox(self):
        return self.driver.find_element(*SearchLandingPage.searchtextbox)

    def getshowtitles(self):
        return self.driver.find_elements(*SearchLandingPage.showtitle)

    def gettrendingshows(self):
        return self.driver.find_elements(*SearchLandingPage.trendingshows)
