import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By

class AddCustomer:      
    #Add Customer Page
    main_customer_xpath = "//a[@href='#']/p[contains(text(),'Customers')]"
    inside_customer_xpath = "//ul[@class='nav nav-treeview']/li[1]//p[contains(text(),'Customers')]"
    Add_new_button_xpath = "//a[@class='btn btn-primary']"
    email_xpath = "//input[@id='Email']"
    Password_xpath = "//input[@id='Password']"
    First_name_xpath = "//input[@id='FirstName']"
    Last_name_xpath = "//input[@id='LastName']"
    Gender_male_xpath = "//input[@id='Gender_Male']"
    Gender_Female_xpath = "//input[@id='Gender_Female']"
    DOB_xpath = "//input[@id='DateOfBirth']"
    Company_name_xpath = "//input[@id='Company']"
    tax_exempt_xpath = "//input[@id='IsTaxExempt']"
    Newsletter_xpath = "(//div[@class = 'k-multiselect-wrap k-floatwrap'])[1]"
    Newsletter_yourStoreName_xpath = "//option[contains(text(),'Your store name')]"
    Newsletter_TestStore2_xpath = "//option[contains(text(),'Test store 2')]"
    Customer_roles_xpath = "(//div[@class = 'k-multiselect-wrap k-floatwrap'])[2]"
    lst_Administrator_xpath = "//option[contains(text(),'Administrators')]"
    lst_Forum_xpath = "//option[contains(text(),'Forum Moderators')]"
    lst_Guests_xpath = "//option[contains(text(),'Guests')]"
    lst_Registered_xpath = "//option[contains(text(),'Registered')]"
    lst_Vendors_xpath = "//option[contains(text(),'Vendors')]"
    Mananger_vendor_xpath = "//select[@id='VendorId']"
    lst_vendor_1_xpath = "//option[contains(text(),'Vendor 1')]"
    lst_vendor_2_xpath = "//option[contains(text(),'Vendor 2')]"
    Active_xpath = "//input[@id='Active']"
    Admin_comment_xpath = "//textarea[@id='AdminComment']"
    save_button_xpath = "//button[@name='save']"

    def __init__(self,driver):
        self.driver = driver

    def clickOnCustomerMenu(self):
        self.driver.find_element(By.XPATH,self.main_customer_xpath).click()

    def clickonCustomerMenuItem(self):
        self.driver.find_element(By.XPATH,self.inside_customer_xpath).click()

    def clickOnAddNew(self):
        self.driver.find_element(By.XPATH,self.Add_new_button_xpath).click()

    def setEmail(self,email):
        self.driver.find_element(By.XPATH,self.email_xpath).send_keys(email)
    
    def setPassword(self,password):
        self.driver.find_element(By.XPATH,self.Password_xpath).send_keys(password)

    def setFirstName(self,firstname):
        self.driver.find_element(By.XPATH,self.First_name_xpath).send_keys(firstname)

    def SetLastName(self,lastname):
        self.driver.find_element(By.XPATH,self.Last_name_xpath).send_keys(lastname)

    def SetGender(self,gender):
        if gender=="female":
            self.driver.find_element(By.XPATH,self.Gender_Female_xpath).click()
        else:
            self.driver.find_element(By.XPATH,self.Gender_male_xpath).click()
    
    def setDOB(self,dob):
        self.driver.find_element(By.XPATH,self.DOB_xpath).send_keys(dob)
    
    def setCompanyName(self, company):
        self.driver.find_element(By.XPATH,self.Company_name_xpath).send_keys(company)
    
    def setTaxExempt(self, tax):
        if tax == "yes":
            self.driver.find_element(By.XPATH,self.tax_exempt_xpath).click()
        else:
            pass
    
    def setNewsletter(self, newsletter):
        self.driver.find_element(By.XPATH,self.Newsletter_xpath).click()
        if newsletter == "Test store 2":
            self.nlst = self.driver.find_element(By.XPATH,self.Newsletter_TestStore2_xpath)
        else:
            self.nlst = self.driver.find_element(By.XPATH,self.Newsletter_yourStoreName_xpath)
        self.driver.execute_script("arguments[0].click;",self.nlst)
        self.driver.find_element(By.XPATH,"//label[@id='SelectedNewsletterSubscriptionStoreIds_label']").click()
       

    def setCustomerRoles(self, role):
        self.driver.find_element(By.XPATH,self.Customer_roles_xpath).click()
        time.sleep(2)
        if role == "Registered":
            self.list_item = self.driver.find_element(By.XPATH,self.lst_Registered_xpath)
        elif role == "Administrators":
            self.list_item = self.driver.find_element(By.XPATH,self.lst_Administrator_xpath)
        elif role == "Forum":
            self.list_item = self.driver.find_element(By.XPATH,self.lst_Forum_xpath)
        elif role == "Guests":
            self.driver.find_element(By.XPATH,"//span[@title='delete']")
            self.list_item = self.driver.find_element(By.XPATH,self.lst_Guests_xpath)
        else:
            self.list_item = self.driver.find_element(By.XPATH,self.lst_Vendors_xpath)
        self.driver.execute_script("arguments[0].click;",self.list_item)
    
    def setVendor(self, vendor):
        drp = Select(self.driver.find_element(By.XPATH,self.Mananger_vendor_xpath))
        drp.select_by_visible_text(vendor)
    
    def setActive(self, active):
        if active == "yes":
            self.driver.find_element(By.XPATH,self.Active_xpath).click()
        else:
            pass
    
    def setAdminComment(self,comment):
        self.driver.find_element(By.XPATH,self.Admin_comment_xpath).send_keys(comment)

    def clickSave(self):
        self.driver.find_element(By.XPATH,self.save_button_xpath).click()

        


    

    
        


    
    

    

    

    
        
    

    
    
    





    



    
    




