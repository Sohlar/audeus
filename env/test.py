from pydoc import pager
from tracemalloc import start
from selenium import webdriver
import pandas as pd
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
import time


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://www.google.com/")
time.sleep(3)
currentElem = driver.switch_to.active_element
print("Value of CSS: " + currentElem.value_of_css_property())

print("aria_role: " + currentElem.aria_role)
print("acessible_name: " + currentElem.accessible_name)
print("location: " + currentElem.location)
print("parent: " + currentElem.parent)
driver.find_element(By.id, currentElem.id).send_keys("Please god work")

start
    load page
        click element
            add to script
                y
                    execute JS (active_element) -> xpath function -> return Xpath to python
                n