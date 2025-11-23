from selenium.webdriver.common.by import By

class LoginLocators:
    INICIAR_SESION = (By.XPATH, "//*[@id='root']/div/div/div/div/div/div/div[2]/div/div[2]/div/div")
    input_Correo = (By.ID, "i-login-email")
    input_Clave = (By.ID, "i-login-password")
    checkBox = (By.XPATH, "//*[@id='recaptcha-anchor']/div[1]")
    button_Ingresar = (By.ID, "b-login-submit")
    label_Username = (By.XPATH, "//div[contains(normalize-space(), 'Hola, Test')]")
    div_Menu = (By.XPATH, "//div[contains(text(), 'Menú')]")