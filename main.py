import requests
from deep_translator import GoogleTranslator
API_BASE_URL = 'https://last-airbender-api.fly.dev/'

class DadosPersonagens:
    url_api = API_BASE_URL
    url_api_characters = f'{API_BASE_URL}api/v1/characters'
    
    def __init__(self):
        self.data = self.pushData()
        self.translator = GoogleTranslator(source='en', target='pt')


    def pushData(self):
        response = requests.get('https://last-airbender-api.fly.dev/api/v1/characters')
        data = response.json()
        return data
    
    names = []
    def filterNames(self):
        for chacacter in self.data:
            try:
                self.names.append(chacacter['name'])
            except KeyError:
                self.names.append(chacacter['Without Name'])
                
    affiliations = []    
    def filterAffiliation(self):
        for character in self.data:
            try:
                self.affiliations.append(character["affiliation"])
            except KeyError:    
                self.affiliations.append('Without affiliations')

    def translateData(self):
        ...

chacacters = DadosPersonagens()
chacacters.filterAffiliation()
print(chacacters.affiliations)