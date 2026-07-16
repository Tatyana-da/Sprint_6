import allure
import time
from pages.home_page import HomePage


@allure.epic("Яндекс.Самокат")
@allure.feature("Логотипы")
class TestLogo:

    @allure.story("Переход на главную страницу")
    def test_scooter_logo_redirect(self, driver):
        home_page = HomePage(driver).open()
        home_page.click_scooter_logo()
        assert driver.current_url == "https://qa-scooter.education-services.ru/"

    @allure.story("Переход на Дзен")
    def test_yandex_logo_redirect(self, driver):
        home_page = HomePage(driver).open()
        initial_windows = len(driver.window_handles)
        home_page.click_yandex_logo()
        time.sleep(3)

        assert len(driver.window_handles) > initial_windows, "Новое окно не открылось"

        driver.switch_to.window(driver.window_handles[-1])
        time.sleep(2)
        current_url = driver.current_url

        assert "dzen.ru" in current_url or "ya.ru" in current_url, \
            f"Неверный URL: {current_url}"
        