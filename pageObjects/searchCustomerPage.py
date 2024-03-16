from selenium import webdriver
from selenium.webdriver.common.by import By

class SearchCustomer:
    driver = webdriver.Chrome()
    #Add Customer Page
    Email_ID = "SearchEmail"
    First_Name_ID = "SearchFirstName"
    Last_Name_ID = "SearchLastName"
    btn_Search_ID = "search-customers"

    table_xpath = "//table[@id='customers-grid']"
    table_rows_xpath = "//table[@id='customers-grid']/tbody/tr"
    table_columns_xpath = "//table[@id='customers-grid']/tbody/tr/td"

    def __init__(self, driver):
        self.driver = driver
    
    def setEmail(self, email):
        self.driver.find_element(By.ID,self.Email_ID).clear()
        self.driver.find_element(By.ID,self.Email_ID).send_keys(email)
    
    def setFirstName(self, firstname):
        self.driver.find_element(By.ID,self.First_Name_ID).clear()
        self.driver.find_element(By.ID,self.First_Name_ID).send_keys(firstname)

    def setLastName(self, lastname):
        self.driver.find_element(By.ID,self.Last_Name_ID).clear()
        self.driver.find_element(By.ID,self.Last_Name_ID).send_keys(lastname)
    
    def clickSearch(self):
        self.driver.find_element(By.ID,self.btn_Search_ID).click()

    def getNoofRows(self):
        return len(self.driver.find_elements
                   (By.XPATH,self.table_rows_xpath))
    
    def getNoofColumns(self):
        return len(self.driver.find_elements(By.XPATH,self.table_columns_xpath))

    def searchCustomerByEmail(self,email):
        flag = False
        for r in range(1, self.getNoofRows()+1):
            table = self.driver.find_element(By.XPATH,self.table_xpath)
            emailID = table.find_element(By.XPATH,"//table[@id='customers-grid']/tbody/tr["+str(r)+"]/td[2]").text
            if emailID == email:
                flag = True
                break
        return flag
    
    def searchCustomerByName(self,Name):
        flag = False
        for r in range(1, self.getNoofRows()+1):
            name = self.driver.find_element(By.XPATH,"//table[@id='customers-grid']/tbody/tr["+str(r)+"]/td[3]").text
            if name == Name:
                flag = True
                break
        return flag


    




    


    




