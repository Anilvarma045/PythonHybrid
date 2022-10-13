from selenium import webdriver
from selenium.webdriver.common import by
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver import ActionChains

from selenium.webdriver import ActionChains
driver=webdriver.Chrome(executable_path="D:\BrowserDrivers\chromedriver.exe")
#driver=webdriver.Firefox(executable_path="D:\BrowserDrivers/firefoxdriver.exe")
#driver=webdriver.Ie(executable_path="D:\BrowserDrivers\IEDriverServer.exe")
driver.get("http://127.0.0.1/orangehrm-2.6/login.php");
driver.maximize_window()

driver.find_element('name',"txtUserName").send_keys("nareshit");
#driver.findElement(By.xpath("//input[@name='txtUserName']")).sendKeys("nareshit");
driver.find_element('xpath', '//input[@name="txtUserName"]')

driver.find_element('name',"txtPassword").send_keys("nareshit");
driver.find_element(by=By.NAME, value='txtPassword')

ele=driver.find_element('xpath',"//input[@name='Submit']")
ele.click();
ele2=driver.find_element('xpath','//*[@name="Sumbit"]')


action=ActionChains(driver)
action.drag_and_drop(ele,ele2)

action.double_click(ele).perform()

ss = Screenshot_clipping.Screenshot()
driver = webdriver.Chrome()

screen_shot = ss.full_screenshot(driver, save_path = "E:/BrowserDriver", image_name= 'name.png')


#   Handle Alerts

alert=driver.switch_to_alert()
alert.get().text
alert.accept()

driver.expected
   
print(driver.title)
#driver.close()
driver.back()
driver.forward()
driver.refresh()
time.sleep(3)





























