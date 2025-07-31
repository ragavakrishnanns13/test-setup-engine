# Sample utils for Hybrid Framework
import os
import time

def take_screenshot(driver, filename):
    directory = os.path.dirname(os.path.abspath(__file__))
    screenshot_path = os.path.join(directory, 'screenshots', filename)
    driver.save_screenshot(screenshot_path)

def wait_for_element(driver, locator, timeout=10):
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC

    try:
        element = WebDriverWait(driver, timeout).until(
            EC.presence_of_element_located(locator)
        )
        return element
    except:
        return None
