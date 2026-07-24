import allure
from selenium.webdriver.support.ui import WebDriverWait
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
        
        WebDriverWait(home_page.driver, 10).until(
            lambda driver: len(driver.window_handles) > initial_windows
        )
        
        assert home_page.get_window_handles_count() > initial_windows, "Новое окно не открылось"
        