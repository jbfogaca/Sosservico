from django.urls import path
from .views import *

urlpatterns = [
    path('', listagem),
    path('listagem/', listagem),
    path('listagem/<int:id>/', selecao),
    path('consulta/', consulta),
    path('ordenacao/<str:campo>/', ordenacao),
    path('insercao/', insercao),
    path('salvar_insercao/', salvar_insercao),
    path('edicao/<int:id>/', edicao),
    path('salvar_edicao/', salvar_edicao),
    path('delecao/<int:id>/', delecao),
    path('salvar_delecao/', salvar_delecao),
]
