import time

from pages.ozon_page import OzonPage
from selenium.webdriver.common.by import By


class CatlgPage(OzonPage):

    def __init__(self, driver):
        super().__init__(driver)


    def ctlg_btn(self):
        # нажать на каталог
        return self.driver.find_element(By.XPATH, '//div[@data-widget="catalogMenu"]')

    def tvivt_chap(self):
        # раздел Телевизоры и видеотехника
        return self.driver.find_element(By.XPATH, '//a[@href="/category/televizory-i-videotehnika-15527/"]')

    def cloth_ctlg(self):
        # строка каталога Одежда
        return self.driver.find_element(By.XPATH, '//a[@href="/category/odezhda-obuv-i-aksessuary-7500/"]')

    def ban_plates(self):
        # баннеры-плитки
        return self.driver.find_elements(By.XPATH, '//div[@data-widget="objectBannerList"]//img')

    def shoes_ctlg(self):
        # строка каталога Обувь
        return self.driver.find_element(By.XPATH, '//a[@href="/category/obuv-17777/"]')

    def sport_ctlg(self):
        # строка каталога Спорт и отдых
        return self.driver.find_element(By.XPATH, '//a[@href="/category/sport-i-otdyh-11000/"]')

    def ban_lineplates(self):
        # линейный баннер-плитки
        return self.driver.find_elements(By.XPATH, '//div[@data-widget="objectLine"]//img')