from config import  url_01
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

class TopNavPage():

    def __init__(self, driver):
        self.driver = driver
        # driver.get(url_01)

    def visit(self):
        self.driver.get(url_01)

    def navigate_top(self):
        # копируем у всех элементов верхней навигации
        navtop_list = self.driver.find_elements(By.XPATH, "//a[@rel='nofollow']")
        # num_of_href = len(navtop_list)
        # print(num_of_href)
        return navtop_list

    def navigate_low_list(self):
        # копируем у всех элементов навигации (меню под поиском)
        navlow = self.driver.find_elements(By.XPATH, "//ul[@data-widget='horizontalMenu']/li")
        # navlow_list = self.driver.find_elements(By.CSS_SELECTOR, "li.rb")
        # num_of_href = len(navlow_list)
        # print(num_of_href)
        return navlow

    def navigate_low_elem(self, i):
        # копируем у всех элементов навигации (меню под поиском)
        navlow = self.driver.find_elements(By.XPATH, "//ul[@data-widget='horizontalMenu']/li")
        # navlow_list = self.driver.find_elements(By.CSS_SELECTOR, "li.rb")
        # num_of_href = len(navlow_list)
        # print(num_of_href)
        return navlow[i]

    def check_exist_by_xpath(self):
        try:
            self.driver.find_element(By.XPATH, "//h2[contains(text(), 'Произошла ошибка')]")
            # self.driver.find_element_by_xpath("//*[contains(text(), 'Магазины')]")
        except NoSuchElementException:
            return False
        return True

    # def get_shops(self):
    #     return self.driver.find_element_by_xpath("//*[contains(text(), 'Магазины')]")

    def visit_url(self, url):
        self.driver.get(url)

    def go_back(self):
        self.driver.back()