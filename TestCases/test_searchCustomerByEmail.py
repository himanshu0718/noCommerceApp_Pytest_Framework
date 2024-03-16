import time
import pytest
from pageObjects.LoginPage import Login
from pageObjects.AddCostumerPage import AddCustomer
from pageObjects.searchCustomerPage import SearchCustomer
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
# from selenium import webdriver
import random
import string


class Test_004_SearchCustomerByEmail:
    baseURL = ReadConfig.getApplicationurl()
    useremail = ReadConfig.getUserEmail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()
    # driver = webdriver.Chrome()

    @pytest.mark.regression
    def test_searchCustomerByEmail(self, setup):
        self.logger.info("**** 004 Search customer by email ****")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.driver.implicitly_wait(20)

        self.lp = Login(self.driver)
        self.lp.setUserName(self.useremail)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("*** login successful ***")
        self.logger.info("*** Starting Search Customer by Email Test ***")
    
    
        self.addcust = AddCustomer(self.driver)
        self.addcust.clickOnCustomerMenu()
        self.addcust.clickonCustomerMenuItem()

        self.logger.info("*** searching customer by email ID")
        searchcust = SearchCustomer(self.driver)
        searchcust.setEmail("victoria_victoria@nopCommerce.com")
        searchcust.clickSearch()
        status = searchcust.searchCustomerByEmail("victoria_victoria@nopCommerce.com")
        # print(status)
        # status = True
        assert True==status
        self.logger.info("*** TC Search Customer by Email Test finished")
        self.driver.close()