from pages.base_page import BasePage
from locators.order_page_locators import OrderPageLocators
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure
import time


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
        time.sleep(0.5)
        metro_input.clear()
        metro_input.send_keys(station_name)
        time.sleep(1)

        WebDriverWait(self.driver, 5).until(
            EC.presence_of_all_elements_located((By.XPATH, "//button[contains(@class, 'select-search__option')]"))
        )

        option = self.driver.find_element(By.XPATH, f"//button[contains(@class, 'select-search__option') and contains(., '{station_name}')]")
        option.click()
        time.sleep(0.5)

    @allure.step("Нажать 'Далее'")
    def click_next(self):
        self.click_element(OrderPageLocators.NEXT_BUTTON)

    @allure.step("Заполнить данные аренды")
    def fill_rental_data(self, date, rental_days, color, comment):
        self.send_keys_to_element(OrderPageLocators.DATE_INPUT, date)
        time.sleep(0.5)

        self.driver.find_element(By.XPATH, "//div[contains(text(),'Про аренду')]").click()
        time.sleep(0.5)

        self._select_rental_period(rental_days)
        
        # Выбор цвета только если он указан
        if color:
            self._select_color(color)
        
        # Ввод комментария только если он указан
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
        self.driver.execute_script("arguments[0].scrollIntoView(true);", dropdown)
        time.sleep(0.3)
        dropdown.click()
        time.sleep(0.5)

        option_text = rental_periods[days]
        option = self.driver.find_element(By.XPATH, f"//div[contains(@class, 'Dropdown-option') and text()='{option_text}']")
        option.click()
        time.sleep(0.3)

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
    