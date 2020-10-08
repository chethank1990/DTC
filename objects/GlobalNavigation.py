from selenium.webdriver.common.by import By


class GlobalNavigation:

    def __init__(self, driver):
        self.driver = driver

    homebutton = (By.XPATH, '//android.widget.FrameLayout[@content-desc="Home"]')
    mylistbutton = (By.XPATH, '//android.widget.FrameLayout[@content-desc="My List"]')
    browsebutton = (By.XPATH, '//android.widget.FrameLayout[@content-desc="Browse"]')
    searchbutton = (By.XPATH, '//android.widget.FrameLayout[@content-desc="Search"]')
    accountbutton = (By.XPATH, '//android.widget.FrameLayout[@content-desc="Account"]')

    def gethomebutton(self):
        return self.driver.find_element( *GlobalNavigation.homebutton )

    def getmylistbutton(self):
        return self.driver.find_element( *GlobalNavigation.mylistbutton )

    def getbrowsebutton(self):
        return self.driver.find_element( *GlobalNavigation.browsebutton )

    def getsearchbutton(self):
        return self.driver.find_element( *GlobalNavigation.searchbutton )

    def getaccountbutton(self):
        return self.driver.find_element( *GlobalNavigation.accountbutton )