from pages.ozon_page import OzonPage
from selenium.webdriver.common.by import By
from config import url_actions


class ActionPage(OzonPage):

    def __init__(self, driver):
        super().__init__(driver)

        page = OzonPage(driver)
        page.gotourl(url_actions)

    def allactions(self):
        return self.driver.find_elements(By.XPATH, '//div[@data-widget="actionCategory"]//span')

    def nextact(self):
        return self.driver.find_element(By.XPATH, '//button[@aria-label="Next slide"]/..')

