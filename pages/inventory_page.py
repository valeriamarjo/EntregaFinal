# pages/inventory_page.py
from selenium.webdriver.common.by import By

class InventoryPage:
    def __init__(self, driver):
        self.driver = driver
      
        # Tus selectores originales (corregidos en mayúsculas)
        self.contador_Carrito = (By.CLASS_NAME, "shopping_cart_badge")
        self.link_carrito = (By.CLASS_NAME, "shopping_cart_link")
        self.nombres_productos = (By.CLASS_NAME, "inventory_item_name")
        
        # Selector para los botones de agregar al carrito (Clase 8/9)
        self.btn_inventario = (By.CLASS_NAME, "btn_inventory")

    def obtener_titulo(self):
        # Devuelve el título del navegador
        return self.driver.title

    def obtener_contador(self):
        # Devuelve el texto del número del carrito
        return self.driver.find_element(*self.contador_Carrito).text

    def agregar_al_carrito(self):
        # Corregido: Agregamos los paréntesis obligatorios en .click() para que ejecute la acción
        self.driver.find_elements(*self.btn_inventario)[0].click()

    def nombre_producto_uno(self):
        # Devuelve el texto del primer producto de la lista
        return self.driver.find_elements(*self.nombres_productos)[0].text

    def ir_al_carrito(self):
        # Corregido: Agregamos los paréntesis en .click()
        self.driver.find_element(*self.link_carrito).click()