import time
import pytest
from pages.login_page import LoginPage
from pages.cripto_page import CriptoPage 
from pages.base_page import BasePage
from data.config import REGISTER_URL, USER, PASSWORD


# --- Fixture de Pytest para el ciclo de vida del Driver ---

@pytest.fixture(scope="module")
def driver_setup():
    """Inicializa el driver antes de la suite de tests y lo cierra después."""
    driver = BasePage.setup_driver()
    yield driver
    driver.quit()

class TestVitaWalletFlows:


    def test_01_intercambio_crypto_a_USDT(self, driver_setup):
        """
        Caso de Prueba: Flujo intercambio cripto moneda, de peso Argentino a USD Tether.
        """
        driver = driver_setup
        login_page = LoginPage(driver)
        cripto_page = CriptoPage(driver)
        
        # 1. Navegar al Login de VitaWallet
        login_page.navigate(REGISTER_URL)
        
        # 2. Login
        login_page.login(USER, PASSWORD)
        
        #3. Intercambio de moneda Peso Argentino a USDT
        cripto_page.intercambioCripto("Peso Argentino","  -  USD Tether")
        time.sleep(5)
        cripto_page.take_screenshot()
      

        