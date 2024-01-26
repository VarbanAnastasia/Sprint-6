import pytest
from selenium.webdriver import Firefox
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service


@pytest.fixture
def driver():
    service = Service(GeckoDriverManager().install())
    driver = Firefox(service=service)
    driver.maximize_window()
    yield driver
    driver.quit()
