from flask import Flask, render_template, request, redirect, flash, send_from_directory
import os, time

app = Flask(__name__)

app.config['UPLOAD_PATH'] = os.path.dirname(os.path.abspath(__file__)) + '/uploads'

@app.route('/')
def index():
    return render_template('index.html', titulo='Suba seu Dataset')


app.run(debug=True)