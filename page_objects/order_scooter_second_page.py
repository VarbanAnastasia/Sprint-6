import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class LocatorOrderScooterFromSecondPage:
    DATE_PICKER = (By.XPATH, ".//input[@placeholder='* Когда привезти самокат']")
    DATE_PICKER_CHOICE = (By.CSS_SELECTOR, ".react-datepicker__day--025")
    RENT_PERIOD = (By.XPATH, "//div[@class='Dropdown-control']/div[@class='Dropdown-placeholder']")
    RENT_PERIOD_CHOICE = (By.XPATH, '//div[@class="Dropdown-menu"]/div[@class="Dropdown-option" and text() = "двое '
                                    'суток"]')
    COLOUR_CHOICE = (By.XPATH, "//input[@id='black']")
    COMMENT_INPUT = (By.XPATH, './/input[@placeholder="Комментарий для курьера"]')
    BACK_BUTTON = (By.XPATH, './/button[@class="Button_Button__ra12g Button_Middle__1CSJM Button_Inverted__3IF-i"]')
    ORDER_BUTTON = (By.XPATH, '//div[@class="Order_Buttons__1xGrp"]/button[@class="Button_Button__ra12g '
                              'Button_Middle__1CSJM"]')
    CONFIRMATION_BUTTON_YES = (By.XPATH, '//div[@class="Order_Modal__YZ-d3"]//button[@class="Button_Button__ra12g '
                                         'Button_Middle__1CSJM"]')
    CONFIRMATION_BUTTON_NO = (By.XPATH, '//div[@class="Order_Modal__YZ-d3"]//button[@class="Button_Button__ra12g '
                                        'Button_Middle__1CSJM Button_Inverted__3IF-i"]')
    SEE_STATUS = (By.XPATH, '//div[@class="Order_Modal__YZ-d3"]//button[@class="Button_Button__ra12g '
                            'Button_Middle__1CSJM"]')
    SUCCESSFUL_ORDER = (By.CSS_SELECTOR, '.Order_ModalHeader__3FDaJ')


@allure.step("Заполнение второй формы для оформления заказа")
class OrderScooterPageSecond:

    def __init__(self, driver):
        self.driver = driver

    @allure.step("Заполнение даты")
    def fill_date_form(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(LocatorOrderScooterFromSecondPage.DATE_PICKER)).click()
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(LocatorOrderScooterFromSecondPage.DATE_PICKER_CHOICE)).click()

    @allure.step("Заполнение периода аренды")
    def fill_rent_period(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(LocatorOrderScooterFromSecondPage.RENT_PERIOD)).click()
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(LocatorOrderScooterFromSecondPage.RENT_PERIOD_CHOICE)).click()

    @allure.step("Заполнение цвета")
    def fill_color(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(LocatorOrderScooterFromSecondPage.COLOUR_CHOICE)).click()

    def fill_comment(self, comment):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(LocatorOrderScooterFromSecondPage.COMMENT_INPUT)).send_keys(comment)

    @allure.step("Заполнение второй формы")
    def fill_second_form(self):
        self.fill_date_form()
        self.fill_rent_period()
        self.fill_color()
        self.fill_comment('Не забудьте привезти самокат')

    @allure.step("Нажатие кнопки назад")
    def click_back_button(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(LocatorOrderScooterFromSecondPage.BACK_BUTTON)).click()

    @allure.step("Нажатие кнопки оформления заказа")
    def click_order_button(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(LocatorOrderScooterFromSecondPage.ORDER_BUTTON)).click()

    @allure.step("Нажатие кнопки подтверждения")
    def click_confirmation_button_yes(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(LocatorOrderScooterFromSecondPage.CONFIRMATION_BUTTON_YES)).click()

    @allure.step("Нажатие кнопки отмены")
    def click_confirmation_button_no(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(LocatorOrderScooterFromSecondPage.CONFIRMATION_BUTTON_NO)).click()

    @allure.step("Нажатие кнопки посмотреть статус")
    def click_see_status(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(LocatorOrderScooterFromSecondPage.SEE_STATUS)).click()

    @allure.step("Проверка успешного оформления заказа")
    def check_successful_order(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(LocatorOrderScooterFromSecondPage.SUCCESSFUL_ORDER)).text
