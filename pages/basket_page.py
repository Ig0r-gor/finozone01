import time

from pages.ozon_page import OzonPage
from selenium.webdriver.common.by import By


class BasketPage(OzonPage):

    def __init__(self, driver):
        super().__init__(driver)


    def basket_btn(self):
        return self.driver.find_element(By.XPATH, '//a[@href="/cart"]')

    def tobask_btn01(self):
        # кнопки в корзину
        return self.driver.find_elements(By.XPATH,
                                        '//div[@data-widget="searchResultsV2"]//*[contains(text(), "В корзину")]')

    def formalize_btn(self):
        # кнопка к оформлению в корзине
        return self.driver.find_element(By.XPATH, '//div[@text="Перейти к оформлению"]/button')
        # возвращаем первый элемент-кнопку из найденных

    def alert_modal_01(self):
        # закрыть модалку
        btn = self.driver.find_elements(By.XPATH, '//div[@data-widget="alertPopup"]//button')
        btn[1].click()