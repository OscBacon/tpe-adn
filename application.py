# -*- coding: utf-8 -*-
import os
from flask import render_template
from flask import Flask
from flask import url_for
from flask import request
from flask import redirect
from dna import DNA2Text
from dna import Text2DNA

app = Flask(__name__)

@app.route('/')
@app.route('/index.html')
def index():
    return render_template('index.html', page=1, title="Accueil")

@app.route('/introduction.html', methods=['GET','POST'])
def introduction():
    text = None
    dna = None
    processed_text = None
    processed_dna = None
    if request.method == 'POST':
        try:
            request.form['text']
        except KeyError:
            pass
        else:
            text = request.form['text']
            processed_text = Text2DNA.t2dna(text)
        try:
            request.form['dna']
        except KeyError:
            pass
        else:
            dna = request.form['dna']
            processed_dna = DNA2Text.dna2t(dna)
    return render_template('introduction.html', text=text, processed_text=processed_text, dna=dna, processed_dna=processed_dna, page=2, title="Introduction")

@app.route('/entretien.html')
def entretien():
    return render_template('entretien.html', page=3, title="Entretien")

@app.route('/stockage.html')
def stockage():
    return render_template('stockage.html', page=4, title="Stockage d'information")

@app.route('/math.html')
def math():
    return render_template('math.html', page=5, title="Math / SVT")

@app.route('/t2dna.html')
def text2dna():
    return render_template('t2dna.html', page=6, title="Information a ADN")

@app.route('/dna2t.html')
def dna2text():
    return render_template('dna2t.html', page=7, title="ADN a Information")

@app.route('/conclusion.html')
def conclusion():
    return render_template('conclusion.html', page=8, title="Conclusion")

@app.route('/bibliographie.html')
def bibliographie():
    return render_template('bibliographie.html', page=9, title="Bibliographie")

@app.route('/t2dna_src.html')
def t2dna_src():
    return render_template('t2dna_src.html', source=True, title="Code de conversion de texte vers ADN")

@app.route('/dna2t_src.html')
def dna2t_src():
    return render_template('dna2t_src.html', source=True, title="Code de conversion d'ADN vers texte")

if __name__ == '__main__':
    app.run(port = int(os.environ.get('PORT', 33507)))
