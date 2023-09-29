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
from datetime import datetime

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
        sleep(5)
        show = Select(self.driver.find_element(by=By.NAME,value=locators.Logi_Locators().Show))
        show.select_by_value('50')
        sleep(5)
        date = self.driver.find_elements(by=By.XPATH,value=locators.Logi_Locators().data_range)
        date_list=[]
        for  i in date:
             a =(i.text)
             date_list.append(a)
        #print("No of entry :"(len(date_list))) 
        unique_dates = set()

        # Iterate through the date_list and add unique dates to the set
        for date_str in date_list:
            unique_dates.add(date_str)
        sorted_dates = sorted(unique_dates, key=lambda x: datetime.strptime(x, '%d-%m-%Y'))
        # Count the number of unique days
        start_date = sorted_dates[0]
        end_date = sorted_dates[-1]

        start_date = datetime.strptime(start_date, '%d-%m-%Y').date()
        end_date = datetime.strptime(end_date, '%d-%m-%Y').date()

        delta = end_date - start_date
        number_of_days = delta.days
        print(f"Number of days between {start_date} and {end_date}: {number_of_days} days")
         
        if 21 <= number_of_days <= 30:  # Adjust the range as needed
           print("Number of days is visible for an acceptable duration.")
        else:
           print(f"Number of days is visible for {number_of_days} days, which is not within the expected range.")
           
        sleep(5)
        self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().karigar).click()
        sleep(5)
        selected_Karigar = "SRI MURUGAN  Nagai Maligai"
        karigar = self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().text_box)
        karigar.send_keys(selected_Karigar)
        karigar.send_keys(Keys.RETURN)   
        sleep(5)
        show = Select(self.driver.find_element(by=By.NAME,value=locators.Logi_Locators().Show))
        show.select_by_value('50')   
        
        filter = self.driver.find_elements(by=By.XPATH,value=locators.Logi_Locators().filter_karigar)
        filter_Karigar=[]  
        for  i in filter:
             a =(i.text)
             filter_Karigar.append(a)   

        unique = set(filter_Karigar) 
        #print(unique)
        result_string = ' '.join(unique)
        #print(result_string)

        
        if result_string == selected_Karigar:  
           print("Karigar Filter option Working Successfully")
        else:
           print(f"karigar Filter option Selected {selected_Karigar} : output {result_string} list, which is not within the expected output.")
           
        sleep(5)
        self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().branch).click()
        sleep(5)
        selected_branch = "CHINNA ANNAN JEWELLERY"
        branch = self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().text_box)
        branch.send_keys(selected_branch)
        branch.send_keys(Keys.RETURN)
        
        sleep(5)
        show = Select(self.driver.find_element(by=By.NAME,value=locators.Logi_Locators().Show))
        show.select_by_value('50')
    
        filter = self.driver.find_elements(by=By.XPATH,value=locators.Logi_Locators().fiter_option)
        filter_list=[]  
        for  i in filter:
             a =(i.text)
             filter_list.append(a)  
             unique = set(filter_list) 
        #print(unique)
        result_string = ' '.join(unique)
        #print(result_string)   
        if selected_branch == result_string:  
           print("Branch Filter option Working Successfully")
        else:
           print(f"Branch Filter option Selected {selected_branch} : output {result_string} list, which is not within the expected output.")
    
        items = self.driver.find_elements(by=By.XPATH,value=locators.Logi_Locators().items)
        items_list = []
        for i in items:
            a = (i.text) 
            items_list.append(a)
        #print(items_list)
        total = 0
        for value in items_list:
            total = total+int(value)
        print('Total No Of Items :',total )
        
        