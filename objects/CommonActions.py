from appium.webdriver.common.touch_action import TouchAction


class CommonActions:

    def __init__(self, driver):
        self.driver = driver


    def getverticalupscroll(self):
        touch = TouchAction(self.driver)
        return touch.press( x=710, y=1666 ).move_to( x=725, y=775 ).release().perform()
