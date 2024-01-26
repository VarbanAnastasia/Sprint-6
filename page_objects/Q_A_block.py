# класс для локаторов на странице Вопросы о важном
from selenium.webdriver.common.by import By


class LocatorQuestionsAboutImportant:
    # локатор до блока Вопрос-ответ
    QA_BLOCK = [By.CSS_SELECTOR, "[class*='accordion'][data-accordion-component='Accordion']"]
    # локатор первого вопроса
    FIRST_QUESTION = [By.CSS_SELECTOR, '[class*="Home_FAQ"] [id="accordion__heading-0"]']
    # локатор ответа первого вопроса
    FIRST_ANSWER = [By.CSS_SELECTOR, '[class*="Home_FAQ"] [id="accordion__panel-0"]']
    # локатор второго вопроса
    SECOND_QUESTION = [By.CSS_SELECTOR, '[class*="Home_FAQ"] [id="accordion__heading-1"]']
    # локатор ответа второго вопроса
    SECOND_ANSWER = [By.CSS_SELECTOR, '[class*="Home_FAQ"] [id="accordion__panel-1"]']
    # локатор третьего вопроса
    THIRD_QUESTION = [By.CSS_SELECTOR, '[class*="Home_FAQ"] [id="accordion__heading-2"]']
    # локатор ответа третьего вопроса
    THIRD_ANSWER = [By.CSS_SELECTOR, '[class*="Home_FAQ"] [id="accordion__panel-2"]']
    # локатор четвертого вопроса
    FOURTH_QUESTION = [By.CSS_SELECTOR, '[class*="Home_FAQ"] [id="accordion__heading-3"]']
    # локатор ответа четвертого вопроса
    FOURTH_ANSWER = [By.CSS_SELECTOR, '[class*="Home_FAQ"] [id="accordion__panel-3"]']
    # локатор пятого вопроса
    FIFTH_QUESTION = [By.CSS_SELECTOR, '[class*="Home_FAQ"] [id="accordion__heading-4"]']
    # локатор ответа пятого вопроса
    FIFTH_ANSWER = [By.CSS_SELECTOR, '[class*="Home_FAQ"] [id="accordion__panel-4"]']
    # локатор шестого вопроса
    SIXTH_QUESTION = [By.CSS_SELECTOR, '[class*="Home_FAQ"] [id="accordion__heading-5"]']
    # локатор ответа шестого вопроса
    SIXTH_ANSWER = [By.CSS_SELECTOR, '[class*="Home_FAQ"] [id="accordion__panel-5"]']
    # локатор седьмого вопроса
    SEVENTH_QUESTION = [By.CSS_SELECTOR, '[class*="Home_FAQ"] [id="accordion__heading-6"]']
    # локатор ответа седьмого вопроса
    SEVENTH_ANSWER = [By.CSS_SELECTOR, '[class*="Home_FAQ"] [id="accordion__panel-6"]']
    # локатор восьмого вопроса
    EIGHTH_QUESTION = [By.CSS_SELECTOR, '[class*="Home_FAQ"] [id="accordion__heading-7"]']
    # локатор ответа восьмого вопроса
    EIGHTH_ANSWER = [By.CSS_SELECTOR, '[class*="Home_FAQ"] [id="accordion__panel-7"]']
