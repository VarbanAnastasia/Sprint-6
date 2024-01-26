import allure
import pytest

from page_objects.base_page import BasePage, BasePageLocators
from page_objects.order_scooter_first_page import OrderScooterPage
from conftest import driver
from page_objects.order_scooter_second_page import OrderScooterPageSecond


@allure.story("Заказ самоката")
class TestOrderScooter:

    # Заказ с помощью кнопки наверху
    @pytest.mark.parametrize("name, surname, address, phone", [
        ("Анастасия", "Варбан", "ул Пушкина 13", "+796123222334"),
        ("Анна", "Петрова", "ул Пушкина 13", "+796123222334"),
    ])
    @allure.title("Заказ с помощью кнопки наверху")
    def test_order_scooter_button_top(self, driver, name, surname, address, phone):
        base_page = BasePage(driver)
        base_page.go_to_site('https://qa-scooter.praktikum-services.ru/')
        base_page.find_element_located(BasePageLocators.ORDER_BUTTON_TOP).click()
        order_scooter = OrderScooterPage(driver)
        order_scooter.fill_form(name, surname, address, phone)
        base_page.find_element_located(BasePageLocators.CONTINUE_BUTTON).click()
        assert driver.current_url == "https://qa-scooter.praktikum-services.ru/order"

        rent_information = OrderScooterPageSecond(driver)
        rent_information.fill_second_form()

        rent_information.click_back_button()
        base_page.find_element_located(BasePageLocators.CONTINUE_BUTTON).click()
        rent_information.click_order_button()
        rent_information.click_confirmation_button_no()
        rent_information.click_order_button()
        rent_information.click_confirmation_button_yes()
        assert 'Заказ оформлен' in rent_information.check_successful_order()
        rent_information.click_see_status()

    @allure.title("Заказ с помощью кнопки внизу")
    # Заказ с помощью кнопки внизу
    @pytest.mark.parametrize("name, surname, address, phone", [
        ("Анастасия", "Варбан", "ул Пушкина 13", "+796123222334"),
        ("Анна", "Петрова", "ул Пушкина 13", "+796123222334"),
    ])
    def test_order_scooter_button_bottom(self, driver, name, surname, address, phone):
        base_page = BasePage(driver)
        base_page.go_to_site('https://qa-scooter.praktikum-services.ru/')
        base_page.scroll_to_order_button()
        base_page.find_element_located(BasePageLocators.ORDER_BUTTON_BOTTOM).click()
        order_scooter = OrderScooterPage(driver)
        order_scooter.fill_form(name, surname, address, phone)
        base_page.find_element_located(BasePageLocators.CONTINUE_BUTTON).click()
        assert driver.current_url == "https://qa-scooter.praktikum-services.ru/order"

        rent_information = OrderScooterPageSecond(driver)
        rent_information.fill_second_form()

        rent_information.click_back_button()
        base_page.find_element_located(BasePageLocators.CONTINUE_BUTTON).click()
        rent_information.click_order_button()
        rent_information.click_confirmation_button_no()
        rent_information.click_order_button()
        rent_information.click_confirmation_button_yes()
        assert 'Заказ оформлен' in rent_information.check_successful_order()
        rent_information.click_see_status()


