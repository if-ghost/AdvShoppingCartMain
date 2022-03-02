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
    sleep(1)

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

def create_new_user():
    driver.find_element(By.ID, "menuUser").click()
    sleep(2)
    driver.find_element(By.XPATH, '//div/a[contains(., "CREATE NEW ACCOUNT")]').click()

    # Check that we're on the new user registration page
    if driver.current_url == 'https://advantageonlineshopping.com/#/register' and driver.title == u'\xa0Advantage Shopping':
        print("We\'re at the new user registration page")
    else:
        print("We\'re not at the registration page. Check your code and try again.")

    driver.find_element(By.NAME, 'usernameRegisterPage').send_keys(locators.new_username)
    print(locators.new_username)
    driver.find_element(By.NAME, 'passwordRegisterPage').send_keys(locators.new_password)
    print(locators.new_password)
    driver.find_element(By.NAME, 'confirm_passwordRegisterPage').send_keys(locators.new_password)
    driver.find_element(By.NAME, 'emailRegisterPage').send_keys(locators.new_email)
    driver.find_element(By.NAME, 'first_nameRegisterPage').send_keys(locators.new_firstname)
    driver.find_element(By.NAME, 'last_nameRegisterPage').send_keys(locators.new_lastname)
    driver.find_element(By.NAME, 'phone_numberRegisterPage').send_keys(locators.phone)

    Select(driver.find_element(By.NAME, "countryListboxRegisterPage")).select_by_visible_text('Canada')
    sleep(0.5)
    driver.find_element(By.NAME, 'cityRegisterPage').send_keys(locators.city)
    driver.find_element(By.NAME, "addressRegisterPage").send_keys(locators.address)
    driver.find_element(By.NAME, "postal_codeRegisterPage").send_keys(locators.postal_code)

    # Agree to the terms
    driver.find_element(By.NAME, 'i_agree').click()

    # Register
    driver.find_element(By.ID, 'register_btnundefined').click()
    sleep (1)

    # Check that new user was created
    if driver.current_url == 'https://advantageonlineshopping.com/#/' and driver.find_element(By.LINK_TEXT, locators.new_username).is_displayed():
        print('New user was successfully created.')

def check_my_account():
    driver.find_element(By.ID, 'menuUser').click()
    sleep(0.5)
    driver.find_element(By.XPATH, '//a/div/label[contains(., "My account")]').click()
    sleep(0.5)

    # if driver.find_element(By.XPATH, f'//div/div/label[contains(., {locators.full_name})]').is_displayed():
    #     print('Full name is displayed')
    # else:
    #     print('Full name is not displayed. Check code and try again')



    # check orders
    driver.find_element(By.ID, 'menuUser').click()
    sleep(0.5)
    driver.find_element(By.XPATH, '//a/div/label[contains(., "My orders")]').click()

    if driver.find_element(By.XPATH, '//div/label[contains(., "No orders")]').is_displayed():
        print('There are no orders')
    else:
        print('Order check error. Try again')

    # Sign out
    driver.find_element(By.ID, 'menuUser').click()
    sleep(0.5)
    driver.find_element(By.XPATH, '//a/div/label[contains(., "Sign out")]').click()
    sleep(0.25)

def delete_new_account():
    driver.find_element(By.ID, 'menuUser').click()
    sleep(0.25)
    driver.find_element(By.NAME, 'username').send_keys(locators.new_username)
    driver.find_element(By.NAME, 'password').send_keys(locators.new_password)
    sleep(0.5)
    driver.find_element(By.ID, 'sign_in_btnundefined').click()
    sleep(0.5)
    driver.find_element(By.ID, 'menuUser').click()
    sleep(0.25)
    driver.find_element(By.XPATH, '//a/div/label[contains(., "My account")]').click()
    sleep(0.25)

    driver.find_element(By.CLASS_NAME, 'deleteBtnText').click()
    sleep(1)
    # driver.find_element(By.CLASS_NAME, 'deletePopupBtn deleteRed').click()
    driver.find_element(By.XPATH, '/html/body/div[3]/section/article/div[2]/div[3]/div[1]').click()
    sleep(6)

def confirm_account_deletion():
    if driver.current_url == locators.adshopcart_url:
        driver.find_element(By.ID, 'menuUser').click()
        sleep(0.25)
        driver.find_element(By.NAME, 'username').send_keys(locators.new_username)
        driver.find_element(By.NAME, 'password').send_keys(locators.new_password)
        sleep(0.5)
        driver.find_element(By.ID, 'sign_in_btnundefined').click()
        sleep(0.5)
    if driver.find_element(By.XPATH, '//div/label[contains(., "Incorrect user name or password.")]').is_displayed():
        print('User deletion confirmed')





# setUp()
# create_new_user()
# check_my_account()
# delete_new_account()
# confirm_account_deletion()

