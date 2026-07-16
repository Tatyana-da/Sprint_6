from selenium.webdriver.common.by import By


class HomePageLocators:

    BOTTOM_ORDER_BUTTON = (By.XPATH, "//div[@class='Home_FinishButton__1_cWm']//button")
    FAQ_SECTION = (By.CSS_SELECTOR, ".Home_FourPart__1uthg")
    FAQ_VISIBLE_ANSWER = (By.XPATH, "//div[@data-accordion-component='AccordionItemPanel' and not(@hidden)]//p")

    @staticmethod
    def get_faq_question_by_index(index):
        return (By.XPATH, f"(//div[@data-accordion-component='AccordionItem']//div[@role='button' and contains(@class, 'accordion__button')])[{index + 1}]")
    