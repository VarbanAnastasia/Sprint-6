import allure
import pytest

from page_objects.q_a_block import LocatorQuestionsAboutImportant, QuestionsPage
from conftest import driver


list_questions = [[LocatorQuestionsAboutImportant.FIRST_QUESTION, LocatorQuestionsAboutImportant.FIRST_ANSWER,
                   'Сутки — 400 рублей. Оплата курьеру — наличными или картой.'],
                  [LocatorQuestionsAboutImportant.SECOND_QUESTION, LocatorQuestionsAboutImportant.SECOND_ANSWER,
                   'Пока что у нас так: один заказ — один самокат. '
                   'Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.'],
                  [LocatorQuestionsAboutImportant.THIRD_QUESTION, LocatorQuestionsAboutImportant.THIRD_ANSWER,
                   'Допустим, вы оформляете заказ на 8 мая. '
                   'Мы привозим самокат 8 мая в течение дня. '
                   'Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. '
                   'Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.'],
                  [LocatorQuestionsAboutImportant.FOURTH_QUESTION, LocatorQuestionsAboutImportant.FOURTH_ANSWER,
                   'Только начиная с завтрашнего дня. Но скоро станем расторопнее.'],
                  [LocatorQuestionsAboutImportant.FIFTH_QUESTION, LocatorQuestionsAboutImportant.FIFTH_ANSWER,
                   'Пока что нет! ''Но если что-то срочное — всегда можно позвонить '
                   'в поддержку по красивому номеру 1010.'],
                  [LocatorQuestionsAboutImportant.SIXTH_QUESTION, LocatorQuestionsAboutImportant.SIXTH_ANSWER,
                   'Самокат приезжает к вам с полной зарядкой. '
                   'Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. '
                   'Зарядка не понадобится.'],
                  [LocatorQuestionsAboutImportant.SEVENTH_QUESTION, LocatorQuestionsAboutImportant.SEVENTH_ANSWER,
                   'Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. '
                   'Все же свои.'],
                  [LocatorQuestionsAboutImportant.EIGHTH_QUESTION, LocatorQuestionsAboutImportant.EIGHTH_ANSWER,
                   'Да, обязательно. Всем самокатов! И Москве, и Московской области.']]


@pytest.mark.parametrize('question_locator,question_text_locator, text', list_questions)
@allure.title('Анализ текста после клика по вопросу')
class TestQABlock:
    def test_questions(self, driver, question_locator, question_text_locator, text):
        questions_page = QuestionsPage(driver)
        questions_page.go_to_site('https://qa-scooter.praktikum-services.ru/')
        questions_page.scroll_to_qa_block(question_locator)
        correct_text = questions_page.check_the_questions(question_locator, question_text_locator)
        assert correct_text == text

