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
  
    
   
    def test_Billing(self,booting_function):   
        self.driver.find_element(by=By.NAME,value=locators.Logi_Locators().username_inputBox).send_keys(data.Logi_Data().username)
        self.driver.find_element(by=By.NAME,value=locators.Logi_Locators().password_inputBox).send_keys(data.Logi_Data().password)
        sleep(5)
        self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().signButton).click()
        sleep(10)
        self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().side_bar).click()
        sleep(5)
        self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().customer_order).click()
        sleep(5)
        self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().karigar_allotment).click()
        assert self.driver.title == 'Logimax Technology | Admin'
        print('karigar allotment Page open successfully' )
        sleep(5)
        self.driver.find_element(by=By.ID,value=locators.Logi_Locators().date_range).click()  
        sleep(5)
        self.driver.find_element(by=By.NAME,value=locators.Logi_Locators().Start_date).clear() 
        sleep(5)
        self.driver.find_element(by=By.NAME,value=locators.Logi_Locators().Start_date).send_keys(data.Logi_Data().From_date)
        assert self.driver.title == 'Logimax Technology | Admin'
        print('Start date : {a}'.format(a =data.Logi_Data().From_date))
        sleep(5)
        self.driver.find_element(by=By.NAME,value=locators.Logi_Locators().End_date).clear()
        sleep(5)
        self.driver.find_element(by=By.NAME,value=locators.Logi_Locators().End_date).send_keys(data.Logi_Data().To_date)
        assert self.driver.title == 'Logimax Technology | Admin'
        print('End date : {a}'.format(a =data.Logi_Data().To_date))
        self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().apply_date).click()
        sleep(5)
        self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().Search_option).send_keys(data.Logi_Data().search_id)
        sleep(5)    
        self.driver.find_element(by=By.NAME,value=locators.Logi_Locators().check_box).click()
        sleep(5)
           
        self.driver.find_element(by=By.NAME,value=locators.Logi_Locators().Assign_to).click()
        sleep(5)
        self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().update_order).click()
        order=self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().text_box)
        order.send_keys('SRI MURUGAN  Nagai Maligai')
        order.send_keys(Keys.RETURN)
        assert self.driver.title == 'Logimax Technology | Admin'
        print('update order : {a}'.format(a ='SRI MURUGAN  Nagai Maligai'))
        sleep(5)
        self.driver.find_element(by=By.ID,value=locators.Logi_Locators().Assigned).click()
        assert self.driver.title == 'Logimax Technology | Admin'
        print('Order Assigned Successfully completed')