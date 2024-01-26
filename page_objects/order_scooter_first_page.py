import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class LocatorOrderScooterFromFirstPage:
    NAME_INPUT = (By.XPATH, '//input[@placeholder="* Имя"]')
    SURNAME_INPUT = (By.XPATH, '//input[@placeholder="* Фамилия"]')
    ADDRESS_INPUT = (By.XPATH, '//input[@placeholder="* Адрес: куда привезти заказ"]')
    METRO_STATION_INPUT = (By.XPATH, '//input[@placeholder="* Станция метро"]')
    CERTAIN_METRO_STATION_INPUT = (By.XPATH, ".//div[@class='select-search has-focus']//div["
                                             "@class='select-search__select']")
    PHONE_INPUT = (By.XPATH, '//input[@placeholder="* Телефон: на него позвонит курьер"]')


class OrderScooterPage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Заполнение имени")
    def fill_name(self, name):
        name_input = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(LocatorOrderScooterFromFirstPage.NAME_INPUT))
        name_input.send_keys(name)

    @allure.step("Заполнение фамилии")
    def fill_surname(self, surname):
        surname_input = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(LocatorOrderScooterFromFirstPage.SURNAME_INPUT))
        surname_input.send_keys(surname)

    @allure.step("Заполнение адреса")
    def fill_address(self, address):
        address_input = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(LocatorOrderScooterFromFirstPage.ADDRESS_INPUT))
        address_input.send_keys(address)

    @allure.step("Заполнение станции метро")
    def fill_metro_station(self):
        metro_station = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(LocatorOrderScooterFromFirstPage.METRO_STATION_INPUT))
        metro_station.click()
        certain_metro_station = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(LocatorOrderScooterFromFirstPage.CERTAIN_METRO_STATION_INPUT)
        )
        certain_metro_station.click()

    @allure.step("Заполнение номера телефона")
    def fill_phone(self, phone):
        phone_input = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(LocatorOrderScooterFromFirstPage.PHONE_INPUT))
        phone_input.send_keys(phone)
        
    @allure.step("Заполнение формы")
    def fill_form(self, name, surname, address, phone):
        self.fill_name(name)
        self.fill_surname(surname)
        self.fill_address(address)
        self.fill_phone(phone)
        self.fill_metro_station()
