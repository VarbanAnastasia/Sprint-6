import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePageLocators:
    ORDER_BUTTON_TOP = (By.XPATH, "//div[@class='Header_Header__214zg']//button[@class='Button_Button__ra12g']")
    ORDER_BUTTON_BOTTOM = (By.CSS_SELECTOR, ".Button_Button__ra12g.Button_Middle__1CSJM")
    CONTINUE_BUTTON = (By.XPATH, "//div[@class='Order_NextButton__1_rCA']//button[@class='Button_Button__ra12g "
                                 "Button_Middle__1CSJM']")


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    @allure.step("Переход на сайт")
    def go_to_site(self, url):
        return self.driver.get(url)

    @allure.step("Нахождение элемента")
    def find_element_located(self, locator):
        return WebDriverWait(self.driver, 20).until(expected_conditions.presence_of_element_located(locator))

    def find_element_located_click(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(expected_conditions.presence_of_element_located(locator)).click()

    @allure.step("Скролл страницы")
    def scroll_to_qa_block(self, locator):
        qa_block_element = self.find_element_located(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", qa_block_element)

    @allure.step("Скролл страницы")
    def scroll_to_order_button(self, locator):
        WebDriverWait(self.driver, 20).until(expected_conditions.visibility_of_element_located(locator))
        order_button_element = self.find_element_located(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", order_button_element)

    @allure.step("Переключение экрана")
    def switch_window(self, locator, num, time=10):
        self.driver.switch_to.window(self.driver.window_handles[num])
        return WebDriverWait(self.driver, time).until(expected_conditions.presence_of_element_located(locator))

    @allure.step("Получение ссылки на страницу")
    def current_url(self):
        return self.driver.current_url



