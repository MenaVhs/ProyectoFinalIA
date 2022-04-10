import requests

class GetModel:
    def get_model_by_url(url):
        response = requests.get(url)
        if response.status_code != 200:
            return 'error'
        return response.content