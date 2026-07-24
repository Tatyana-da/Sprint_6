from selenium.webdriver.common.by import By


class BasePageLocators:
    """Общие локаторы для всех страниц"""

    YANDEX_LOGO = (By.CSS_SELECTOR, ".Header_LogoYandex__3TSOI")
    SCOOTER_LOGO = (By.CSS_SELECTOR, ".Header_LogoScooter__3lsAR")
    HEADER_ORDER_BUTTON = (By.XPATH, "//div[@class='Header_Nav__AGCXC']//button[contains(text(),'Заказать')]")
    ORDER_STATUS_INPUT = (By.CSS_SELECTOR, ".Header_SearchInput__3YRIQ input")
    ORDER_STATUS_GO_BUTTON = (By.CSS_SELECTOR, ".Header_SearchInput__3YRIQ .Header_Button__28dPO")
    COOKIE_BUTTON = (By.ID, "rcc-confirm-button")
    