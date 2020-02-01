from flask import Flask, render_template, request, redirect, flash, send_from_directory, url_for
import os, time

app = Flask(__name__)

app.config['UPLOAD_PATH'] = os.path.dirname(os.path.abspath(__file__)) + '/uploads'

nome_df = ""

@app.route('/')
def index():
    return render_template('index.html', titulo='Suba seu Dataset')

@app.route('/upload',methods=['POST'])
def upload():
    arquivo = request.files['arquivo']
    upload_path = app.config['UPLOAD_PATH']
    arquivo.save(f'{upload_path}/{arquivo.filename}')
    #nome_df = arquivo.filename
    return redirect(url_for('index'))
app.run(debug=True)