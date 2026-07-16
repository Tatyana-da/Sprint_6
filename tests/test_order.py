import pytest
import allure
import time
from pages.home_page import HomePage
from pages.order_page import OrderPage


@allure.epic("Яндекс.Самокат")
@allure.feature("Оформление заказа")
class TestOrder:

    @allure.story("Позитивный сценарий с разными данными")
    @pytest.mark.parametrize("customer_data, rental_data, button_position", [
        # Набор данных 1: полный заказ, черный цвет, комментарий
        (
            {
                "name": "Иван",
                "surname": "Петров",
                "address": "ул. Тверская, д. 15",
                "metro_station": "Сокольники",
                "phone": "+79001234567"
            },
            {
                "date": "15.07.2026",
                "rental_days": 2,
                "color": "BLACK",
                "comment": "Позвонить за час"
            },
            "header"
        ),
        # Набор данных 2: полный заказ, серый цвет, без комментария
        (
            {
                "name": "Мария",
                "surname": "Иванова",
                "address": "пр. Мира, д. 25",
                "metro_station": "Преображенская площадь",
                "phone": "+79007654321"
            },
            {
                "date": "16.07.2026",
                "rental_days": 3,
                "color": "GREY",
                "comment": ""
            },
            "bottom"
        ),
        # Набор данных 3: заказ без выбора цвета и без комментария
        (
            {
                "name": "Алексей",
                "surname": "Смирнов",
                "address": "ул. Арбат, д. 10",
                "metro_station": "Черкизовская",
                "phone": "+79009998877"
            },
            {
                "date": "17.07.2026",
                "rental_days": 1,
                "color": "",
                "comment": ""
            },
            "bottom"
        )
    ])
    def test_positive_order_flow(self, driver, customer_data, rental_data, button_position):
        home_page = HomePage(driver).open()

        if button_position == "header":
            home_page.click_header_order_button()
        else:
            home_page.click_bottom_order_button()

        time.sleep(1)

        order_page = OrderPage(driver)
        order_page.fill_customer_data(**customer_data)
        order_page.click_next()

        time.sleep(1)

        order_page.fill_rental_data(**rental_data)
        order_page.click_order()
        time.sleep(0.5)
        order_page.confirm_order()

        assert order_page.is_success_message_displayed(), "Сообщение об успехе не появилось"

        success_text = order_page.get_success_message()
        assert "Заказ оформлен" in success_text or "Создан" in success_text, \
            f"Неверное сообщение: {success_text}"

        allure.attach(
            f"Клиент: {customer_data}\n"
            f"Аренда: {rental_data}\n"
            f"Кнопка: {button_position}",
            name="Тестовые данные",
            attachment_type=allure.attachment_type.TEXT
        )
        