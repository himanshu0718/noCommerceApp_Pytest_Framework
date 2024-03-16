import time
import pytest
from pageObjects.LoginPage import Login
from pageObjects.AddCostumerPage import AddCustomer
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
import string
import random
from selenium.webdriver.common.by import By

class Test_003_AddCustomer:
    baseUrl = ReadConfig.getApplicationurl()
    useremail = ReadConfig.getUserEmail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    @pytest.mark.sanity
    def test_Add_Customer(self, setup):
        self.logger.info("*** Test Case 003 - Add Customer ***")
        self.driver=setup   
        self.driver.get(self.baseUrl)
        self.driver.maximize_window()
        self.driver.implicitly_wait(20)

        self.lp = Login(self.driver)
        self.lp.setUserName(self.useremail)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("*** login successful ***")
        self.logger.info("*** Starting Add Customer Test ***")

        self.addcust = AddCustomer(self.driver)
        self.addcust.clickOnCustomerMenu()
        self.addcust.clickonCustomerMenuItem()
        self.addcust.clickOnAddNew()
        self.logger.info("**** providing customer info *****")
        self.email = random_gen()+"@gmail.com"
        self.addcust.setEmail(self.email)
        self.addcust.setPassword("test123")
        self.addcust.setFirstName("Himanshu")
        self.addcust.SetLastName("Sharma")
        self.addcust.SetGender("male")
        self.addcust.setDOB("02/25/2024")                # format - MM / DD / YYYY
        self.addcust.setCompanyName("Google")
        self.addcust.setTaxExempt("yes")
        self.addcust.setNewsletter("Your store name")
        self.addcust.setCustomerRoles("Forum")
        self.addcust.setVendor("Vendor 1")
        self.addcust.setActive("yes")
        self.addcust.setAdminComment("This is for testing...........")
        self.addcust.clickSave()

        self.logger.info("**** saving customer info *****")
        self.logger.info("**** Add customer validation started *****")

        self.msg = self.driver.find_element(By.TAG_NAME,"body").text
        # print(self.msg)
  
        try:
            if 'customer has been added successfully.' in self.msg:
                assert True == True
                self.logger.info("***Add Customer Tc Passed")
            else:
                self.driver.save_screenshot(".\\Screenshots\\"+"test_addCustomer_fail.png")
                self.logger.info("*** Add customer TC failed ****")
                assert True == False
        finally:
            self.driver.close()
            self.logger.info("***  Ending TC ****")

def random_gen(size=8, chars=string.ascii_lowercase+string.digits):
    return ''.join(random.choice(chars) for x in range(size))



