import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from pages.home_page import HomePage
from pages.order_page import OrderPage
from helpers import generate_order_data
from data.faq_data import FAQ_DATA


@pytest.fixture(scope="function")
def driver():
    options = Options()
    service = Service(r"C:\Users\gorin\Desktop\Проект_Яндекс.Практикум\Sprint_6\geckodriver.exe")
    driver = webdriver.Firefox(service=service, options=options)
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture(scope="function")
def home_page(driver):
    return HomePage(driver)


@pytest.fixture(scope="function")
def order_page(driver):
    return OrderPage(driver)


@pytest.fixture(scope="function")
def order_data_1():
    return generate_order_data()


@pytest.fixture(scope="function")
def order_data_2():
    return generate_order_data()


@pytest.fixture(scope="function")
def order_data_3():
    data = generate_order_data()
    data["rental"]["color"] = ""
    data["rental"]["comment"] = ""
    return data


@pytest.fixture(params=FAQ_DATA)
def faq_data(request):
    return request.param
