from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import allure
from locators.base_page_locators import BasePageLocators


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    @allure.step("Найти элемент")
    def find_element(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(locator)
        )

    @allure.step("Найти все элементы")
    def find_elements(self, locator, timeout=10):
        WebDriverWait(self.driver, timeout).until(
            EC.presence_of_all_elements_located(locator)
        )
        return self.driver.find_elements(*locator)

    @allure.step("Кликнуть по элементу")
    def click_element(self, locator, timeout=10):
        element = WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator)
        )
        element.click()

    @allure.step("Ввести текст")
    def send_keys_to_element(self, locator, text, timeout=10):
        element = self.find_element(locator, timeout)
        element.clear()
        element.send_keys(text)

    @allure.step("Получить текст")
    def get_text(self, locator, timeout=10):
        return self.find_element(locator, timeout).text

    @allure.step("Прокрутить до элемента")
    def scroll_to_element(self, locator):
        element = self.find_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

    @allure.step("Проверить видимость")
    def is_element_visible(self, locator, timeout=5):
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator)
            )
            return True
        except TimeoutException:
            return False

    @allure.step("Проверить наличие элемента")
    def is_element_present(self, locator, timeout=3):
        try:
            self.find_element(locator, timeout)
            return True
        except TimeoutException:
            return False

    @allure.step("Получить текущий URL")
    def get_current_url(self):
        return self.driver.current_url

    @allure.step("Переключиться на новое окно")
    def switch_to_new_window(self):
        self.driver.switch_to.window(self.driver.window_handles[-1])

    @allure.step("Получить количество окон")
    def get_window_handles_count(self):
        return len(self.driver.window_handles)

    @allure.step("Открыть URL")
    def open_url(self, url):
        self.driver.get(url)

    @allure.step("Нажать логотип Яндекса")
    def click_yandex_logo(self):
        self.click_element(BasePageLocators.YANDEX_LOGO)

    @allure.step("Нажать логотип Самоката")
    def click_scooter_logo(self):
        self.click_element(BasePageLocators.SCOOTER_LOGO)

    @allure.step("Нажать верхнюю кнопку 'Заказать'")
    def click_header_order_button(self):
        self.click_element(BasePageLocators.HEADER_ORDER_BUTTON)

    @allure.step("Принять куки")
    def accept_cookies(self):
        if self.is_element_present(BasePageLocators.COOKIE_BUTTON):
            self.click_element(BasePageLocators.COOKIE_BUTTON)

    @allure.step("Ожидать видимость элемента")
    def wait_for_element_visible(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )

    @allure.step("Ожидать, что элемент станет кликабельным")
    def wait_for_element_clickable(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator)
        )
    