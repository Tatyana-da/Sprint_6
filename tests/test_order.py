import pytest
import allure
from pages.home_page import HomePage
from pages.order_page import OrderPage
from config import Config


@allure.epic("Яндекс.Самокат")
@allure.feature("Оформление заказа")
class TestOrder:

    @allure.story("Позитивный сценарий с данными 1 - через header")
    def test_positive_order_flow_header(self, home_page, order_page, order_data_1):
        home_page.open()
        home_page.click_header_order_button()
        self._fill_order(order_page, order_data_1)

    @allure.story("Позитивный сценарий с данными 2 - через bottom")
    def test_positive_order_flow_bottom(self, home_page, order_page, order_data_2):
        home_page.open()
        home_page.click_bottom_order_button()
        self._fill_order(order_page, order_data_2)

    @allure.story("Позитивный сценарий с данными 3 - через bottom без цвета и комментария")
    def test_positive_order_flow_without_color_and_comment(self, home_page, order_page, order_data_3):
        home_page.open()
        home_page.click_bottom_order_button()
        self._fill_order(order_page, order_data_3)

    def _fill_order(self, order_page, order_data):
        order_page.fill_customer_data(**order_data["customer"])
        order_page.click_next()
        order_page.fill_rental_data(**order_data["rental"])
        order_page.click_order()
        order_page.confirm_order()

        assert order_page.is_success_message_displayed(), "Сообщение об успехе не появилось"

        success_text = order_page.get_success_message()
        assert "Заказ оформлен" in success_text, f"Неверное сообщение: {success_text}"

        allure.attach(
            f"Клиент: {order_data['customer']}\n"
            f"Аренда: {order_data['rental']}",
            name="Тестовые данные",
            attachment_type=allure.attachment_type.TEXT
        )
        