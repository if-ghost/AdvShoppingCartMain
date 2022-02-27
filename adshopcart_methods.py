import sys
import datetime
import adshopcart_locators as locators

from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
s = Service(executable_path='C:\\Users\IT Productivity Hub\PycharmProjects\pythonProject\chromedriver.exe')
driver = webdriver.Chrome(service = s)
###


def setUp():
    print(f'Test started at: {datetime.datetime.now()}')

    # Make window full screen
    driver.maximize_window()

    # Let's wait for the browser response
    driver.implicitly_wait(30)

    # Navigate to the website
    driver.get(locators.adshopcart_url)

    # Check that we're at the correct URL address, and we're seeing the correct title
    # Here we separate checks for URL and title, to be able to determine which is passing, and which is failing.
    if driver.current_url == locators.adshopcart_url:
        print(f'We\'re at the Advantage Shopping Cart homepage -- {driver.current_url}')
    else:
        print(f'We\'re not at the advantage shopping cart homepage. Please check your code and try again.')
        driver.close()
        driver.quit()
    # &nbsp; represents a non-breaking space in html. We will use the Unicode representation instead: u'\xa0'
    if driver.title == u'\xa0Advantage Shopping':
        print(f'We\'re seeing the correct title: "Advantage Shopping"')
    else:
        print(f'We\'re not seeing the correct title. Please check your code and try again.')
        driver.close()
        driver.quit()

def tearDown():
    if driver is not None:
        print(f'------------')
        print(f'Test completed at: {datetime.datetime.now()}')
        driver.close()
        driver.quit()

