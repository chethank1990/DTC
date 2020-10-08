from selenium.webdriver.common.by import By


class ShowBrowse:

    def __init__(self,driver):
        self.driver = driver

    trending = (By.XPATH, '//androidx.appcompat.app.ActionBar.Tab[@content-desc="Trending"]/android.widget.TextView')


    def gettrednding(self):
        return self.driver.find_element(*ShowBrowse.trending)