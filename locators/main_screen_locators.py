from selenium.webdriver.common.by import By

class ConstructorLocators:
    NAV_BUILDER_LINK = (By.XPATH, "//p[contains(text(),'Конструктор')]")
    NAV_FEED_LINK = (By.XPATH, "//p[contains(text(),'Лента Заказов')]")
    
    FIRST_INGREDIENT_IMAGE = (By.XPATH, "//a[contains(@class, 'BurgerIngredient_ingredient')]//img")
    INGREDIENT_COUNTER = (By.XPATH, ".//p[contains(@class, 'counter_counter__num')]")
    BASKET_DROP_ZONE = (By.XPATH, "//ul[contains(@class, 'BurgerConstructor_basket')]")
    
    MODAL_OVERLAY = (By.XPATH, "//h2[text()='Детали ингредиента']")
    MODAL_CLOSE_BUTTON = (By.XPATH, "//button[contains(@class, 'Modal_modal__close_modified__')]")
    
    SUBMIT_ORDER_BUTTON = (By.XPATH, "//button[contains(text(),'Оформить заказ')]")
    ORDER_NUMBER_VALUE = (By.XPATH, "//h2[contains(@class, 'Modal_modal__title')]")

