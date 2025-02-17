from dados import DadosPersonagens

characters = DadosPersonagens()
names = characters.listCharacters()
print(*names)