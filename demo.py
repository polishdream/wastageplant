from flask import Flask, g, Markup, render_template, redirect, request, url_for
from sqlAl import db, Params, BioParams, Cin, C1, C2, C3, C4, C5, Settler, SettlerParams
from DefaultSqlAl import DefaultParams, DefaultBioParams, DefaultCin, DefaultC1, DefaultSettler, DefaultSettlerParams
from werkzeug import secure_filename
from sqlalchemy import desc
from sqlalchemy.exc import SQLAlchemyError
import sqlite3
import datetime
import os
#from subprocess import Popen, PIPE, STDOUT
import subprocess

app = Flask(__name__)
app.config.from_object(__name__)
app.config.from_envvar('DEMO_SETTINGS', silent=True)
app.debug = True

@app.route('/')
def index():
        return render_template('index.html')

@app.route('/simulation')
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

@app.route('/influent')
def influent():
        f = Cin.query.first()
        params = [dict(si = f.si,
                        snd = f.snd,
                        snh = f.snh,
                        sno = f.sno,
                        so = f.so,
                        ss = f.ss,
                        xa = f.xa,
                        xh = f.xh,
                        xi = f.xi,
                        xnd = f.xnd,
			xp = f.xp,
			xs = f.xs)]

        return render_template('doplyw.html', Params=params)

@app.route('/bioreactor')
def bioreactor():
	f = C1.query.first()
	bf = BioParams.query.first()
        params = [dict(si = f.si,
                        snd = f.snd,
                        snh = f.snh,
                        sno = f.sno,
                        so = f.so,
                        ss = f.ss,
                        xa = f.xa,
                        xh = f.xh,
                        xi = f.xi,
                        xnd = f.xnd,
                        xp = f.xp,
                        xs = f.xs,
                	ya = bf.ya,
                	yh = bf.yh,
                	fp = bf.fp,
                	ixb = bf.ixb,
                	ixp = bf.ixp,
                	mih = bf.mih,
                	ks = bf.ks,
                	koh = bf.koh,
                	kno = bf.kno,
                	bh = bf.bh,
                	ng = bf.ng,
                	nh = bf.nh,
                	kh = bf.kh,
                	kx = bf.kx,
                	mia = bf.mia,
                	knh = bf.knh,
                	ba = bf.ba,
                	koa = bf.koa,
                	ka = bf.ka,
                	sosat = bf.sosat)]
        return render_template('bioParams.html', Params = params)

@app.route('/secondarySettler')
def settler():
	f = Settler.query.first()
        sf = SettlerParams.query.first()
        params = [dict(x1 = f.x1,
			x2 = f.x2,
			x3 = f.x3,
			x4 = f.x4,
			x5 = f.x5,
			x6 = f.x6,
			x7 = f.x7,
			x8 = f.x8,
			x9 = f.x9,
			x10 = f.x10,
			v10 = sf.v10,
			v0 = sf.v0,
			rh = sf.rh,
			rp = sf.rp,
			fns = sf.fns)]

        return render_template('osadParams.html', Params=params)

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
	elif request.form['submit'] == 'Start':
		subprocess.call(["/var/www/demo/ASM1/bioTest.py"])
		#Popen(('/var/www/demo/ASM1/script.py',), stdout=PIPE, stderr=STDOUT)
	#return redirect(url_for('symulacja'))
	return render_template("process.html")

@app.route('/submitInParams', methods=['POST'])
def submitInParams():
        if request.form['inSubmit'] == 'Zapisz':
                dt = datetime.datetime.now()
                record = Cin.query.first()
                record.timestamp = dt
                record.si = request.form['si']
                record.snd = request.form['snd']
                record.snh = request.form['snh']
                record.sno = request.form['sno']
                record.so = request.form['so']
                record.ss = request.form['ss']
                record.xa = request.form['xa']
                record.xh = request.form['xh']
                record.xi = request.form['xi']
                record.xnd = request.form['xnd']
		record.xp = request.form['xp']
		record.xs = request.form['xs']
                db.session.commit()

        elif request.form['inSubmit'] == 'Default':
                defPar = DefaultCin.query.first()
                dt = datetime.datetime.now()
                record = Cin.query.first()
                record.timestamp = dt
                record.snd = defPar.snd
                record.snh = defPar.snh
                record.sno = defPar.sno
                record.so = defPar.so
                record.ss = defPar.ss
                record.xa = defPar.xa
                record.xh = defPar.xh
                record.xi = defPar.xi
                record.xnd = defPar.xnd
		record.xp = defPar.xp
		record.xs = defPar.xs
                db.session.commit()
        return redirect(url_for('influent'))


