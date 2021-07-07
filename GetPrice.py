# import time module for scheduling
import time
# import required functions from selenium module for automation
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
def GetPrice():
    driver = webdriver.Chrome("")
    driver.get("https://ethereumprice.org/live/")
    try:
        price = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "")))
        return price
    except:
        return "error occured"

