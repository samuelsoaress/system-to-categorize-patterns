from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', titulo='Suba seu Dataset')


app.run(debug=True)