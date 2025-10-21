import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from core.environment.host import get_host_for_selenium_testing
from core.selenium.common import initialize_driver, close_driver

@pytest.fixture(scope="module")
def driver():
    d = initialize_driver()
    yield d
    close_driver(d)

def test_notepad_redirects_to_login(driver):
    """
    Estilo tutorial: abrimos /notepad y comprobamos que redirige a /login.
    """
    host = get_host_for_selenium_testing()
    driver.get(f"{host}/notepad")
    WebDriverWait(driver, 10).until(EC.url_contains("/login"))

if __name__ == "__main__":
    driver = initialize_driver()
    try:
        test_notepad_redirects_to_login(driver)
    except Exception as e:
        pass
    finally:
        close_driver(driver)