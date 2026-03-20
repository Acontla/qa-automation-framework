from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    """Clase base con funciones comunes para todas las páginas"""
    
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
    
    def find_element(self, locator):
        """Encuentra un elemento esperando a que sea visible"""
        return self.wait.until(EC.visibility_of_element_located(locator))
    
    def click(self, locator):
        """Hace clic en un elemento"""
        self.find_element(locator).click()
    
    def enter_text(self, locator, text):
        """Escribe texto en un campo"""
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)
    
    def get_text(self, locator):
        """Obtiene el texto de un elemento"""
        return self.find_element(locator).text
