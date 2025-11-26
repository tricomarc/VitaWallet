import time
from locators.locators import CriptoLocators
from .base_page import BasePage

class CriptoPage(BasePage):

    @property
    def div_Cripto(self):
        return CriptoLocators.div_Cripto
    
    @property
    def input_Monto(self):
        return CriptoLocators.input_Monto

    @property
    def div_Cross(self):
        return CriptoLocators.div_Cross


    def div_SelectorMoneda(self, posicion):
        return CriptoLocators.div_SelectorMoneda(posicion)

    
    def div_CriptoType(self, crypto_value):
        return CriptoLocators.div_CriptoType(crypto_value)

    def intercambioCripto(self, moneda, cripto):
        self.click(self.div_Cripto, 10)
        self.click(self.div_Cross, 10)
        self.click(self.div_SelectorMoneda(1), 10)
        self.wait_for_visibility(self.div_CriptoType(moneda), 10)  
        self.click(self.div_CriptoType(moneda), 10)
        self.wait_for_visibility(self.input_Monto, 10)
        self.click(self.input_Monto, 10)
        self.type_text(self.input_Monto, '10000')
        self.click(self.div_SelectorMoneda(2), 10)
        self.wait_for_visibility(self.div_CriptoType(cripto), 10)  
        self.click(self.div_CriptoType(cripto), 10)
        self.wait_for_visibility(self.input_Monto, 10)