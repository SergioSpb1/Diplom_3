import allure
from pages.base_page import BasePage
from locators.main_screen_locators import ConstructorLocators

class BurgerConstructorPage(BasePage):
    @allure.step("Переход на вкладку Конструктор")
    def navigate_to_builder(self):
        self.click_via_js(ConstructorLocators.NAV_BUILDER_LINK)

    @allure.step("Переход на вкладку Лента заказов")
    def navigate_to_order_stream(self):
        self.click_via_js(ConstructorLocators.NAV_FEED_LINK)

    @allure.step("Клик по карточке первого ингредиента")
    def open_ingredient_details(self):
        self.click_via_js(ConstructorLocators.FIRST_INGREDIENT_IMAGE)

    @allure.step("Проверка видимости модального окна")
    def is_ingredient_modal_visible(self):
        return self.is_element_displayed(ConstructorLocators.MODAL_OVERLAY)

    @allure.step("Закрытие модального окна")
    def close_ingredient_modal(self):
        self.click_via_js(ConstructorLocators.MODAL_CLOSE_BUTTON)

    @allure.step("Получение значения счетчика ингредиента")
    def get_counter_value(self):
        return self.get_element_text(ConstructorLocators.INGREDIENT_COUNTER)

    @allure.step("Перетаскивание ингредиента в корзину")
    def drag_ingredient_to_basket(self):
        self.drag_and_drop_via_js(
            ConstructorLocators.FIRST_INGREDIENT_IMAGE,
            ConstructorLocators.BASKET_DROP_ZONE
        )

    @allure.step("Нажатие на кнопку оформления заказа")
    def submit_order(self):
        self.click_via_js(ConstructorLocators.SUBMIT_ORDER_BUTTON)

    @allure.step("Ожидание закрытия модального окна")
    def wait_until_modal_disappears(self):
        return self.wait_for_element_invisibility(ConstructorLocators.MODAL_OVERLAY)

    @allure.step("Ожидание появления номера заказа в модальном окне")
    def get_generated_order_number(self):
        self.wait.until(
            lambda driver: (
                len(driver.find_element(*ConstructorLocators.ORDER_NUMBER_VALUE).text.strip()) > 0 
                and driver.find_element(*ConstructorLocators.ORDER_NUMBER_VALUE).text.strip() != "9999"
            )
        )
        return self.get_element_text(ConstructorLocators.ORDER_NUMBER_VALUE)

    @allure.step("Ожидание полного исчезновения окна заказа")
    def wait_until_order_modal_disappears(self):
        return self.wait_for_element_invisibility(ConstructorLocators.ORDER_NUMBER_VALUE)
        
    @allure.step("Принудительное закрытие окна заказа через JS")
    def close_order_modal_via_js(self):
        self.click_via_js(ConstructorLocators.MODAL_CLOSE_BUTTON)
