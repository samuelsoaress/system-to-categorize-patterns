import _thread
from automatizador import sem_classe, hoteis, materiais_construcao, cosmeticos, locacao_automovel, farmacia, academia, supermercado, passagens_aereas, fast_food, restaurante
from automatizador import main

def filho(dados):
    dados = main(dados)
    return dados

def principal(dados):
    thread.start_new_thread(filho, (dados,))
    return dados