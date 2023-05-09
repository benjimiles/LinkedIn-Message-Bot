from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time 

driver = webdriver.Chrome("Path_to_chrome_driver")
driver.get("https://www.linkedin.com")

username = driver.find_element(by=By.NAME, value="session_key")
password = driver.find_element(by=By.NAME, value="session_password")