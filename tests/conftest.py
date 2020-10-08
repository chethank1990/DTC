from appium.webdriver import webdriver
import pytest
import time

driver = None


@pytest.fixture(scope="class")
def setup(request):
    global driver
    desired_cap = {
        "platformName": "Android",
        "platformVersion": "10",
        "deviceName": "RZ8M30KCBXN",
        "app": "C:\\Users\\chethan.kumar\\PycharmProjects\DTC\\testdata\\dplus.apk",
        "appPackage": "com.discovery.discoveryplus.mobile.enterprise",
        "appActivity": "com.discovery.plus.presentation.activities.LaunchActivity",
        "appWaitDuration" : "60000"
    }

    driver = webdriver.WebDriver( 'http://localhost:4723/wd/hub', desired_cap )
    driver.implicitly_wait( 180 )
    request.cls.driver = driver
    yield
    #driver.close()

