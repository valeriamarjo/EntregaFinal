from selenium import webdriver
from selenium.webdriver.common.by import By

def login(driver):
    driver.get("https://demosauce.com/")

    usuario = driver.find_element(By.ID, "user-name")
    usuario.send_keys("standard_user") 

    clave = driver.find_element(By.ID, "password")
    clave.send_keys("secret_sauce")

    boton = driver.find_element(By.ID, "login-button").click()
    

