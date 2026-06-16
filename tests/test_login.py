import pytest
from pages.login_page import LoginPage
from utils.data_reader import leer_csv_login

@pytest.mark.parametrize("usuario, clave, es_valido", leer_csv_login())
def test_login_data_driven(driver, usuario, clave, es_valido):
    login_page = LoginPage(driver)
    
    login_page.login(usuario, clave)

    if es_valido:
        assert "/inventory.html" in driver.current_url, "No se redirigió al inventario"
    else:
        error = login_page.get_error_messageerror_message()
        assert "Epic sadface" in error, "No apareció el mensaje de error esperado"