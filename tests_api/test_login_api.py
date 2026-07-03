import pytest
import requests

LOGIN_URL = 'https://reqres.in/api/login' 

headers_seguridad = {
    "x-api-key": "pub_5bca5ffc8772df976fcf8970168a1ad219ad499c472afbba2f27085fa4b4ef7d",
    "Content-Type": "application/json",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
}

@pytest.mark.api 
@pytest.mark.parametrize("email, password, expected_status", [
    ("eve.holt@reqres.in", "cityslicka", 200),  
    ("eve.holt@reqres.in", "", 400)             
])
def test_login_endpoint(email, password, expected_status):
    """Prueba parametrizada que evalúa los escenarios de autenticación en la API.""" 
    
    cuerpo_peticion = {
        "email": email,
        "password": password
    }
    
    respuesta = requests.post(LOGIN_URL, json=cuerpo_peticion, headers=headers_seguridad, verify=False)
    
    assert respuesta.status_code == expected_status, f"Se esperaba {expected_status} en cambio se recibió {respuesta.status_code}"
    
    if expected_status == 200:
        datos_devueltos = respuesta.json() 
        assert "token" in datos_devueltos, "El servidor de autenticación no retornó el token de acceso" 