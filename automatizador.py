import pandas as pd
import pymysql
import os

bd = pymysql.connect(host='localhost',
                                user='root',
                                password='',
                                db='data_note',
                                cursorclass=pymysql.cursors.DictCursor)


cursor = bd.cursor()

#Função que procura os padrões e altera

SQL_CATEGORIA_POR_ID = 'SELECT nome from palavras_chaves where categoria = %s'

def mape(dados):
    categoria = 10
    while categoria >= 0:
        cursor.execute(SQL_CATEGORIA_POR_ID,(categoria,))
        for palavra in cursor.fetchall():
            for linha in dados.index:
                if (dados.loc[linha, 'COD_COMPUTADOR'] == 11) or (dados.loc[linha, 'COD_COMPUTADOR'] == 10)or (dados.loc[linha, 'COD_COMPUTADOR'] == 7):
                    estabelecimento = dados.loc[linha,'NOME_ESTABELECIMENTO']
                    if palavra['nome'] in estabelecimento:
                        dados.loc[linha, 'COD_COMPUTADOR'] = categoria
                else:
                    continue
        categoria -= 1
    return dados


def categorize(dados):
    dados = mape(dados)
    return dados


def categorizador(dados):
    dados['COD_COMPUTADOR'] = 11
    dados = categorize(dados)
    return dados