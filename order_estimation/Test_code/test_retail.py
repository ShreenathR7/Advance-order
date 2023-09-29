# app.py - The main executable file
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from pynput.keyboard import Key,Controller
from time import sleep
from Test_locators import locators
from Test_data import data
import pytest


class Test_Logimax:
    @pytest.fixture
    

    def booting_function(self):
       self.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
       self.driver.get(data.Logi_Data().url)
       self.driver.maximize_window()
       self.driver.implicitly_wait(5)
  
    
   
    def test_Estimation(self,booting_function):   
        self.driver.find_element(by=By.NAME,value=locators.Logi_Locators().username_inputBox).send_keys(data.Logi_Data().username)
        self.driver.find_element(by=By.NAME,value=locators.Logi_Locators().password_inputBox).send_keys(data.Logi_Data().password)
        sleep(8)
        self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().signButton).click()
        sleep(10)
        self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().side_bar).click()
        sleep(20)
        self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().estimation).click()
        sleep(20)
        self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().Add_Estimation).click()
        assert self.driver.title == "Logimax Technology | Admin"
        print("Estimation Open Successfully")
        sleep(5)
        self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().Branch).click()
        sleep(5)
        branch = self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().text_box)
        branch.send_keys('Head OFFICE')
        branch.send_keys(Keys.RETURN) 
        assert self.driver.title == "Logimax Technology | Admin"
        print('Branch Name : {a}'.format(a = "HEAD OFFICE"))
        sleep(5)
        self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().Sales_Employee).click()
        sleep(5)
        employee = self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().text_box)
        employee.send_keys('111-Logimax Developer')
        employee.send_keys(Keys.RETURN)
        assert self.driver.title == "Logimax Technology | Admin" 
        print("Sales Employee : {a}".format(a = "111-Logimax Developer"))
        sleep(5)
        customer = self.driver.find_element(by=By.ID,value=locators.Logi_Locators().Customer)
        sleep(10)
        customer.send_keys('VIJAY')
        sleep(5)
        customer.send_keys(Keys.BACK_SPACE)
        sleep(10)
        se_ver = self.driver.find_elements(By.XPATH, "//ul[@id='ui-id-1']//li")
        print('Total',len(se_ver))
        customer_name = 'VIJAY-8989712430'
        for element in se_ver:
            if element.text == customer_name:
                element.click()
                break
        assert self.driver.title == "Logimax Technology | Admin"    
        print('Customer Name : {a}'.format(a = customer_name))    
            
        sleep(30)
        self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().Close).click()    
        sleep(5)
        self.driver.find_element(by=By.ID,value=locators.Logi_Locators().tag_checkbox).click()
        
        Name = self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().label).text
        assert self.driver.title == "Logimax Technology | Admin"
        print("Selected Checkbox Name : {a}".format(a = Name))
        sleep(5)
        self.driver.find_element(by=By.ID,value=locators.Logi_Locators().order).send_keys(data.Logi_Data().tag_scan_code)
        assert self.driver.title == "Logimax Technology | Admin"
        print("Oder Id : {a}".format(a = data.Logi_Data().tag_scan_code))
        sleep(5)
        self.driver.find_element(by=By.ID,value=locators.Logi_Locators().search).click()
        
        sleep(20)
        self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().employee).click()
        sleep(5)
        branch = self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().text_box)
        branch.send_keys('111-Logimax Developer')
        branch.send_keys(Keys.RETURN)
        assert self.driver.title == "Logimax Technology | Admin"
        print("Employee Name : {a}".format(a = "111-Logimax Developer"))
        sleep(5)
        
        self.driver.find_element(by=By.NAME,value=locators.Logi_Locators().wastage_per).clear()
        sleep(5)
        self.driver.find_element(by=By.NAME,value=locators.Logi_Locators().wastage_per).send_keys(data.Logi_Data().wastage_value)    
        assert self.driver.title == "Logimax Technology | Admin"
        print("wastage Percentage : {a}".format(a = data.Logi_Data().wastage_value))
        sleep(5)
        MC = Select (self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().MC_Type))
        MC.select_by_value('2')
        selected_option = MC.first_selected_option
        selected_text = selected_option.text
        assert self.driver.title == 'Logimax Technology | Admin'
        print("MC Type : {a}".format(a = selected_text))
        
        self.driver.find_element(by=By.ID,value=locators.Logi_Locators().save_print).click()
        name = self.driver.find_element(by=By.ID,value=locators.Logi_Locators().save_print).text
        assert self.driver.title == 'Logimax Technology | Admin'
        print('Clickable Name : {a}'.format(a = name))
        print("Estimation adding successfully")
        
       
        
        
        
        
        
        
        
 