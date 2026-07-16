import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
import random
from datetime import datetime, timedelta


@pytest.fixture(scope="function")
def driver():
    """Фикстура для создания драйвера Firefox"""
    options = Options()
    service = Service(r"C:\Users\gorin\Desktop\Проект_Яндекс.Практикум\Sprint_6\geckodriver.exe")
    driver = webdriver.Firefox(service=service, options=options)
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture(scope="function")
def order_data():
    """Генерация уникальных данных для заказа."""
    metro_stations = [
        "Сокольники",
        "Преображенская площадь",
        "Черкизовская",
        "Бульвар Рокоссовского",
        "Локомотив",
        "Измайловская"
    ]

    return {
        "customer": {
            "name": random.choice(["Иван", "Мария", "Алексей", "Екатерина", "Дмитрий", "Анна"]),
            "surname": random.choice(["Петров", "Иванова", "Смирнов", "Козлова", "Соколов", "Михайлова"]),
            "address": f"{random.choice(['ул. Тверская', 'пр. Мира', 'ул. Арбат', 'ул. Ленина', 'ул. Пушкина'])}, д. {random.randint(1, 100)}",
            "metro_station": random.choice(metro_stations),
            "phone": f"+7{random.randint(900, 999)}{random.randint(1000000, 9999999)}"
        },
        "rental": {
            "date": (datetime.now() + timedelta(days=random.randint(1, 30))).strftime("%d.%m.%Y"),
            "rental_days": random.randint(1, 7),
            "color": random.choice(["BLACK", "GREY"]),
            "comment": random.choice(["Позвонить за час", "Без комментариев", "Домофон 123", "Оставить у двери"])
        },
        "button_position": random.choice(["header", "bottom"])
    }


@pytest.fixture(params=[
    (0, "Сутки — 400 рублей. Оплата курьеру — наличными или картой."),
    (1, "Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим."),
    (2, "Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30."),
    (3, "Только начиная с завтрашнего дня. Но скоро станем расторопнее."),
    (4, "Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010."),
    (5, "Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится."),
    (6, "Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои."),
    (7, "Да, обязательно. Всем самокатов! И Москве, и Московской области.")
])
def faq_data(request):
    return request.param
