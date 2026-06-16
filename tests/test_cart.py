from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage

def test_cart_pom_con_bucles(login_in_driver):
    driver = login_in_driver 

    inventory_page = InventoryPage(driver)
    cart_page = CartPage(driver)

    nombre_esperado = inventory_page.nombre_producto_uno()

    inventory_page.agregar_al_carrito()

    assert inventory_page.obtener_contador() == "1", "El contador del carrito no se actualizó"

    inventory_page.ir_al_carrito()

    lista_productos_carrito = cart_page.obtener_productos_carrito()
    
    item_del_carrito = lista_productos_carrito[0]["name"]

    assert item_del_carrito == nombre_esperado, "El producto en el carrito no coincide con el seleccionado"