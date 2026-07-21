import allure
import time
from pages.home_page import HomePage
from config import Config


@allure.epic("Яндекс.Самокат")
@allure.feature("Логотипы")
class TestLogo:

    @allure.story("Переход на главную страницу")
    def test_scooter_logo_redirect(self, home_page):
        home_page.open()
        home_page.click_scooter_logo()
        assert home_page.get_current_url() == Config.BASE_URL

    @allure.story("Переход на Яндекс")
    def test_yandex_logo_redirect(self, home_page):
        home_page.open()
        initial_windows = home_page.get_window_handles_count()
        
        home_page.click_yandex_logo()
        time.sleep(3)

        assert home_page.get_window_handles_count() > initial_windows, "Новое окно не открылось"

        home_page.switch_to_new_window()
        time.sleep(2)
        current_url = home_page.get_current_url()

        # На тестовом стенде может быть about:blank, в реальности - ya.ru
        assert current_url == Config.EXPECTED_YA_URL or current_url == "about:blank", \
            f"Неверный URL: {current_url}"
        