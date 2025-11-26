from selenium.webdriver.common.by import By

class LoginLocators:
    INICIAR_SESION = (By.XPATH, "//*[@id='root']/div/div/div/div/div/div/div[2]/div/div[2]/div/div")
    input_Correo = (By.ID, "i-login-email")
    input_Clave = (By.ID, "i-login-password")
    checkBox = (By.XPATH, "//*[@id='recaptcha-anchor']/div[1]")
    button_Ingresar = (By.ID, "b-login-submit")
    label_Username = (By.XPATH, "//div[contains(normalize-space(), 'Hola, Test')]")
    div_Menu = (By.XPATH, "//div[contains(text(), 'Menú')]")




class CriptoLocators:
    div_Cripto = (By.XPATH, "//div[@class='css-146c3p1 r-bvisft' and contains(text(), 'Cripto')]")
    input_Monto = (By.ID, 'i-bitcoin-amount')
    div_Cross = (By.XPATH,"//div[@class='css-175oi2r r-obd0qt r-6koalj r-17s6mgv']")
    div_SelectorMoneda = (By.XPATH, "(//div[@class='css-175oi2r r-1mlwlqe r-1udh08x r-417010 r-6zzn7w r-q1j0wu'])[2]")
    @staticmethod
    def div_CriptoType(crypto_value):
        """Retorna localizador formateado según valor ingresado"""
        XPATH_TEMPLATE = "//div[@class='css-146c3p1 r-dnmrzs r-1udh08x r-1udbk01 r-3s2u2q r-1iln25a r-bvisft r-1khnkhu r-1joea0r' and contains(text(),'{crypto_value}')]"
        # Formatea la cadena e inserta el valor
        dynamic_xpath = XPATH_TEMPLATE.format(crypto_value=crypto_value)
        # Retorna localizador formateado
        return (By.XPATH, dynamic_xpath)