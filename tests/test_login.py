from selenium.webdriver.common.by import By

def test_login_saucedemo(driver):
    """Prueba básica de login en SauceDemo"""
    # Abrir página
    driver.get("https://www.saucedemo.com")
    
    # Escribir usuario y contraseña
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    
    # Hacer clic en login
    driver.find_element(By.ID, "login-button").click()
    
    # Verificar que se cargó la página de productos
    assert "inventory" in driver.current_url
    print("✅ Login exitoso!")
