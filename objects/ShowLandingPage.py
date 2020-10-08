from selenium.webdriver.common.by import By


class ShowLandingPage:

    def __init__(self,driver):
        self.driver = driver

    watchnowbutton = (By.ID, "watchNowButton")


    def getwatchnowbutton(self):
        return self.driver.find_element(*ShowLandingPage.watchnowbutton)