from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class Func:
    def __init__(self):
        self.base_url = 'https://b2c.passport.rt.ru/'

    def log_in(self, auth_var, log_data, password):
        driver_service = Service(executable_path="/testsdrivers/chromedriver.exe")
        driver = webdriver.Chrome(service=driver_service)
        driver.get('https://b2c.passport.rt.ru/')

        auth_but = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, auth_var)))
        auth_but.click()

        input_log = driver.find_element('id', 'username')
        input_log.clear()
        input_log.send_keys(log_data)

        input_pass = driver.find_element('id', 'password')
        input_pass.clear()
        input_pass.send_keys(password)

        button = driver.find_element('id', 'kc-login')
        button.click()
        return driver.current_url

    def open_page(self, but_id):
        driver_service = Service(executable_path="/testsdrivers/chromedriver.exe")
        driver = webdriver.Chrome(service=driver_service)
        driver.get('https://b2c.passport.rt.ru/')
        button = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, but_id)))
        button.click()
        return driver.current_url
