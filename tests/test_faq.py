import allure
from pages.home_page import HomePage


@allure.epic("Яндекс.Самокат")
@allure.feature("Вопросы о важном")
class TestFAQ:

    @allure.story("Проверка ответов")
    def test_faq_answers(self, driver, faq_data):
        question_index, expected = faq_data
        home_page = HomePage(driver).open()
        home_page.click_faq_question(question_index)
        assert home_page.is_faq_answer_displayed(), "Ответ не отображается"
        actual = home_page.get_faq_answer_text()
        assert actual == expected, f"Неверный ответ для вопроса {question_index + 1}"
        