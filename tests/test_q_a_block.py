from page_objects.base_page import BasePage
from page_objects.Q_A_block import LocatorQuestionsAboutImportant
from conftest import driver


class TestQABlock:
    def test_1_question(self, driver):
        base_page = BasePage(driver)
        base_page.go_to_site('https://qa-scooter.praktikum-services.ru/')
        base_page.scroll_to_qa_block()
        base_page.find_element_located(LocatorQuestionsAboutImportant.FIRST_QUESTION).click()
        first_answer = base_page.find_element_located(LocatorQuestionsAboutImportant.FIRST_ANSWER).text
        assert first_answer == 'Сутки — 400 рублей. Оплата курьеру — наличными или картой.'

    def test_2_question(self, driver):
        base_page = BasePage(driver)
        base_page.go_to_site('https://qa-scooter.praktikum-services.ru/')
        base_page.scroll_to_qa_block()
        base_page.find_element_located(LocatorQuestionsAboutImportant.SECOND_QUESTION).click()
        first_answer = base_page.find_element_located(LocatorQuestionsAboutImportant.SECOND_ANSWER).text
        assert first_answer == ('Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, '
                                'можете просто сделать несколько заказов — один за другим.')

    def test_3_question(self, driver):
        base_page = BasePage(driver)
        base_page.go_to_site('https://qa-scooter.praktikum-services.ru/')
        base_page.scroll_to_qa_block()
        base_page.find_element_located(LocatorQuestionsAboutImportant.THIRD_QUESTION).click()
        first_answer = base_page.find_element_located(LocatorQuestionsAboutImportant.THIRD_ANSWER).text
        assert first_answer == ('Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. '
                                'Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы '
                                'привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.')

    def test_4_question(self, driver):
        base_page = BasePage(driver)
        base_page.go_to_site('https://qa-scooter.praktikum-services.ru/')
        base_page.scroll_to_qa_block()
        base_page.find_element_located(LocatorQuestionsAboutImportant.FOURTH_QUESTION).click()
        first_answer = base_page.find_element_located(LocatorQuestionsAboutImportant.FOURTH_ANSWER).text
        assert first_answer == 'Только начиная с завтрашнего дня. Но скоро станем расторопнее.'

    def test_5_question(self, driver):
        base_page = BasePage(driver)
        base_page.go_to_site('https://qa-scooter.praktikum-services.ru/')
        base_page.scroll_to_qa_block()
        base_page.find_element_located(LocatorQuestionsAboutImportant.FIFTH_QUESTION).click()
        first_answer = base_page.find_element_located(LocatorQuestionsAboutImportant.FIFTH_ANSWER).text
        assert first_answer == ('Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по '
                                'красивому номеру 1010.')

    def test_6_question(self, driver):
        base_page = BasePage(driver)
        base_page.go_to_site('https://qa-scooter.praktikum-services.ru/')
        base_page.scroll_to_qa_block()
        base_page.find_element_located(LocatorQuestionsAboutImportant.SIXTH_QUESTION).click()
        first_answer = base_page.find_element_located(LocatorQuestionsAboutImportant.SIXTH_ANSWER).text
        assert first_answer == ('Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если '
                                'будете кататься без передышек и во сне. Зарядка не понадобится.')

    def test_7_question(self, driver):
        base_page = BasePage(driver)
        base_page.go_to_site('https://qa-scooter.praktikum-services.ru/')
        base_page.scroll_to_qa_block()
        base_page.find_element_located(LocatorQuestionsAboutImportant.SEVENTH_QUESTION).click()
        first_answer = base_page.find_element_located(LocatorQuestionsAboutImportant.SEVENTH_ANSWER).text
        assert first_answer == ('Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не '
                                'попросим. Все же свои.')

    def test_8_question(self, driver):
        base_page = BasePage(driver)
        base_page.go_to_site('https://qa-scooter.praktikum-services.ru/')
        base_page.scroll_to_qa_block()
        base_page.find_element_located(LocatorQuestionsAboutImportant.EIGHTH_QUESTION).click()
        first_answer = base_page.find_element_located(LocatorQuestionsAboutImportant.EIGHTH_ANSWER).text
        assert first_answer == 'Да, обязательно. Всем самокатов! И Москве, и Московской области.'
