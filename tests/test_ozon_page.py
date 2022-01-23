import pytest
from selenium.webdriver.common.by import By
from pages.ozon_page import OzonPage
from pages.shops_page import ShopPage
from pages.topnav_page import TopNavPage
import time

@pytest.mark.skip
def test_visit(driver):
    # проверяем отображение вкладки Магазины
    page = OzonPage(driver)
    #
    page.visit()
    assert page.get_shops().is_displayed()
    time.sleep(2)

@pytest.mark.skip
def test_shops(driver):
    # проверяем переход к магазинам и отображение вкладки Книги
    page = OzonPage(driver)
    page.visit()
    page.get_shops().click()
    shop_page = ShopPage(driver)
    time.sleep(1)
    assert shop_page.get_shops()[1].is_displayed()
    time.sleep(2)

@pytest.mark.skip
def test_scroll(driver):
    # проверяем видимость подвижного меню после скрола
    page = OzonPage(driver)
    page.visit()
    # page.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    page.footer().click()
    driver.save_screenshot('result-00.png')
    page.scrolldown()
    driver.save_screenshot('result-01.png')
    # time.sleep(2)
    time.sleep(5)
    # scrolled_page = OzonPage(driver)
    # assert page.ontopmenu().is_displayed()
    assert page.footer().is_displayed()
    # time.sleep(5)

def test_topnav(driver):
    # проверяем налчие ссылки неподвижного меню верхней навигации
    num_ref = 0
    page = TopNavPage(driver)
    page.visit()
    # time.sleep(1)
    # navtoplist = page.navigate_top()
    for i in range(len(page.navigate_top())):
        if page.navigate_top()[i].get_attribute('href') != '':
            num_ref += 1
    assert len(page.navigate_top()) == num_ref

def test_topnav_01(driver):
    # проверяем работают ли ссылки неподвижного меню верхней навигации
    page = TopNavPage(driver)
    page.visit()
    nav_list = page.navigate_top()
    href_list = []
    for i in range(len(nav_list)):
        href_list.append(nav_list[i].get_attribute('href'))

    for i in range(len(href_list)):
        page.visit_url(href_list[i])
        assert page.check_exist_by_xpath() is False
        # проверяем что на странице из списка нет элемента с ошибкой

    # page.visit_url('https://www.ozon.ru/')
    # time.sleep(2)
    # assert page.check_exist_by_xpath() is False


def test_lownav(driver):
    # проверяем налчие ссылки неподвижного меню верхней навигации (меню под поиском)
    num_ref = 0
    page = TopNavPage(driver)
    page.visit()
    # time.sleep(1)
    # navtoplist = page.navigate_top()
    for i in range(len(page.navigate_low_list())):
        if page.navigate_low_list()[i].get_attribute('href') != '':
            num_ref += 1
    assert len(page.navigate_low_list()) == num_ref


def test_lownav_01(driver):
    # проверяем работают ли ссылки, открываются ли страницы при нажатии
    # в неподвижного меню верхней навигации (меню под поиском)
    page = TopNavPage(driver)
    page.visit()
    nav_list = page.navigate_low_list()
    # print(nav_list)
    for i in range(len(nav_list)):
        page.navigate_low_elem(i).click()
        time.sleep(3)
        page.visit()
        # возврат к странице