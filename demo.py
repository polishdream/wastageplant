from flask import Flask, g, Markup, render_template, redirect, request, url_for
from sqlAl import Params, Flags, db, C1, C2, C3, C4, C5
from sAluser import CC1, CC2, CC3, CC4, CC5, dbu
from werkzeug import secure_filename
from sqlalchemy import desc
from sqlalchemy.exc import SQLAlchemyError
import sqlite3
import time
import os
import subprocess

app = Flask(__name__)
app.config.from_object(__name__)
app.config.from_envvar('DEMO_SETTINGS', silent=True)
app.debug = True

@app.route('/')
def index():
        return render_template('index.html')

@app.route('/symulacja')
def symulacja():
	f = Params.query.first()
	params = [dict(tsim = f.tsim,
			qin = f.qin,
			qw = f.qw,
			qir = f.qir,
			qr = f.qr,
			kla1 = f.kla1,
			kla2 = f.kla2,
			kla3 = f.kla3,
			kla4 = f.kla4,
			kla5 = f.kla5)]
			
        return render_template('params.html', Params=params)

@app.route('/symulacja/doplyw')
def influent():
        return render_template('doplyw.html')

@app.route('/symulacja/bioreaktor')
def bioreactor():
        return render_template('bioParams.html')

@app.route('/symulacja/osadnik')
def settler():
        return render_template('osadParams.html')

if __name__ == '__main__':
    app.run()
