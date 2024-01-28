import allure
from selenium.webdriver.common.by import By

from page_objects.base_page import BasePage


class LocatorOrderScooterFromFirstPage:
    NAME_INPUT = (By.XPATH, '//input[@placeholder="* Имя"]')
    SURNAME_INPUT = (By.XPATH, '//input[@placeholder="* Фамилия"]')
    ADDRESS_INPUT = (By.XPATH, '//input[@placeholder="* Адрес: куда привезти заказ"]')
    METRO_STATION_INPUT = (By.XPATH, '//input[@placeholder="* Станция метро"]')
    CERTAIN_METRO_STATION_INPUT = (By.XPATH, ".//div[@class='select-search has-focus']//div["
                                             "@class='select-search__select']")
    PHONE_INPUT = (By.XPATH, '//input[@placeholder="* Телефон: на него позвонит курьер"]')


class OrderScooterPage(BasePage):

    @allure.step("Заполнение имени")
    def fill_name(self, name):
        return self.find_element_located(LocatorOrderScooterFromFirstPage.NAME_INPUT).send_keys(name)

    @allure.step("Заполнение фамилии")
    def fill_surname(self, surname):
        return self.find_element_located(LocatorOrderScooterFromFirstPage.SURNAME_INPUT).send_keys(surname)

    @allure.step("Заполнение адреса")
    def fill_address(self, address):
        return self.find_element_located(LocatorOrderScooterFromFirstPage.ADDRESS_INPUT).send_keys(address)

    @allure.step("Заполнение станции метро")
    def fill_metro_station(self):
        self.find_element_located_click(LocatorOrderScooterFromFirstPage.METRO_STATION_INPUT)
        return self.find_element_located_click(LocatorOrderScooterFromFirstPage.CERTAIN_METRO_STATION_INPUT)

    @allure.step("Заполнение номера телефона")
    def fill_phone(self, phone):
        self.find_element_located(LocatorOrderScooterFromFirstPage.PHONE_INPUT).send_keys(phone)
        
    @allure.step("Заполнение формы")
    def fill_form(self, name, surname, address, phone):
        self.fill_name(name)
        self.fill_surname(surname)
        self.fill_address(address)
        self.fill_phone(phone)
        self.fill_metro_station()
