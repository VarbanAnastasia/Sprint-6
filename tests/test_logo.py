import allure

from conftest import driver
from page_objects.base_page import BasePage
from page_objects.logo import Logo


@allure.story("Логотипы")
class TestLogo:
    @allure.title("Проверка возврата на главную страницу при нажатии лого Самокат")
    def test_redirection_to_main_page(self, driver):
        base_page = BasePage(driver)
        base_page.go_to_site('https://qa-scooter.praktikum-services.ru/')
        logo = Logo(driver)
        logo.click_logo_scooter()
        assert base_page.current_url() == 'https://qa-scooter.praktikum-services.ru/'

    @allure.title("Проверка возврата на главную страницу Дзен при нажатии лого Яндекс")
    def test_redirection_to_yandex_main_page(self, driver):
        base_page = BasePage(driver)
        base_page.go_to_site('https://qa-scooter.praktikum-services.ru/')
        logo = Logo(driver)
        logo.transition_logo_yandex()
        logo.switch_dzen()
        current_url = logo.current_url()
        assert 'https://dzen.ru/' in current_url


