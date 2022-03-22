from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import BasketPageLocators
    
class BasketPage(BasePage):
    def should_not_be_item_in_basket(self): 
        assert self.is_not_element_present(*BasketPageLocators.ITEM_BASKET), \
            "The product is in the basket, but should not"
            
    def should_be_empty_basket_message(self):
        assert self.there_is_text_about_an_empty_basket(*BasketPageLocators.EMPTY_BASKET), \
            "Message about empty busket doesn't present"
    
    def there_is_text_about_an_empty_basket(self, how, what):
        basket_empty_language = ["O carrinho está vazio.",
                                "La seva cistella està buida.",
                                "Cosul tau este gol.",
                                "Ваш кошик пустий.",
                                "장바구니가 비었습니다.",
                                "Sua cesta está vazia.",
                                "Ваша корзина пуста",
                                "Il tuo carrello è vuoto.",
                                "Το καλάθι σας είναι άδειο.",
                                "Je winkelmand is leeg",
                                "سلة التسوق فارغة",
                                "Twój koszyk jest pusty.",
                                "Váš košík je prázdný.",
                                "Ihr Warenkorb ist leer.",
                                "Váš košík je prázdny",
                                "Din indkøbskurv er tom.",
                                "Votre panier est vide.",
                                "Your basket is empty.",
                                "Korisi on tyhjä",
                                "Tu carrito esta vacío."]
        basket_empty_message = self.browser.find_element(how, what,).text
        result=False
        for el in basket_empty_language:
            if el in basket_empty_message:
                result = True
        return result    
            