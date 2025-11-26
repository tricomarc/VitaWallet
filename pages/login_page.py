import time
import traceback
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException, TimeoutException
from .base_page import BasePage
from locators.locators import LoginLocators

class LoginPage(BasePage):

    @property
    def button_IniciarSesion(self):
        return LoginLocators.INICIAR_SESION
    @property
    def input_Correo(self):
        return LoginLocators.input_Correo
    @property
    def input_Clave(self):
        return LoginLocators.input_Clave
    @property
    def checkBox(self):
        return LoginLocators.checkBox
    @property
    def button_Ingresar(self):
        return LoginLocators.button_Ingresar
    @property
    def label_Username(self):
        return LoginLocators.label_Username

    @property
    def div_Menu(self):
        return LoginLocators.div_Menu
    
    
    def login(self, email, password):
        """
        Realiza el proceso de inicio de sesión con manejo robusto de excepciones.
        """
        try:
            print(f"INFO: Intentando iniciar sesión con {email}...")
            
            self.click(self.button_IniciarSesion, 10)
            self.type_text(self.input_Correo, email)
            self.type_text(self.input_Clave, password)
            self.switchToIframe()
            self.click(self.checkBox, 10)
            self.switch_to_default_content()
            time.sleep(2)
            self.click(self.button_Ingresar, 10)
            self.wait_until_text_contains(self.label_Username, 'Hola, Test', 10)
            
            print("INFO: Login completado exitosamente y verificación de usuario 'Hola, Test' realizada.")
            
        except (NoSuchElementException, TimeoutException) as e:
            print(f"--- ¡FALLA CRÍTICA DE AUTOMATIZACIÓN! ---")
            print(f"ERROR: Falló el paso de login o la aserción debido a una excepción de Selenium.")
            print(f"TIPO: {type(e).__name__}")
            print(f"MENSAJE: {e.msg if hasattr(e, 'msg') else str(e)}")
            print("------------------------------------------")
            raise
            
        except Exception as e:
            print(f"--- ¡FALLA GENERAL DE AUTOMATIZACIÓN! ---")
            print(f"ERROR: Se encontró una excepción inesperada durante el login.")
            print(f"TIPO: {type(e).__name__}")
            traceback.print_exc()
            print("------------------------------------------")
            raise
        finally:
            print("INFO: Ejecutando finally: tomando captura de pantalla para registro.")
            self.take_screenshot()