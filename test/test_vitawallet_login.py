# web-tests/tests/test_vitawallet_flows.py

import time
import pytest
from pages.login_page import LoginPage
from pages.base_page import BasePage
from data.config import REGISTER_URL
import random
import string

# --- Fixture de Pytest para el ciclo de vida del Driver ---

@pytest.fixture(scope="module")
def driver_setup():
    """Inicializa el driver antes de la suite de tests y lo cierra después."""
    driver = BasePage.setup_driver()
    yield driver
    driver.quit()

# ----------------------------------------------------
# Clase de Tests de Vita Wallet
# ----------------------------------------------------

class TestVitaWalletFlows:


    def test_01_intercambio_crypto_a_USDT(self, driver_setup):
        """
        Caso de Prueba: Registro de usuario Argentino y simulación de verificación.
        """
        driver = driver_setup
        login_page = LoginPage(driver)
        
        # 1. Navegar a la página de registro
        login_page.navigate(REGISTER_URL)
        
        
        # 2. Registrar el nuevo usuario
        login_page.login('mlazorc@gmail.com', 'Test*5915')
        time.sleep(5)
        login_page.click(login_page.div_Menu, 10)
        time.sleep(3)
        #login_page.take_screenshot()

        