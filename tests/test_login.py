import pytest
from pages.login_page import LoginPage
from utils.data_reader import leer_csv_login

@pytest.mark.ui
@pytest.mark.parametrize("username, password, es_valido", leer_csv_login())
def test_login_data_driven(driver, username, password, es_valido):
    
    login_page = LoginPage(driver)
    
    login_page.ejecutar_login(username, password)

    if es_valido:
        assert "/inventory.html" in driver.current_url, "El sistema no redirigió al inventario de productos"
    else:
        texto_error = login_page.obtener_mensaje_error()
        assert "Epic sadface" in texto_error, "El mensaje de error esperado no se visualizó en la pantalla"