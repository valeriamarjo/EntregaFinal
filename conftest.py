import pytest
from selenium import webdriver
from utils.loginpage import login
import os
from datetime import datetime
from page.login_page import LoginPage
from users.data_reader import user

@pytest.fixture
def driver(): #inicalización del navegador para las pruebas
    options = webdriver.ChromeOptions()
    options.add_argument("--incognito")

    chrome_driver= webdriver.Chrome(options= options)

    yield chrome_driver #pausa el código hasta aca

    chrome_driver.quit()

@pytest.fixture
def login_in_driver(driver):
    login(driver)
    return (driver)

import os
from datetime import datetime

def pytest_configure(config):
    # Esto cambia la ruta del reporte dinámicamente antes de empezar
    if config.getoption("--html"):
        fecha = datetime.now().strftime("%Y%m%d_%H%M%S")
        config.option.htmlpath = f"Test_resultados/SauceDemoTCRepo_{fecha}.html"

@pytest.fixture
def driver_logged(driver):
    login_page = LoginPage(driver)

    user = read_users_csv()[0]

    login_page.login(user["username", user["password"]])

    return driver