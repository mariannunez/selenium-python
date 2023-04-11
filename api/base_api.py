import requests


class BaseAPI:
    def __init__(self, base_url):
        self.url = base_url

    def get_request(self, params=""):
        return requests.get(self.url+params)
