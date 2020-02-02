from flask import Flask, render_template, request, redirect, flash, send_from_directory, url_for
from automatizador import sem_classe, hoteis, materiais_construcao, cosmeticos, locacao_automovel, farmacia, academia, supermercado, passagens_aereas, fast_food, restaurante
from automatizador import main
import os, time
import pandas as pd

class Categoria:
    def __init__(self, total, resto, categorizado):
        self.total = total 
        self.resto = resto
        self.categorizado = categorizado

    

app = Flask(__name__)

app.config['UPLOAD_PATH'] = os.path.dirname(os.path.abspath(__file__)) + '/uploads'

nome_df = ""

dados = pd.DataFrame()
lista = []

def le_arquivo(nome_df):
    dados = pd.read_csv("{}/{}".format(app.config['UPLOAD_PATH'],nome_df))
    return dados


def categorize(dados):
    dados = main(dados)
    return dados


def categorizador(dados):
    dados['COD_COMPUTADOR'] = 11
    dados = categorize(dados)
    return dados

@app.route('/')
def index():
    return render_template('index.html', titulo='Suba seu Dataset')


@app.route('/upload',methods=['POST'])
def upload():
    arquivo = request.files['arquivo']
    upload_path = app.config['UPLOAD_PATH']
    arquivo.save(f'{upload_path}/{arquivo.filename}')
    nome_df = arquivo.filename
    dados = le_arquivo(nome_df)
    dados = categorizador(dados)
    total = len(dados)
    resto = len(dados[dados['COD_COMPUTADOR'] == 11])
    categorizado = total - resto
    lista.append(total)
    lista.append(resto)
    lista.append(categorizado)
    dados.to_csv("{}/{}".format(app.config['UPLOAD_PATH'],'DATA.csv'), index=False)
    return redirect(url_for('download'))


@app.route('/download')
def download():
    return render_template('download.html',titulo='Baixe seu dataset', categorias=lista)

@app.route('/uploads/<nome_arquivo>')
def data(nome_arquivo):
    return send_from_directory('uploads', nome_arquivo)

app.run(debug=True)