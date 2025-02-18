import requests
from deep_translator import GoogleTranslator

class DadosPersonagens:
    api_base_url = 'https://last-airbender-api.fly.dev/'
    url_api_characters = f'{api_base_url}api/v1/characters'
    
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
                self.names.append('Without Name')

    affiliations = []    
    def filterAffiliation(self):
        for character in self.data:
            try:
                self.affiliations.append(character["affiliation"])
            except KeyError:    
                self.affiliations.append('Without affiliations')
    
    def translateAffiliation(self):
        if len(self.affiliations) == 0:
            raise "Não existem dados para serem traduzidos, execute o método filterAffiliation primero"
        
        listAffiliationTranslates = []
        for affiliation in self.affiliations:
            name_translate = self.translator.translate(affiliation)
            listAffiliationTranslates.append(name_translate)
        return listAffiliationTranslates
    
    def listCharacters(self):
        if len(self.names) == 0:
            self.filterNames()
        listAffiliation = self.translateAffiliation()
        nameAndAffiliation = list(zip(self.names, listAffiliation))
        return print(nameAndAffiliation)
        