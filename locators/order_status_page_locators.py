from selenium.webdriver.common.by import By


class OrderStatusPageLocators:
    """Локаторы страницы статуса заказа"""

    ORDER_NUMBER_INPUT = (By.XPATH, "//input[@placeholder='Введите номер заказа']")
    GO_BUTTON = (By.XPATH, "//button[contains(text(),'Go!')]")
    STATUS_INFO = (By.CSS_SELECTOR, ".Order_StatusInfo__2ilDt")
    