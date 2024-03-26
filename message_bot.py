from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time 

driver = webdriver.Chrome("C:/Users/Benji/chromedriver.exe")
driver.get("https://www.linkedin.com")
time.sleep(2)

username = driver.find_element(by=By.NAME, value="session_key")
password = driver.find_element(by=By.NAME, value="session_password")

username.send_keys('your email here')
password.send_keys('your password here')
time.sleep(2)

submit = driver.find_element(by=By.XPATH, value='//*[@id="main-content"]/section[1]/div/div/form/div[2]/button')
submit.click()
time.sleep(6)

driver.get("https://www.linkedin.com/search/results/people/?origin=SWITCH_SEARCH_VERTICAL&sid=FVZ")
time.sleep(6)

all_buttons = driver.find_elements(by=By.XPATH, value="//button[@aria-label='Message ']")
message_buttons = [btn for btn in all_buttons if btn.text == "Message"]
message_buttons[0].click()
time.sleep(2)

main_div = driver.find_element(by=By.XPATH, value="//div[starts-with(@class, 'msg-form__msg-content-container')]")
main_div.click()

paragraphs = driver.find_elements(by=By.TAG_NAME, value="p")

# # Figure out the index of the paragraph we want to target.
# # counter = 0
# # for p in paragraphs:
# #     print(counter)
# #     print(p.text)
# #     counter += 1

paragraphs[-5].send_keys('testing')
time.sleep(2)
# submit = driver.find_element(by=By.XPATH, value='//button[@type='submit']').click()

close_button = driver.find_element(by=By.XPATH, value='/html/body/div[4]/aside/div[2]/header/div[3]/button[2]').click()

time.sleep(20)