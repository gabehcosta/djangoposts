from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('postagens', views.postagens, name='postagens'),
    path('nova-postagem', views.nova_postagem, name='nova-postagem'),
    path('publicar-postagem', views.publicar_postagem),
    path('edicao-postagem/<id_postagem>', views.edicao_postagem),
    path('editar-postagem/', views.editar_postagem),
    path('excluir-postagem/<id_postagem>', views.excluir_postagem)
]