import pytest
from selenium import webdriver
import time

@pytest.fixture(scope="function")
def driver(request):
    path = str(request.fspath)
    # print(request.fspath)
    # print(f"{path[:path.find('tests')]}\chromedriver")
    # time.sleep(5)
    driver = webdriver.Chrome(f"{path[:path.find('tests')]}chromedriver")
    driver.maximize_window()
    driver.implicitly_wait(5)
    yield driver
    driver.close()
