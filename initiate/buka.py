'''
Created on Dec 15, 2015

@author: Anthony.Makanju
'''
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

#iepath="C:\IEDriverServer_Win32_2.45.0\IEDriverServer.exe"
#driver=webdriver.Ie(iepath)
chromepath="C:\chromedriver_win32\chromedriver.exe"
driver=webdriver.Chrome(chromepath)
driver.get("http://amakanju.pythonanywhere.com/")#//http://amakanju.pythonanywhere.com/
print(driver.current_url)
print(driver.title)
driver.maximize_window()
driver.find_element_by_id("id_username").clear()
driver.find_element_by_id("id_username").send_keys("tmak")
driver.find_element_by_id("id_password").clear()
driver.find_element_by_id("id_password").send_keys("tmak")
driver.find_element_by_xpath("html/body/div[2]/div/div/form/input[2]").click()
driver.find_element_by_link_text("God is Good").click()
driver.back()
time.sleep(2)
driver.find_element_by_xpath("//a[@href='/post/3/']")
driver.back()
time.sleep(2)
driver.find_element_by_xpath("//a[@href='/accounts/logout/']")
driver.quit()
print("Automation complete!")
