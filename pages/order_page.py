from pages.base_page import BasePage
from locators.order_page_locators import OrderPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class OrderPage(BasePage):

    @allure.step("Заполнить данные клиента")
    def fill_customer_data(self, name, surname, address, metro_station, phone):
        self.send_keys_to_element(OrderPageLocators.NAME_INPUT, name)
        self.send_keys_to_element(OrderPageLocators.SURNAME_INPUT, surname)
        self.send_keys_to_element(OrderPageLocators.ADDRESS_INPUT, address)
        self._select_metro(metro_station)
        self.send_keys_to_element(OrderPageLocators.PHONE_INPUT, phone)

    def _select_metro(self, station_name):
        metro_input = self.find_element(OrderPageLocators.METRO_INPUT)
        metro_input.click()
        metro_input.clear()
        metro_input.send_keys(station_name)

        WebDriverWait(self.driver, 5).until(
            EC.presence_of_all_elements_located(OrderPageLocators.METRO_OPTIONS)
        )

        option = self.find_element(OrderPageLocators.get_metro_option_by_text(station_name))
        option.click()

    @allure.step("Нажать 'Далее'")
    def click_next(self):
        self.click_element(OrderPageLocators.NEXT_BUTTON)

    @allure.step("Заполнить данные аренды")
    def fill_rental_data(self, date, rental_days, color, comment):
        self.send_keys_to_element(OrderPageLocators.DATE_INPUT, date)

        self.wait_for_element_visible(OrderPageLocators.RENTAL_SECTION)
        self.click_element(OrderPageLocators.RENTAL_SECTION)

        self._select_rental_period(rental_days)
        
        if color:
            self._select_color(color)
        
        if comment:
            self.send_keys_to_element(OrderPageLocators.COMMENT_INPUT, comment)

    def _select_rental_period(self, days):
        rental_periods = {
            1: "сутки",
            2: "двое суток",
            3: "трое суток",
            4: "четверо суток",
            5: "пятеро суток",
            6: "шестеро суток",
            7: "семеро суток"
        }

        dropdown = self.find_element(OrderPageLocators.RENTAL_PERIOD_DROPDOWN)
        self.scroll_to_element(OrderPageLocators.RENTAL_PERIOD_DROPDOWN)
        dropdown.click()

        option_text = rental_periods[days]
        option = self.find_element(OrderPageLocators.get_rental_period_option(option_text))
        option.click()

    def _select_color(self, color):
        color_locators = {
            "BLACK": OrderPageLocators.COLOR_BLACK,
            "GREY": OrderPageLocators.COLOR_GREY
        }
        self.click_element(color_locators[color])

    @allure.step("Нажать 'Заказать'")
    def click_order(self):
        self.click_element(OrderPageLocators.ORDER_BUTTON)

    @allure.step("Подтвердить заказ")
    def confirm_order(self):
        self.click_element(OrderPageLocators.CONFIRM_BUTTON)

    @allure.step("Проверить сообщение об успехе")
    def is_success_message_displayed(self):
        return self.is_element_visible(OrderPageLocators.SUCCESS_MODAL)

    @allure.step("Получить текст сообщения об успехе")
    def get_success_message(self):
        return self.get_text(OrderPageLocators.SUCCESS_MODAL)
    