@app.route('/submitBioParams', methods=['POST'])
def submitBioParams():
        if request.form['bioSubmit'] == 'Zapisz':
                dt = datetime.datetime.now()
                record = C1.query.first()
                record.timestamp = dt
                record.si = request.form['si']
                record.snd = request.form['snd']
                record.snh = request.form['snh']
                record.sno = request.form['sno']
                record.so = request.form['so']
                record.ss = request.form['ss']
                record.xa = request.form['xa']
                record.xh = request.form['xh']
                record.xi = request.form['xi']
                record.xnd = request.form['xnd']
                record.xp = request.form['xp']
                record.xs = request.form['xs']

		record = BioParams.query.first()
                record.timestamp = dt
                record.ya = request.form['ya']
                record.yh = request.form['yh']
                record.fp = request.form['fp']
                record.ixb = request.form['ixb']
                record.ixp = request.form['ixp']
                record.mih = request.form['mih']
                record.ks = request.form['ks']
                record.koh = request.form['koh']
                record.kno = request.form['kno']
                record.bh = request.form['bh']
                record.ng = request.form['ng']
                record.nh = request.form['nh']
		record.kh = request.form['kh']
		record.kx = request.form['kx']
		record.mia = request.form['mia']
		record.knh = request.form['knh']
		record.ba = request.form['ba']
		record.koa = request.form['koa']
		record.ka = request.form['ka']
		record.sosat = request.form['sosat']
                db.session.commit()

        elif request.form['bioSubmit'] == 'Default':
                defPar = DefaultC1.query.first()
                dt = datetime.datetime.now()
                record = C1.query.first()
                record.timestamp = dt
                record.snd = defPar.snd
                record.snh = defPar.snh
                record.sno = defPar.sno
                record.so = defPar.so
                record.ss = defPar.ss
                record.xa = defPar.xa
                record.xh = defPar.xh
                record.xi = defPar.xi
                record.xnd = defPar.xnd
                record.xp = defPar.xp
                record.xs = defPar.xs

		defPar = DefaultBioParams.query.first()
		record = BioParams.query.first()
                record.timestamp = dt
                record.ya = defPar.ya
                record.yh = defPar.yh
                record.fp = defPar.fp
                record.ixb = defPar.ixb
                record.ixp = defPar.ixp
                record.mih = defPar.mih
                record.ks = defPar.ks
                record.koh = defPar.koh
                record.kno = defPar.kno
                record.bh = defPar.bh
                record.ng = defPar.ng
                record.nh = defPar.nh
                record.kh = defPar.kh
                record.kx = defPar.kx
                record.mia = defPar.mia
                record.knh = defPar.knh
                record.ba = defPar.ba
                record.koa = defPar.koa
                record.ka = defPar.ka
                record.sosat = defPar.sosat
                db.session.commit()
        return redirect(url_for('bioreactor'))

@app.route('/submitSetParams', methods=['POST'])
def submitSetParams():
        if request.form['setSubmit'] == 'Zapisz':
                dt = datetime.datetime.now()
                record = Settler.query.first()
                record.timestamp = dt
                record.x1 = request.form['x1']
                record.x2 = request.form['x2']
                record.x3 = request.form['x3']
                record.x4 = request.form['x4']
                record.x5 = request.form['x5']
                record.x6 = request.form['x6']
                record.x7 = request.form['x7']
                record.x8 = request.form['x8']
                record.x9 = request.form['x9']
                record.x10 = request.form['x10']

		record = SettlerParams.query.first()
                record.timestamp = dt
                record.v10 = request.form['v10']
                record.v0 = request.form['v0']
                record.rh = request.form['rh']
                record.rp = request.form['rp']
                record.fns = request.form['fns']
		db.session.commit()
	if request.form['setSubmit'] == 'Reset':
		dt = datetime.datetime.now()
		defPar = DefaultSettler.query.first()
                record = Settler.query.first()
		record.x1 = defPar.x1
                record.x2 = defPar.x2
                record.x3 = defPar.x3
                record.x4 = defPar.x4
                record.x5 = defPar.x5
		record.x6 = defPar.x6
                record.x7 = defPar.x7
                record.x8 = defPar.x8
                record.x9 = defPar.x9
                record.x10 = defPar.x10

		defPar = DefaultSettlerParams.query.first()
		record = SettlerParams.query.first()
		record.v10 = defPar.v10
		record.v0 = defPar.v0
		record.rh = defPar.rh
		record.rp = defPar.rp
		record.fns = defPar.fns
		db.session.commit()
	return redirect(url_for('settler'))

if __name__ == '__main__':
    app.run()
