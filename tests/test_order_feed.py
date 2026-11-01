
import allure
from data import StellarUrls
from pages.login_page import BurgerLoginPage
from pages.main_screen_page import BurgerConstructorPage
from pages.order_stream_page import BurgerOrderStreamPage

class TestOrderStream:

    @allure.title("Проверка увеличения общего счетчика заказов при создании нового заказа")
    def test_total_orders_increments_after_order(self, driver, create_unique_user):
        login_page = BurgerLoginPage(driver)
        constructor_page = BurgerConstructorPage(driver)
        stream_page = BurgerOrderStreamPage(driver)
        
        stream_page.open_url(StellarUrls.ORDER_STREAM_PAGE)
        initial_total = int(stream_page.get_total_orders())
        
        login_page.open_url(StellarUrls.LOGIN_PAGE)
        login_page.login_with_credentials(create_unique_user["email"], create_unique_user["password"])
        
        constructor_page.drag_ingredient_to_basket()
        constructor_page.submit_order()
        
        constructor_page.get_generated_order_number() 
        constructor_page.close_order_modal_via_js()
        constructor_page.wait_until_order_modal_disappears()
        
        constructor_page.navigate_to_order_stream()
        updated_total = int(stream_page.get_total_orders())
        
        assert updated_total > initial_total 

    @allure.title("Проверка увеличения суточного счетчика заказов при создании нового заказа")
    def test_today_orders_counter_increments_after_order(self, driver, create_unique_user):
        login_page = BurgerLoginPage(driver)
        constructor_page = BurgerConstructorPage(driver)
        stream_page = BurgerOrderStreamPage(driver)
        
        stream_page.open_url(StellarUrls.ORDER_STREAM_PAGE)
        initial_today = int(stream_page.get_today_orders())
        
        login_page.open_url(StellarUrls.LOGIN_PAGE)
        login_page.login_with_credentials(create_unique_user["email"], create_unique_user["password"])
        
        constructor_page.drag_ingredient_to_basket()
        constructor_page.submit_order()
        
        constructor_page.get_generated_order_number()
        constructor_page.close_order_modal_via_js()
        constructor_page.wait_until_order_modal_disappears()
        
        constructor_page.navigate_to_order_stream()
        updated_today = int(stream_page.get_today_orders())
        
        assert updated_today > initial_today

    @allure.title("Проверка появления номера нового заказа в блоке 'В работе'")
    def test_number_is_in_work(self, driver, create_unique_user):
        login_page = BurgerLoginPage(driver)
        constructor_page = BurgerConstructorPage(driver)
        stream_page = BurgerOrderStreamPage(driver)
        
        login_page.open_url(StellarUrls.LOGIN_PAGE)
        login_page.login_with_credentials(create_unique_user["email"], create_unique_user["password"])
        
        constructor_page.drag_ingredient_to_basket()
        constructor_page.submit_order()
        
        order_number = constructor_page.get_generated_order_number()
        
        formatted_order_number = str(order_number).zfill(4)
        
        constructor_page.close_order_modal_via_js()
        constructor_page.wait_until_order_modal_disappears()
        constructor_page.navigate_to_order_stream()
        
        orders_in_progress = stream_page.get_in_progress_numbers()
        
        assert formatted_order_number in orders_in_progress


