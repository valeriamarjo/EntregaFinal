from selenium.webdriver.common.by import By

class InventoryPage:
    def __init__(self, driver):
      
         self.contador_Carrito = (By.CLASS_NAME, "shopping_cart_badge")
         self.link_carrito = (By.CLASS_NAME, "shopping_Cart_link")
         self.nombres_productos = (By.CLASS_NAME, "inventory_item_name")

    def obtener_titulo(self):
        return self.driver.title

    def obtener_productos (self):
        return self.driver.find_elements(*self.inventory_items)

    def menu_visible (self):
        return self.driver.find_element(*self.menu_button).is_displayed()

    def filtro_visible (self):
        return self.driver.find_element(*self.filtro).is_displayed()
    
    def agregar_al_carrito(self):
        self.driver.find_elements(*self.add_to_Cart_buttons)[0].click

    def obtener_contador(self):
        return self.driver.find_element(*self.contador_Carrito).text

    def nombre_producto_uno(self):
        return self.driver.find_elements(*self.nombres_productos)[0].text

    def ir_al_carrito (self):
        self.driver.find_element(*self.link_carrito).click

    def agregar_producto_por_nombre(self, nombre_producto_json):
        productos = self.driver.find_elements(*self.inventory_items)

        for producto in productos: 
            nombre = self.driver.find_element(*self.nombres_productos).text

            if nombre == nombre_producto_json:
                producto.find_element(*self.add_to_Cart_buttons).click()



