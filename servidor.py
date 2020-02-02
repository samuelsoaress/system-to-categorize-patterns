from flask import Flask, render_template, request, redirect, flash, send_from_directory, url_for
from automatizador import mape, le_arquivo, categorizador,
import os, time
import pandas as pd
import pymysql

bd = pymysql.connect(host='localhost',
                                user='root',
                                password='',
                                db='data_note',
                                cursorclass=pymysql.cursors.DictCursor)


cursor = bd.cursor()

SQL_CRIA = 'INSERT into palavras_chaves (nome, categoria) values (%s,%s)'
    

app = Flask(__name__)

app.config['UPLOAD_PATH'] = os.path.dirname(os.path.abspath(__file__)) + '/uploads'

nome_df = ""

dados = pd.DataFrame()
lista = []

# Routes

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

@app.route('/cadastro')
def cadastro():
    return render_template('cadastro.html', titulo='Cadastre uma nova Keyword')


@app.route('/cadastro',methods=['POST'])
def criar():
    nome = request.form['nome']
    categoria = request.form['categoria']
    cursor.execute(SQL_CRIA,(nome,categoria))
    bd.commit()
    return redirect(url_for('cadastro'))




@app.route('/download')
def download():
    return render_template('download.html',titulo='Baixe seu dataset', categorias=lista)


@app.route('/uploads/<nome_arquivo>')
def data(nome_arquivo):
    return send_from_directory('uploads', nome_arquivo)

app.run(debug=True)