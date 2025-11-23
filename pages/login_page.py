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
        # El bloque TRY contiene todos los pasos críticos del login.
        try:
            print(f"INFO: Intentando iniciar sesión con {email}...")
            
            # Clics e Inputs
            self.click(self.button_IniciarSesion, 10)
            self.type_text(self.input_Correo, email)
            self.type_text(self.input_Clave, password)
            
            # Manejo de reCAPTCHA (asumiendo que switchToIframe usa self.recaptcha_iframe)
            self.switchToIframe() # Asumiendo que esta es tu función personalizada
            self.click(self.checkBox, 10)
            self.switch_to_default_content()
            time.sleep(2)
            # Finalizar Login
            self.click(self.button_Ingresar, 10)
            
            # Aserción (punto de falla común si el login no funciona)
            self.wait_until_text_contains(self.label_Username, 'Hola, Test', 10)
            
            print("INFO: Login completado exitosamente y verificación de usuario 'Hola, Test' realizada.")
            
        # El bloque EXCEPT captura los errores de Selenium y realiza un manejo de fallos.
        except (NoSuchElementException, TimeoutException) as e:
            # Captura elementos no encontrados o timeouts de espera
            print(f"--- ¡FALLA CRÍTICA DE AUTOMATIZACIÓN! ---")
            print(f"ERROR: Falló el paso de login o la aserción debido a una excepción de Selenium.")
            print(f"TIPO: {type(e).__name__}")
            print(f"MENSAJE: {e.msg if hasattr(e, 'msg') else str(e)}")
            print("------------------------------------------")
            # Esto re-lanza el error para que el test case falle formalmente
            raise
            
        except Exception as e:
            # Captura cualquier otra excepción no manejada específicamente
            print(f"--- ¡FALLA GENERAL DE AUTOMATIZACIÓN! ---")
            print(f"ERROR: Se encontró una excepción inesperada durante el login.")
            print(f"TIPO: {type(e).__name__}")
            traceback.print_exc() # Imprime el stack trace completo para la depuración
            print("------------------------------------------")
            # Re-lanza la excepción
            raise
            
        # El bloque FINALLY se ejecuta siempre, independientemente de si el TRY tuvo éxito o el EXCEPT falló.
        finally:
            print("INFO: Ejecutando finally: tomando captura de pantalla para registro.")
            #self.take_screenshot()