from pages.base_page import BasePage
from locators.order_status_page_locators import OrderStatusPageLocators
import allure


class OrderStatusPage(BasePage):

    @allure.step("Проверить статус по номеру")
    def check_order_status(self, order_number):
        self.send_keys_to_element(OrderStatusPageLocators.ORDER_NUMBER_INPUT, order_number)
        self.click_element(OrderStatusPageLocators.GO_BUTTON)

    @allure.step("Получить текст статуса")
    def get_status_text(self):
        return self.get_text(OrderStatusPageLocators.STATUS_INFO)
    