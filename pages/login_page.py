from selenium.webdriver.common.by import By

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

        self.username_input = (By.ID, "user-name")
        self.password_input = (By.ID, "password")
        self.login_button = (By.ID, "login-button")
        self.error_container = (By.CSS_SELECTOR, "[data-test='error']")

    def open_page(self):
        self.driver.get("https://www.saucedemo.com")

    def ingresar_username(self, username):
        input_web = self.driver.find_element(*self.username_input)
        input_web.clear()
        input_web.send_keys(username)
    
    def ingresar_password(self, password):
        input_web = self.driver.find_element(*self.password_input)
        input_web.clear()
        input_web.send_keys(password)

    def click_login(self):
        self.driver.find_element(*self.login_button).click()

    def ejecutar_login(self, username, password):
        self.open_page()
        self.ingresar_username(username)
        self.ingresar_password(password)
        self.click_login()

    def obtener_mensaje_error(self):
        texto_error = self.driver.find_element(*self.error_container).text
        return texto_error