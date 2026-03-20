from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class InventoryPage(BasePage):
    """Página de inventario/productos de SauceDemo"""
    
    # Localizadores
    PRODUCT_LIST = (By.CLASS_NAME, "inventory_list")
    
    def is_product_list_displayed(self):
        """Verifica que la lista de productos sea visible"""
        try:
            self.find_element(self.PRODUCT_LIST)
            return True
        except:
            return False
