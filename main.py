import requests
API_BASE_URL = 'https://last-airbender-api.fly.dev/'

class DadosPersonagens:
    url_api = API_BASE_URL
    url_api_characters = f'{API_BASE_URL}api/v1/characters'
    
    def __init__(self):
        self.data = self.totalData()

    def totalData(self):
        response = requests.get('https://last-airbender-api.fly.dev/api/v1/characters')
        data = response.json()
        return data
