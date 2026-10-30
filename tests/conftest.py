import pytest
import uuid
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from data import StellarUrls

@pytest.fixture(params=["chrome", "firefox"])
def driver(request):
    if request.param == "chrome":
        options = webdriver.ChromeOptions()
        service = ChromeService(ChromeDriverManager().install())
        browser = webdriver.Chrome(service=service, options=options)
    elif request.param == "firefox":
        options = webdriver.FirefoxOptions()
        browser = webdriver.Firefox(options=options)

    yield browser
    browser.quit()


class StellarApiWorker:
    @classmethod
    def register_account(cls, payload):
        return requests.post(StellarUrls.API_REGISTER, json=payload)
        
    @classmethod
    def wipe_account(cls, token):
        headers = {"Authorization": token}
        return requests.delete(StellarUrls.API_USER_MODIFICATION, headers=headers)


@pytest.fixture
def create_unique_user():
    unique_id = uuid.uuid4().hex[:6]
    
    user_payload = {
        "email": f"astro_tester_{unique_id}@yandex.ru",
        "password": f"Pwd_{unique_id}",
        "name": f"Astro-{unique_id}"
    }
    
    response = StellarApiWorker.register_account(user_payload)
    response_data = response.json()
    
    auth_token = response_data.get("accessToken")
    user_payload["accessToken"] = auth_token
    
    yield user_payload
    
    if auth_token:
        StellarApiWorker.wipe_account(auth_token)
