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
                self.affiliations.append('Sem afiliados')
    
    enemies = []    
    def filterEnemies(self):
        for character in self.data:
            try:
                if len(character["enemies"]) == 0:
                    character["enemies"] = ["Sem inimigos"]
                    self.enemies.append(character["enemies"])
                    continue
                self.enemies.append(character["enemies"])
            except KeyError:    
                self.enemies.append('Sem inimigos')
    
    allies = []    
    def filterAllies(self):
        for character in self.data:
            try:
                if len(character["allies"]) == 0:
                    character["allies"] = ["Sem aliados"]
                    self.allies.append(character["allies"])
                    continue
                self.allies.append(character["allies"])
            except KeyError:    
                self.allies.append('Sem aliados')
    
    def translateAffiliation(self):
        if len(self.affiliations) == 0:
            raise "Não existem dados para serem traduzidos, execute o método filterAffiliation primero"
        
        listAffiliationTranslates = []
        for affiliation in self.affiliations:
            name_translate = self.translator.translate(affiliation)
            listAffiliationTranslates.append(name_translate)
        return listAffiliationTranslates
    
    def listCharacters(self):
        self.filterNames()
        self.filterEnemies()
        self.filterAllies()
        affilation_translate = self.translateAffiliation()
        nameAndAffiliation = list(zip(self.names, affilation_translate, self.allies, self.enemies))
        return nameAndAffiliation
        