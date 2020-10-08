from selenium.webdriver.common.by import By


class HomePage:

    def __init__(self,driver):
        self.driver = driver

    railname = (By.ID, "sectionTitle")
    homeherocarousel = (By.XPATH,'//android.widget.ImageView[@content-desc="Carousel Item"]')


    def getrailname(self):
        return self.driver.find_element(*HomePage.railname)

    def gethomeherocarousel(self):
        return self.driver.find_element(*HomePage.homeherocarousel)