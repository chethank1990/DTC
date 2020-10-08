from selenium.webdriver.common.by import By


class Account:

    def __init__(self,driver):
        self.driver = driver

    itemlistinaccount = (By.ID, "titleText")

    def getitemlistinaccount(self):
        return self.driver.find_elements(*Account.itemlistinaccount)

