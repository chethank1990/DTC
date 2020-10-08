from selenium.webdriver.common.by import By


class Login:

    def __init__(self, driver):
        self.driver = driver

    loginemail = (By.ID, "signInEmail")
    loginpassword = (By.ID, "signInPassword")
    logincontinue = (By.ID, "signInContinue")

    def getloginemail(self):
        return self.driver.find_element(*Login.loginemail)
    def getloginpassword(self):
        return self.driver.find_element(*Login.loginpassword)
    def getlogincontinue(self):
        return self.driver.find_element(*Login.logincontinue)
