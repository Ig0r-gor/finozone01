from config import url_01

class ShopPage():

    def __init__(self, driver):
        self.driver = driver

    def get_shops(self):
        return self.driver.find_elements_by_xpath("//*[contains(text(), 'Книги')]")