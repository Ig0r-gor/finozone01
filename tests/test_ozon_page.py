import pytest
from selenium.common.exceptions import ElementNotInteractableException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from pages.ozon_page import OzonPage
from pages.shops_page import ShopPage
from pages.topnav_page import TopNavPage
from pages.actions import ActionPage
from pages.search_page import SearchPage
from pages.catalog_page import CatlgPage
from pages.basket_page import BasketPage
import time

@pytest.mark.skip
def test_visit(driver):
    # проверяем отображение вкладки Магазины
    page = OzonPage(driver)
    #
    page.visit()
    assert page.get_shops().is_displayed()
    time.sleep(2)

# @pytest.mark.skip
# def test_shops(driver):
#     # проверяем переход к магазинам и отображение вкладки Книги
#     page = OzonPage(driver)
#     page.visit()
#     page.get_shops().click()
#     shop_page = ShopPage(driver)
#     time.sleep(1)
#     assert shop_page.get_shops()[1].is_displayed()
#     time.sleep(2)

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
    # print("start  ---  " * 10)
    nav_list = page.navigate_low_list()
    # print(len(nav_list))
    for i in range(len(nav_list)):
        page.navigate_low_elem(i).click()
        page.visit()
        # возврат к странице


def test_allshopclick(driver):
    # проверяем нажатие ссылок всех магазинов
    page = ShopPage(driver)
    shops_list = page.allshops()
    for i in range(len(shops_list)):
        try:
            page.allshops()[i].click()
            time.sleep(0.3)
        except ElementNotInteractableException:
            page.nextlist().click()


def test_actionsclick(driver):
    # проверяем нажатие ссылок всех магазинов
    page = ActionPage(driver)
    # actions_list = page.allactions()
    for i in range(11):
        page.allactions()[i].click()

    page.nextact().click()

    for i in range(11, 21):
        page.allactions()[i].click()
        # time.sleep(0.3)

    page.nextact().click()

    for i in range(21, 25):
        page.allactions()[i].click()
        # time.sleep(0.3)

    page.nextact().click()

    for i in range(25, 33):
        page.allactions()[i].click()
        # time.sleep(0.3)

def test_search_01(driver):
    # проверка ниличи поля поиска и кнопки
    page = SearchPage(driver)
    page.visit()
    assert page.input_field().is_displayed(), 'поле поиска не отображается'
    assert page.search_btn().is_displayed(), 'кнопка поиска не отображается'


def test_search_02(driver):
    # проверка ввода в поле поиска и сравнение результатов
    page = SearchPage(driver)
    page.visit()
    page.input_field().send_keys("самсунг")

    page.search_btn().click()
    s_list = page.search_res()
    for i in range(len(s_list)):
        # print(s_list[i])
        assert s_list[i].find('Samsung') != -1, 'В результатах поиска нет запрашиваемого слова'
        # проверяем что в найденных значениях есть английское наименование указанной на русском марки

def test_search_03(driver):
    # проверка ввода в поле поиска и сравнение результатов
    page = SearchPage(driver)
    page.visit()
    page.input_field().send_keys("gsktcjc")

    page.search_btn().click()
    time.sleep(5)
    s_list = page.search_res()
    # time.sleep(5)
    for i in range(len(s_list)):
        # print(' ---- ' * 5)
        # print(s_list[i])
        assert s_list[i].lower().find('пылесос') != -1, 'В результатах поиска нет запрашиваемого слова'
        # проверяем что в найденных значениях есть правильное наименование набранное в другой раскладке

@pytest.mark.skip
def test_search_04(driver):
    # проверка сортировки результатов поиска
    # НЕ РАБОТАЕТ!!!
    page = SearchPage(driver)
    page.visit()
    page.input_field().send_keys("телевизор смарт тв")
    page.search_btn().click()
    time.sleep(3)
    page.select_lowcost().click()

def test_ctlg_01(driver):
    # проверка результатов c открытием каталога
    page = CatlgPage(driver)
    page.visit()
    page.input_field().send_keys("телевизор смарт тв")
    page.ctlg_btn().click()
    assert page.tvivt_chap().is_displayed(), 'не отображается категория Электроника после введенного запроса'

def test_ctlg_02(driver):
    # проверка результата открытия раздела каталога Одежда
    page = CatlgPage(driver)
    page.visit()
    page.ctlg_btn().click()
    page.cloth_ctlg().click()
    time.sleep(5)
    plates = page.ban_plates()
    for i in range(len(plates)):
        assert plates[i].get_attribute('src') != '', 'отсутствует картинка в плитке Одежда'

def test_ctlg_03(driver):
    # проверка результата открытия раздела каталога Обувь
    page = CatlgPage(driver)
    page.visit()
    page.ctlg_btn().click()
    page.shoes_ctlg().click()
    # time.sleep(5)
    plates = page.ban_plates()
    for i in range(len(plates)):
        assert plates[i].get_attribute('src') != '', 'отсутствует картинка в плитке Обувь'


def test_ctlg_04(driver):
    # проверка результата открытия раздела каталога Спорт и отдых
    page = CatlgPage(driver)
    page.visit()
    page.ctlg_btn().click()
    page.sport_ctlg().click()
    # time.sleep(5)
    plates = page.ban_plates()
    line_plates = page.ban_lineplates()
    for i in range(len(plates)):
        assert plates[i].get_attribute('src') != '', 'отсутствует картинка в плитке Спорт'
    for i in range(len(line_plates)):
        assert line_plates[i].get_attribute('src') != '', 'отсутствует картинка в Линейной плитке Спорт'


def test_basket_01(driver):
    # проверка отображения кoрзины
    page = BasketPage(driver)
    page.visit()
    assert page.basket_btn().is_displayed(), 'не отображается значок Корзина'


def test_basket_02(driver):
    # проверка отображения в кoрзине, переход к оформлению

    page = BasketPage(driver)
    page.visit()
    page.input_field().send_keys("смартфон motorola")
    # time.sleep(3)
    page.search_btn().click()
    page.tobask_btn01()[0].click()
    # time.sleep(3)
    page.basket_btn().click()
    # time.sleep(3)

    page.alert_modal_01()
    # time.sleep(3)
    assert page.formalize_btn().is_displayed(), 'Не отображается кнопка Перейти к оформлению'
    page.formalize_btn().click()
    # time.sleep(3)

