from pages.base_page import BasePage
from locators.home_page_locators import HomePageLocators
import allure
from config import Config


class HomePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Открыть главную страницу")
    def open(self):
        self.open_url(Config.BASE_URL)
        self.accept_cookies()
        return self

    @allure.step("Нажать нижнюю кнопку 'Заказать'")
    def click_bottom_order_button(self):
        self.scroll_to_element(HomePageLocators.BOTTOM_ORDER_BUTTON)
        self.click_element(HomePageLocators.BOTTOM_ORDER_BUTTON)

    @allure.step("Нажать вопрос FAQ с индексом {index}")
    def click_faq_question(self, index):
        locator = HomePageLocators.get_faq_question_by_index(index)
        self.scroll_to_element(HomePageLocators.FAQ_SECTION)
        self.click_element(locator)

    @allure.step("Получить текст видимого ответа FAQ")
    def get_faq_answer_text(self):
        self.wait_for_element_visible(HomePageLocators.FAQ_VISIBLE_ANSWER)
        return self.get_text(HomePageLocators.FAQ_VISIBLE_ANSWER)

    @allure.step("Проверить, что ответ отображается")
    def is_faq_answer_displayed(self):
        return self.is_element_visible(HomePageLocators.FAQ_VISIBLE_ANSWER)
    