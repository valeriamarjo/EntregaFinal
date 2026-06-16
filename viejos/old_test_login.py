import pytest
from selenium import webdriver
from utils.LoginPage import login

def test_login_validation_ok(driver):
    login_page = LoginPage(driver)

    login_page.login("standard_user","secret_sauce")
    
    assert "/inventory.html" in driver.current_url, "no se redirigió a la página indicada"

    def test_login_invalid_password(driver):
        login_page = LoginPage(driver)

        login_page.login("standar_user", "123456")

        error = login_page.get_error_passowrd_message()
        assert "Epic sadface: Username and pasword do not match any user in this service"