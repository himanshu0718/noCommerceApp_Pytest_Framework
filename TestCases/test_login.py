from selenium import webdriver
import pytest
from pageObjects.LoginPage import Login
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

class Test_001_Login:
    baseUrl = ReadConfig.getApplicationurl()
    useremail = ReadConfig.getUserEmail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_homePageTitle(self,setup):
        self.logger.info("********** Test_001_Login *********")
        self.logger.info("********** Verifying Home Page Title *********")
        self.driver = setup
        self.driver.get(self.baseUrl)
        act_title = self.driver.title
        if act_title=="Your store. Login":
            assert True
            self.driver.close()
            self.logger.info("********** Home Page Title Test is passed *********")
            

        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"test_homePageTitle.png")
            self.driver.close()
            self.logger.error("********** Home Page Title Test is Failed *********")
            assert False

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_login(self,setup):
        self.logger.info("********* Verifying login Test *********")
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.lp = Login(self.driver)
        self.lp.setUserName(self.useremail)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        act_title = self.driver.title
        if act_title == "Dashboard / nopCommerce administration":
            assert True
            self.logger.info("********* login Test is Passed *********")
            self.driver.close()

        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"test_login.png")
            self.driver.close()
            self.logger.error("********* login Test is Failed *********")
            assert False

