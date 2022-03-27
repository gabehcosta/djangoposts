from django.shortcuts import redirect, render
from .models import Postagem

def index(request):
    return render(request, 'index.html')

def postagens(request):
    lista_postagens = Postagem.objects.order_by('-data_postagem').all()
    return render(request, 'postagens.html', {'postagens' : lista_postagens})

def nova_postagem(request):
    return render(request, 'nova-postagem.html')

def publicar_postagem(request):
    nome_autor = request.POST['nome-autor'] 
    titulo_postagem = request.POST['titulo-post']
    texto_postagem = request.POST['texto-post']

    postagem = Postagem.objects.create(
        nome_autor=nome_autor, titulo_postagem=titulo_postagem, texto_postagem=texto_postagem
        )
    
    return redirect('postagens')

def edicao_postagem(request, id_postagem):
    postagem = Postagem.objects.get(id_postagem=id_postagem)
    return render(request, 'edicao-postagem.html', {'postagem':postagem})

def editar_postagem(request):
    id_postagem = request.POST['id-postagem']
    nome_autor = request.POST['nome-autor']
    titulo_postagem = request.POST['titulo-post']
    texto_postagem = request.POST['texto-post']

    postagem = Postagem.objects.get(id_postagem=id_postagem)
    postagem.titulo_postagem = f'{titulo_postagem} - (EDITADO)'
    postagem.texto_postagem = texto_postagem
    postagem.save()

    return redirect('postagens')

def excluir_postagem(request, id_postagem):
    postagem = Postagem.objects.get(id_postagem=id_postagem)
    postagem.delete()

    return redirect('postagens')