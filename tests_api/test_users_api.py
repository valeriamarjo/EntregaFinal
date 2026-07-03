import pytest
import requests

USERS_URL = "https://reqres.in/api/users"

headers_seguridad = {
    "x-api-key": "pub_5bca5ffc8772df976fcf8970168a1ad219ad499c472afbba2f27085fa4b4ef7d",
    "Content-Type": "application/json",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
}

@pytest.mark.api
def test_crear_usuario_endpoint():
    #Validar la creación exitosa de un nuevo usuario
    
    solicitud = {
        "name": "Valeria",
        "email": "avmar1273@gmail.com",
        "password": "AQA-PF-2026"
    }
    
    respuesta = requests.post(USERS_URL, json=solicitud, headers=headers_seguridad, verify=False)
    
    # Validación Código 201-- Creado
    assert respuesta.status_code == 201, f"Se esperaba 201 pero se recibió {respuesta.status_code}"
    
    datos_devueltos = respuesta.json()
    
    #Validación guardado correcto de campos
    assert datos_devueltos["name"] == solicitud["name"], "El nombre guardado no coincide con el enviado"
    assert datos_devueltos["email"] == solicitud["email"], "El email guardado no coincide con el enviado"
    
    tiempo_respuesta = respuesta.elapsed.total_seconds()
    assert tiempo_respuesta < 1.0, f"La API tardó demasiado: {tiempo_respuesta} segundos"


@pytest.mark.api
def test_consultar_usuario_endpoint():
        
    url_especifica = f"{USERS_URL}/2"
    
    respuesta = requests.get(url_especifica, headers=headers_seguridad, verify=False)
    
    assert respuesta.status_code == 200, f"Se esperaba 200 en cambio se recibió {respuesta.status_code}"
    
    tiempo_respuesta = respuesta.elapsed.total_seconds()
    assert tiempo_respuesta < 1.0, f"La API tardó demasiado: {tiempo_respuesta} segundos"


@pytest.mark.api
def test_eliminar_usuario_endpoint():
    
    url_especifica = f"{USERS_URL}/2"
    
    #baja de usuario
    respuesta = requests.delete(url_especifica, headers=headers_seguridad, verify=False)
    
    assert respuesta.status_code == 204, f"Se esperaba 204 en cambio se recibió {respuesta.status_code}"