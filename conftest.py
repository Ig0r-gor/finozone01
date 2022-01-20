import pytest
from selenium import webdriver

@pytest.fixture(scope="mainfunction")
def driver(request):
    path = str(request.fspath)
    driver = webdriver.Chrome(f"{path[:path.find('page_object')]}page_object/chromedriver")
    driver.maximize_window()
    driver.implicitly_wait(5)
    yield driver