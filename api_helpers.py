import requests
from data import StellarUrls

class StellarApiWorker:
    @classmethod
    def register_account(cls, payload):
        return requests.post(StellarUrls.API_REGISTER, json=payload)
        
    @classmethod
    def wipe_account(cls, token):
        headers = {"Authorization": token}
        return requests.delete(StellarUrls.API_USER_MODIFICATION, headers=headers)