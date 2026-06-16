# pages/login_page.py
from selenium.webdriver.common.by import By

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

        # Selectores originales corregidos (By.ID en mayúsculas para que Python no falle)
        self.username_input = (By.ID, "user-name")
        self.password_input = (By.ID, "password")
        self.login_button = (By.ID, "login-button")
        self.error_password = (By.CSS_SELECTOR, "[data-test='error']")

    def open_page(self):
        # Corregido: Agregamos https:// para que Selenium entienda la dirección
        self.driver.get("https://www.saucedemo.com")

    def ingresar_usuario(self, usuario):
        # Comandos puros y directos de tu curso
        self.driver.find_element(*self.username_input).send_keys(usuario)
    
    def ingresar_password(self, password):
        self.driver.find_element(*self.password_input).send_keys(password)

    def click_login(self):
        self.driver.find_element(*self.login_button).click()

    def login(self, usuario, password):
        # Tu lógica original de login secuencial
        self.open_page()
        self.ingresar_usuario(usuario)
        self.ingresar_password(password)
        self.click_login()

    def get_error_messageerror_message(self):
        # Lectura directa del texto tal como lo tenías en tu borrador
        error = self.driver.find_element(*self.error_password).text
        print(error) 
        return error