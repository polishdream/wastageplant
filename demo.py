from flask import Flask, g, Markup, render_template, redirect, request, url_for
from sqlAl import Params, db, C1, C2, C3, C4, C5
from DefaultSqlAl import DefaultParams
from werkzeug import secure_filename
from sqlalchemy import desc
from sqlalchemy.exc import SQLAlchemyError
import sqlite3
import datetime
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

@app.route('/submitParams', methods=['POST'])
def submitParams():
	if request.form['submit'] == 'Zapisz':
		dt = datetime.datetime.now()
		record = Params.query.first()
		record.timestamp = dt
		record.tsim = request.form['tsim']
		record.qin = request.form['qin']
		record.qw = request.form['qw']
		record.qir = request.form['qir']
		record.qr = request.form['qr']
		record.kla1 = request.form['kla1']
                record.kla2 = request.form['kla2']
		record.kla3 = request.form['kla3']
		record.kla4 = request.form['kla4']
		record.kla5 = request.form['kla5']
		db.session.commit()

	elif request.form['submit'] == 'Default':
		defPar = DefaultParams.query.first()

                dt = datetime.datetime.now()
                record = Params.query.first()
                record.timestamp = dt
                record.tsim = defPar.tsim
                record.qin = defPar.qin
                record.qw = defPar.qw
                record.qir = defPar.qir
                record.qr = defPar.qr
                record.kla1 = defPar.kla1
                record.kla2 = defPar.kla2
                record.kla3 = defPar.kla3
                record.kla4 = defPar.kla4
                record.kla5 = defPar.kla5
                db.session.commit()
	return redirect(url_for('symulacja'))

if __name__ == '__main__':
    app.run()
