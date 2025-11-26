import os
from socket import timeout
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.common.exceptions import NoAlertPresentException, TimeoutException, NoSuchElementException

class BasePage:
    """Clase base para inicializar el WebDriver y métodos comunes."""
    
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 15)

    @classmethod
    def setup_driver(cls):
        """Inicializa el WebDriver usando webdriver-manager."""
        chrome_options = Options()

        mobile_emulation = {
            "deviceMetrics": { "width": 375, "height": 812, "pixelRatio": 3.0 },
            "userAgent": "Mozilla/5.0 (Linux; Android 10; SM-G973F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.181 Mobile Safari/537.36"
        }
        chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
       
        prefs = {
            "profile.default_content_setting_values.notifications": 1,
            "profile.default_content_setting_values.geolocation": 1,
        }
        chrome_options.add_experimental_option("prefs", prefs)
        service = ChromeService(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=chrome_options)
        return driver

    def _get_wait(self, timeout):
        """Helper para obtener el objeto WebDriverWait, usando un timeout variable o el predeterminado."""
        if timeout is not None:
            return WebDriverWait(self.driver, timeout)
        return self.wait
    
    def navigate(self, url):
        """Navega a la URL dada."""
        self.driver.get(url)

    def find_element(self, by_locator):
        """Espera y retorna un elemento basado en su localizador."""
        return self.wait.until(EC.presence_of_element_located(by_locator))
    
    def click(self, by_locator, MAX_TIMEOUT):
        """Espera a que el elemento sea clickeable y luego hace click."""
        wait = WebDriverWait(self.driver, MAX_TIMEOUT)
        element = wait.until(EC.element_to_be_clickable(by_locator))
        element.click()
    
    def switchToIframe(self):
        """Cambia al iframe de recaptcha"""
        self.driver.switch_to.frame(0)

    def switch_to_default_content(self):
        """Vuelve el contexto del driver a la página principal (la ventana superior)."""
        self.driver.switch_to.default_content()
        
    def type_text(self, by_locator, text):
        """Escribe texto en un campo de entrada."""
        element = self.find_element(by_locator)
        element.clear()
        element.send_keys(text)

    def wait_until_text_contains(self, by_locator, expected_text, timeout=None):
        """Espera hasta que el texto esperado esté presente en el elemento."""
        wait_obj = self._get_wait(timeout)
        try:
            wait_obj.until(EC.text_to_be_present_in_element(by_locator, expected_text))
            return self.find_element(by_locator)
        except TimeoutException:
            current_timeout = timeout if timeout is not None else self.default_timeout
            print(f"Error: El texto '{expected_text}' no apareció en el elemento {by_locator} dentro de {current_timeout}s.")
            raise
    
    def handle_native_alert(self, action="accept", wait_time=5):
        """Acepta pop-ups de alerta nativa del navegador"""
        print(f"[ALERTA NATIVA] Esperando la alerta nativa por {wait_time}s...")
        time.sleep(wait_time)
        try:
            alert = self.driver.switch_to.alert
            alert_text = alert.text
            print(f"[ALERTA NATIVA] Alerta encontrada con texto: '{alert_text}'")

            if action == "accept":
                alert.accept()
                print("[ALERTA NATIVA] Acción: Permitir (accept) simulada.")
            elif action == "dismiss":
                alert.dismiss()
                print("[ALERTA NATIVA] Acción: Bloquear (dismiss) simulada.")
            
            return True

        except NoAlertPresentException:
            print("[ALERTA NATIVA] No se encontró ninguna alerta nativa. Continuando.")
            return False
        except Exception as e:
            print(f"[ALERTA NATIVA] Error al manejar la alerta: {e}")
            raise

    def wait_for_visibility(self, by_locator, timeout=None):
      """Espera hasta que el elemento sea visible en la interfaz."""
      wait_obj = self._get_wait(timeout)
      try:
          return wait_obj.until(EC.visibility_of_element_located(by_locator))
      except TimeoutException: 
          current_timeout = timeout if timeout is not None else self.default_timeout
          print(f"Error: El elemento localizado por {by_locator} no se hizo visible dentro de {current_timeout}s.")
          raise
        
    def take_screenshot(self, filename="screenshot"):
     """
     Captura la pantalla y la guarda en la carpeta 'screenshots'.
     Retorna la ruta completa del archivo guardado.
     """
     # Asegurarse de que la carpeta 'screenshots' exista
     if not os.path.exists("screenshots"):
         os.makedirs("screenshots")
     
     # Crear un nombre de archivo único
     timestamp = time.strftime("%Y%m%d-%H%M%S")
     filepath = os.path.join("screenshots", f"{filename}_{timestamp}.png")
     
     try:
         self.driver.save_screenshot(filepath)
         print(f"[SCREENSHOT] Captura guardada en: {filepath}")
         return filepath
     except Exception as e:
         print(f"[ERROR SCREENSHOT] No se pudo tomar la captura de pantalla: {e}")
         return None