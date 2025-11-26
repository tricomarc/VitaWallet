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

    @property
    def div_SelectorMoneda(self):
        return CriptoLocators.div_SelectorMoneda

    
    def div_CriptoType(self, crypto_value):
        return CriptoLocators.div_CriptoType(crypto_value)

    def intercambioCripto(self, crypto_type):
        self.click(self.div_Cripto, 10)
        self.click(self.div_Cross, 10)
        self.wait_for_visibility(self.input_Monto, 10)
        self.type_text(self.input_Monto, '10000')
        self.click(self.div_SelectorMoneda, 10)
        self.wait_for_visibility(self.input_Monto, 10)  
        self.click(self.div_CriptoType(crypto_type), 10)
        self.click(self.div_Cross, 10)