from selenium import webdriver
import time
import unittest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__)))
#import HtmlTestRunner
import HTMLTestRunner
#from SampleProject.Page.loginPage import LoginPage
#from SampleProject.Page.homePage import HomePage
from FirstAutomationScript.pages.loginPage import LoginPage
from FirstAutomationScript.pages.homePage import HomePage
print("anand")
print("pandey")
print("welcome to python")

class LoginTest(unittest.TestCase):
    @classmethod

    def setUpClass(brw):
        brw.driver = webdriver.Chrome(executable_path="/Users/priyamvadaanand/PycharmProjects/Automation_Python/FirstAutomationScript/drivers/chromedriver")
        brw.driver.implicitly_wait(10)
        brw.driver.maximize_window()
    def test_login_valid(orng):
        driver = orng.driver
        orng.driver.get("https://anand5581-trials65101.orangehrmlive.com/")
        login = LoginPage(driver)
        login.enter_username("admin")
        login.enter_password("Admin@123")
        login.click_login()

        homepage = HomePage(driver)
        homepage.click_account()
        homepage.click_logout()

        time.sleep(2)
    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()



if __name__ == '__main__':
    unittest.main(testRunner=HTMLTestRunner.HTMLTestRunner(output='/Users/priyamvadaanand/PycharmProjects/Automation_Python/FirstAutomationScript/reprts'))
    #unittest.main(testRunner=HTMLTestRunner.HTMLTestRunner(output='SampleProject/Report'))
