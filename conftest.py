# conftest.py
import pytest
import os
from datetime import datetime
from selenium import webdriver

from pages.login_page import LoginPage
from utils.data_reader import leer_csv_login

@pytest.fixture
def driver():
    """1. Inicialización básica del navegador en modo incógnito."""
    options = webdriver.ChromeOptions()
    options.add_argument("--incognito")

    chrome_driver = webdriver.Chrome(options=options)
    chrome_driver.implicitly_wait(5) 

    yield chrome_driver #

    chrome_driver.quit()


@pytest.fixture
def login_in_driver(driver):
    """2. Fixture intermedia que loguea al usuario estándar de forma directa usando POM."""
    login_page = LoginPage(driver)

    login_page.login("standard_user", "secret_sauce")
    return driver


@pytest.fixture
def driver_logged(driver):
    """3. Fixture avanzada que lee el primer usuario de tu CSV y arranca logueado."""
    login_page = LoginPage(driver)
    
    lista_usuarios = leer_csv_login()
    primer_usuario = lista_usuarios[0] 

    usuario = primer_usuario[0]
    clave = primer_usuario[1]
    
    login_page.login(usuario, clave)
    return driver


def pytest_configure(config):
    if config.getoption("--html"):
        fecha = datetime.now().strftime("%Y%m%d_%H%M%S")
        config.option.htmlpath = f"Test_resultados/SauceDemoTCRepo_{fecha}.html"