from pages.ozon_page import OzonPage
from selenium.webdriver.common.by import By
from config import url_shop


class ShopPage(OzonPage):

    def __init__(self, driver):
        super().__init__(driver)

        page = OzonPage(driver)
        page.gotourl(url_shop)


    def allshops(self):
        return self.driver.find_elements(By.XPATH, '//div[@data-widget="sellerCategory"]//a')


    def nextlist(self):
        return self.driver.find_element(By.XPATH, '//div[@data-widget="sellerCategory"]/div[4]')

