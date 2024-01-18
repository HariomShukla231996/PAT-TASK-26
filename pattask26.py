# data.py  file content

class Web_Data:
    url = "https://www.imdb.com/search/name/"
    movie_name = "Uri: The Surgical Strike"

# locators.py file content

class Web_Locators:
    search_locator = "//input[@id='suggestion-search']"
    password_locator = ""
    submit_button_locator = "//button[@id='suggestion-search-button']//*[name()='svg']//*[name()='path' and contains(@d,'M15.5 14h-')]"

# main.py file content

from Data import data
from Locators import locators
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC




class Hari:
    driver = webdriver.Chrome()


def start(self):
    self.driver.maximize_window()
    self.driver.get(data.Web_Data().url)
    self.driver.implicity_wait(5)


def search_page(self):
    self.driver.find_element(by=By.XPATH, value=locators.Web_Locators().search_locator).clear()
    self.driver.find_element(by=By.XPATH, value=locators.Web_Locators().search_locator).send_keys(data.Web_Data().movie_name)
    self.driver.find_element(by=By.XPATH, value=locators.Web_Locators().submit_button_locator)
    self.driver.implicity_wait(5)
    self.driver.quit()


if __name__ == '__main__':
    hari = Hari()
    hari.start()
    hari.search_page()