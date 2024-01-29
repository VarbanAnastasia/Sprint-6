import allure
from selenium.webdriver.common.by import By

from page_objects.base_page import BasePage


class LogoLocators:
    SCOOTER_LOGO = (By.XPATH, ".//*[@alt='Scooter']")
    YANDEX_LOGO = (By.XPATH, "//*[@alt='Yandex']")
    DZEN_LOGO = [By.XPATH, ".//*[@tabindex='0']"]

    COOKIES = (By.XPATH, ".//*[@id='rcc-confirm-button']")


class Logo(BasePage):

    @allure.step("Клик логотипа Самоката")
    def click_logo_scooter(self):
        return self.find_element_located_click(LogoLocators.SCOOTER_LOGO)

    @allure.step("Переход по логотипу Яндекс")
    def transition_logo_yandex(self):
        self.find_element_located_click(LogoLocators.YANDEX_LOGO)

    @allure.step("Переход на вторую вкладку")
    def switch_dzen(self):
        self.switch_window(LogoLocators.DZEN_LOGO, 1)








