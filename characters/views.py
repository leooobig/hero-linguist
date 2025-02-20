from django.shortcuts import render
from .models import Personagem
from django.core.paginator import Paginator

# Create your views here.
def index(request):
    personagens = Personagem.objects.all()
    #Tratamento dos dados
    for personagem in personagens:
        if personagem.inimigos:
            personagem.inimigos_str = personagem.aliados.replace("[",'').replace("]",'').replace("'",'')
        else:
            personagem.inimigos_str = 'Sem inimigos'
    for personagem in personagens:
        if personagem.aliados:
            personagem.aliados_str = personagem.aliados.replace("[",'').replace("]",'').replace("'",'')
        else:
            personagem.aliados_str = 'Sem aliados'
    
    
    paginator = Paginator(personagens, 5)
    page_num = request.GET.get('page')
    page = paginator.get_page(page_num)

    context = {'page':page}
    return render(request,'characters/index.html', context)