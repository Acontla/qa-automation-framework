from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoginPage(BasePage):
    """Página de login de SauceDemo"""
    
    # Localizadores
    USERNAME_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "h3[data-test='error']")
    
    def navigate_to(self, url):
        """Navega a la URL especificada"""
        self.driver.get(url)
    
    def login(self, username, password):
        """Realiza login con usuario y contraseña"""
        self.enter_text(self.USERNAME_INPUT, username)
        self.enter_text(self.PASSWORD_INPUT, password)
        self.click(self.LOGIN_BUTTON)
    
    def get_error_message(self):
        """Obtiene el mensaje de error si existe"""
        try:
            return self.get_text(self.ERROR_MESSAGE)
        except:
            return ""
