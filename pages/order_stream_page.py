import allure
from pages.base_page import BasePage
from locators.order_stream_locators import OrderStreamLocators

class BurgerOrderStreamPage(BasePage):
    @allure.step("Получение общего числа выполненных заказов")
    def get_total_orders(self):
        return self.get_element_text(OrderStreamLocators.TOTAL_COUNTER)

    @allure.step("Получение числа выполненных заказов за сегодня")
    def get_today_orders(self):
        return self.get_element_text(OrderStreamLocators.TODAY_COUNTER)

    @allure.step("Получение списка номеров заказов в работе")
    def get_in_progress_numbers(self):
        elements = self.find_elements_with_waiting(OrderStreamLocators.IN_PROGRESS_ORDERS)
        return [el.text for el in elements]


