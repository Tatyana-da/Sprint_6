from selenium.webdriver.common.by import By


class OrderPageLocators:
    """Локаторы страницы оформления заказа"""

    # Шаг 1 - Данные клиента
    NAME_INPUT = (By.XPATH, "//input[@placeholder='* Имя']")
    SURNAME_INPUT = (By.XPATH, "//input[@placeholder='* Фамилия']")
    ADDRESS_INPUT = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    METRO_INPUT = (By.XPATH, "//input[@placeholder='* Станция метро']")
    PHONE_INPUT = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    NEXT_BUTTON = (By.XPATH, "//button[contains(text(),'Далее')]")

    # Шаг 2 - Данные аренды
    DATE_INPUT = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    RENTAL_PERIOD_DROPDOWN = (By.CLASS_NAME, "Dropdown-control")

    @staticmethod
    def get_rental_period_option(text):
        return (By.XPATH, f"//div[contains(@class, 'Dropdown-option') and text()='{text}']")

    # Цвета самоката
    COLOR_BLACK = (By.ID, "black")
    COLOR_GREY = (By.ID, "grey")
    
    COMMENT_INPUT = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")
    ORDER_BUTTON = (By.XPATH, "//div[@class='Order_Buttons__1xGrp']//button[contains(text(),'Заказать')]")

    # Модальные окна
    CONFIRM_BUTTON = (By.XPATH, "//button[contains(text(),'Да')]")
    SUCCESS_MODAL = (By.XPATH, "//div[contains(@class, 'Order_ModalHeader')]")

    # Метро опции
    METRO_OPTIONS = (By.XPATH, "//button[contains(@class, 'select-search__option')]")

    @staticmethod
    def get_metro_option_by_text(station_name):
        return (By.XPATH, f"//button[contains(@class, 'select-search__option') and contains(., '{station_name}')]")
    