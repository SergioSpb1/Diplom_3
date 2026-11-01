import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    TIMEOUT_FOR_ELEMENT_VISIBILITY_SEC = 11

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, self.TIMEOUT_FOR_ELEMENT_VISIBILITY_SEC)

    @allure.step("Открытие веб-страницы по адресу: {url}")
    def open_url(self, url):
        self.driver.get(url)

    @allure.step("Ожидание появления элемента с локатором: {locator}")
    def find_element_with_waiting(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    @allure.step("Ожидание появления списка элементов с локатором: {locator}")
    def find_elements_with_waiting(self, locator):
        return self.wait.until(EC.presence_of_all_elements_located(locator))

    @allure.step("Ожидание исчезновения элемента с локатором: {locator}")
    def wait_for_element_invisibility(self, locator):
        self.wait.until(EC.invisibility_of_element_located(locator))
        return True

    @allure.step("Получение текстового содержимого элемента: {locator}")
    def get_element_text(self, locator):
        element = self.find_element_with_waiting(locator)
        return element.text

    @allure.step("Проверка отображения элемента на экране: {locator}")
    def is_element_displayed(self, locator):
        return self.find_element_with_waiting(locator).is_displayed()

    @allure.step("Перетаскивание элемента {source_locator} в {target_locator} через JS")
    def drag_and_drop_via_js(self, source_locator, target_locator):
        #код взят из сообщения П. Акулова в qa-fs-python_study_M7 4.08.2026
        self.find_element_with_waiting(source_locator)
        self.find_element_with_waiting(target_locator)

        element_from = self.driver.find_element(*source_locator)
        element_to = self.driver.find_element(*target_locator)

        self.driver.execute_script("""
            var source = arguments[0];
            var target = arguments[1];

            var evt = document.createEvent("DragEvent");
            evt.initMouseEvent("dragstart", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
            source.dispatchEvent(evt);

            evt = document.createEvent("DragEvent");
            evt.initMouseEvent("dragenter", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
            target.dispatchEvent(evt);

            evt = document.createEvent("DragEvent");
            evt.initMouseEvent("dragover", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
            target.dispatchEvent(evt);

            evt = document.createEvent("DragEvent");
            evt.initMouseEvent("drop", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
            target.dispatchEvent(evt);

            evt = document.createEvent("DragEvent");
            evt.initMouseEvent("dragend", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
            source.dispatchEvent(evt);
        """, element_from, element_to)

    @allure.step("Принудительный клик по элементу через JS: {locator}")
    def click_via_js(self, locator):
        element = self.find_element_with_waiting(locator)
        self.driver.execute_script("arguments[0].click();", element)

    @allure.step("Получение текущего URL-адреса страницы")
    def get_current_url(self):
        return self.driver.current_url


