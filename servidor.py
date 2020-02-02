from flask import Flask, render_template, request, redirect, flash, send_from_directory, url_for
from automatizador import sem_classe, hoteis, materiais_construcao, cosmeticos, locacao_automovel, farmacia, academia, supermercado, passagens_aereas, fast_food, restaurante
from automatizador import main
import os, time
import pandas as pd
import _thread


app = Flask(__name__)

app.config['UPLOAD_PATH'] = os.path.dirname(os.path.abspath(__file__)) + '/uploads'

nome_df = ""

dados = pd.DataFrame()

def le_arquivo(nome_df):
    dados = pd.read_csv("{}/{}".format(app.config['UPLOAD_PATH'],nome_df))
    return dados


def exporta(dados):
    dados.to_csv("{}/{}".format(app.config['UPLOAD_PATH'],'DATA_SET_CORRIGIDO.csv'),index=False)
    

def filho(dados):
    dados = main(dados)
    return dados

def principal(dados,metodo):
    _thread.start_new_thread(metodo, (dados,))
    return dados

def categorizador(dados):
    dados['COD_COMPUTADOR'] = 11
    dados = filho(dados)
    total = len(dados)
    resto = len(dados[dados['COD_COMPUTADOR'] == 11])
    categorizado = total - resto
    exporta(dados)

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
    categorizador(dados)
    dados.to_csv("{}/{}".format(app.config['UPLOAD_PATH'],'DATA_SET_TESTE.csv'))
    return redirect(url_for('download'))


@app.route('/download')
def download():
    categorizador(dados)
    return render_template('download.html',titulo='Baixe seu dataset')
app.run(debug=True)