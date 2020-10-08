from selenium.webdriver.common.by import By


class WelcomeScreen:


    def __init__(self, driver):
        self.driver = driver

    debugskip = (By.ID, "debugSkipButton")
    welcomesignin = (By.ID, "welcomeSignIn")


    def getdebugskip(self):
        return self.driver.find_element(*WelcomeScreen.debugskip)

    def getwelcomesignin(self):
        return self.driver.find_element(*WelcomeScreen.welcomesignin)

