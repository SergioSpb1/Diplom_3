import allure
from data import StellarUrls
from pages.main_screen_page import BurgerConstructorPage

class TestMainDashboardFeatures:

    @allure.title("Проверка успешного перехода в раздел Конструктор")
    def test_navigate_to_constructor_success(self, driver):
        constructor_page = BurgerConstructorPage(driver)
        constructor_page.open_url(StellarUrls.ORDER_STREAM_PAGE)
        constructor_page.navigate_to_builder()

        assert StellarUrls.BASE_URL in driver.current_url

    @allure.title("Проверка успешного перехода в раздел Лента заказов")
    def test_navigate_to_order_stream_success(self, driver):
        constructor_page = BurgerConstructorPage(driver)
        constructor_page.open_url(StellarUrls.BASE_URL)
        constructor_page.navigate_to_order_stream()

        assert StellarUrls.ORDER_STREAM_PAGE in driver.current_url

    @allure.title("Проверка открытия модального окна с деталями ингредиента")
    def test_open_ingredient_details_popup(self, driver):
        constructor_page = BurgerConstructorPage(driver)
        constructor_page.open_url(StellarUrls.BASE_URL)
        constructor_page.open_ingredient_details()

        assert constructor_page.is_ingredient_modal_visible() is True

    @allure.title("Проверка закрытия модального окна ингредиента по клику на крестик")
    def test_close_ingredient_details_popup(self, driver):
        constructor_page = BurgerConstructorPage(driver)
        constructor_page.open_url(StellarUrls.BASE_URL)
        constructor_page.open_ingredient_details()
        constructor_page.close_ingredient_modal()

        assert constructor_page.wait_until_modal_disappears() is True

    @allure.title("Проверка увеличения счетчика ингредиента при его переносе в корзину")
    def test_ingredient_counter_increments_on_drop(self, driver):
        constructor_page = BurgerConstructorPage(driver)
        constructor_page.open_url(StellarUrls.BASE_URL)
        initial_count = int(constructor_page.get_counter_value())
        constructor_page.drag_ingredient_to_basket()
        updated_count = int(constructor_page.get_counter_value())
        
        assert updated_count > initial_count
