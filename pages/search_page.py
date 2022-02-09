import time

from pages.ozon_page import OzonPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
# from config import url_shop


class SearchPage(OzonPage):

    def __init__(self, driver):
        super().__init__(driver)



    # def input_field(self):        #перенесено в OzonPage
    #     return self.driver.find_element(By.NAME, 'text')
    #
    # def search_btn(self):
    #     return self.driver.find_element(By.XPATH, '//form/button')

    def search_res(self):
        s = []
        search_res = self.driver.find_elements(By.CSS_SELECTOR, 'a span.f-tsBodyL span')

        for i in range(len(search_res)):
            s.append(search_res[i].text)
        return s

    def select_lowcost(self):
        sel = Select(self.driver.find_element(By.XPATH, '//div[@role="listbox"]'))
        time.sleep(3)
        # sel = self.driver.find_element(By.XPATH, '//div[@role="listbox"]')
        sel.select_by_visible_text('Сначала дешёвые')
        time.sleep(3)
        return sel


    # catalog_btn = self.driver.find_element(By.XPATH, '//div[@data-widget="catalogMenu"]')
    # favor_btn = self.driver.find_element(By.XPATH, '//a[@data-widget="favoriteCounter"]')
    # favor_btn2 = self.driver.find_element(By.XPATH, '//a[@href="/my/favorites"]')
    # basket_btn = self.driver.find_element(By.XPATH, '//a[@href="/cart"]')
