import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from  selenium.webdriver.support.ui import WebDriverWait 
from  selenium.webdriver.support import  expected_conditions as EC

# Set up the service using the WebDriver Manager
service = Service(ChromeDriverManager().install())

# Initialize the Chrome WebDriver with the service object
driver = webdriver.Chrome(service=service)

# Open the website
driver.get("https://orteil.dashnet.org/cookieclicker/")
cookie_id = "bigCookie"

WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'English')]"))
)

language = driver.find_element(By.XPATH, "//*[contains(text(), 'English')]")
language.click()

WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.ID, cookie_id ))
)

cookie = driver.find_element(By.ID, cookie_id)


while True:
    cookie.click()
    cookie_count = driver.find_element(By.ID, cookie_id).text
    print(cookie_count)



