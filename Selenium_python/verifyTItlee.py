from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common import by
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager


class LoginApp:
    def loginapp(self):
        self.driver = webdriver.Chrome()
       # driver=webdriver.Chrome(executable_path="D:\BrowserDrivers\chromedriver.exe")
        #driver=webdriver.Firefox(executable_path="D:\BrowserDrivers/firefoxdriver.exe")
        self.driver.get("http://127.0.0.1/orangehrm-2.6/login.php");
        self.driver.find_element('name',"txtUserName").send_keys("nareshit");
        self.driver.find_element('xpath', '//input[@name="txtUserName"]')

        self.driver.find_element('name',"txtPassword")
        self.driver.find_element(by=By.NAME, value='txtPassword').send_keys("nareshit");

        self.driver.find_element('xpath',"//input[@name='Submit']").click();
        print(self.driver.title)


       # driver.close()

    def captureemplist(self,setup):
        print("Lets open Pim page")

    def thirdmethod(self):
        print("method 3")








hrm=LoginApp()
hrm.loginapp()
hrm.thirdmethod()
hrm.captureemplist()