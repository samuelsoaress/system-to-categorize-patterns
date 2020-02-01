import pandas as pd


#Função que procura os padrões e altera
def mape(palavras, dados, categoria):
    for palavra in palavras:
        for linha in dados.index:
            if (dados.loc[linha, 'COD_COMPUTADOR'] == 11) or (dados.loc[linha, 'COD_COMPUTADOR'] == 10):
                estabelecimento = dados.loc[linha,'NOME_ESTABELECIMENTO']
                if palavra in estabelecimento:
                    dados.loc[linha, 'COD_COMPUTADOR'] = categoria
            else:
                continue
    return dados


#Função que tranforma palavras no arquivo txt em uma lista de palavras
def arquivo_lista(arquivo):
    palavras = []
    for linha in arquivo:
        linha = linha.strip()
        linha = linha.upper()
        palavras.append(linha)
    return palavras

    
def sem_classe(dados, categoria=10):
    arquivo = open('Palavras_Chaves/sem_classe.txt', "r")
    palavras = arquivo_lista(arquivo)
    data = mape(palavras, dados, categoria)
    return data


def hoteis(dados,categoria=0):
    arquivo = open('Palavras_Chaves/hoteis.txt', "r")
    palavras = arquivo_lista(arquivo)
    data = mape(palavras, dados, categoria)
    return data


def materiais_construcao(dados,categoria=6):
    arquivo = open('Palavras_Chaves/materiais_construcao.txt', "r")
    palavras = arquivo_lista(arquivo)
    data = mape(palavras, dados, categoria)
    return data


def cosmeticos(dados,categoria=4):
    arquivo = open('Palavras_Chaves/cosmeticos.txt', "r")
    palavras = arquivo_lista(arquivo)
    data = mape(palavras, dados, categoria)
    return data


def locacao_automovel(dados,categoria=1):
    arquivo = open('Palavras_Chaves/locacao_automovel.txt', "r")
    palavras = arquivo_lista(arquivo)
    data = mape(palavras, dados, categoria)
    return data


def farmacia(dados,categoria=3):
    arquivo = open('Palavras_Chaves/farmacia.txt', "r")
    palavras = arquivo_lista(arquivo)
    data = mape(palavras, dados, categoria)
    return data


def academia(dados,categoria=9):
    arquivo = open('Palavras_Chaves/academia.txt', "r")
    palavras = arquivo_lista(arquivo)
    data = mape(palavras, dados, categoria)
    return data


def supermercado(dados,categoria=5):
    arquivo = open('Palavras_Chaves/supermercado.txt', "r")
    palavras = arquivo_lista(arquivo)
    data = mape(palavras, dados, categoria)
    return data


def passagens_aereas(dados, categoria=2):
    arquivo = open('Palavras_Chaves/passagens_aereas.txt', "r")
    palavras = arquivo_lista(arquivo)
    data = mape(palavras, dados, categoria)
    return data


def fast_food(dados, categoria=8):
    arquivo = open('Palavras_Chaves/fast_food.txt', "r")
    palavras = arquivo_lista(arquivo)
    data = mape(palavras, dados, categoria)
    return data


def restaurante(dados, categoria=7):
    arquivo = open('Palavras_Chaves/restaurante.txt', "r")
    palavras = arquivo_lista(arquivo)
    data = mape(palavras, dados, categoria)
    return data

def main(dados):
    dados = sem_classe(dados)
    dados = hoteis(dados)
    dados = materiais_construcao(dados)
    dados = cosmeticos(dados)
    dados = locacao_automovel(dados)
    dados = farmacia(dados)
    dados = academia(dados)
    dados = supermercado(dados)
    dados = passagens_aereas(dados)
    dados = fast_food(dados)
    dados = restaurante(dados)
    return dados