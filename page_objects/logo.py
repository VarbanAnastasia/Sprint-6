import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

from page_objects.base_page import BasePage


class LogoLocators:
    SCOOTER_LOGO = (By.XPATH, ".//*[@alt='Scooter']")
    YANDEX_LOGO = (By.XPATH, "//*[@alt='Yandex']")
    DZEN_LOGO = [By.XPATH, ".//*[@tabindex='0']"]

    COOKIES = (By.XPATH, ".//*[@id='rcc-confirm-button']")


class Logo(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    @allure.step("Клик логотипа Самоката")
    def click_logo_scooter(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(LogoLocators.SCOOTER_LOGO)).click()

    @allure.step("Переход по логотипу Яндекс")
    def transition_logo_yandex(self):
        self.find_element_located_click(LogoLocators.YANDEX_LOGO)

    @allure.step("Переход на вторую вкладку")
    def switch_dzen(self):
        self.switch_window(LogoLocators.DZEN_LOGO, 1)








