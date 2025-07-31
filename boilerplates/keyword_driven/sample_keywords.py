# Sample keywords for Keyword Driven Framework
from selenium import webdriver

def open_browser(url):
    driver = webdriver.Chrome()
    driver.get(url)
    return driver

def login(driver, username, password):
    driver.find_element(*Locators.USERNAME_FIELD).send_keys(username)
    driver.find_element(*Locators.PASSWORD_FIELD).send_keys(password)
    driver.find_element(*Locators.LOGIN_BUTTON).click()
