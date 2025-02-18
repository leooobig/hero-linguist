from django.shortcuts import render


# Create your views here.
def index(request):
    from dados import DadosPersonagens

    characters = DadosPersonagens()
    characters.filterAffiliation()
    personagens = characters.listCharacters()
    context = {'personagem' : personagens}

    return render(request,'characters/index.html', context)