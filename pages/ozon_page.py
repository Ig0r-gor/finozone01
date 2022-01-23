from config import  url_01
# from selenium.webdriver.common.keys import Keys
# import time, os

class OzonPage():

    def __init__(self, driver):
        self.driver = driver
        # driver.get(url_01)

    def visit(self):
        self.driver.get(url_01)

    def get_shops(self):
        return self.driver.find_element_by_xpath("//*[contains(text(), 'Магазины')]")

    def ontopmenu(self):
        return self.driver.find_element_by_id('stickyHeader')

    def scrolldown(self):
        # html = self.driver.find_element_by_tag_name('html')

        # print(html.send_keys(Keys.END))
        # print(end_point)
        return self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight * 100);")
        # return self.driver.execute_script("window.scrollTo(0, end_point);")

    def footer(self):
        return self.driver.find_element_by_tag_name('footer')