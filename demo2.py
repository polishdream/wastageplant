# all the imports
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
#MOJE
#import matplotlib
#matplotlib.use('Agg')
#import numpy as np
#import matplotlib.pyplot as plt
#from matplotlib import style
#/MOJE

# MOJE
macDb = 'baza.db' #'/Users/Mateusz/Desktop/beaglebone/projekt/baza.db'
locked = 1
#style.use('fivethirtyeight') # styl wykresu
#fig1 = plt.figure() # figure
# MOJEKONIEC
user = 'user.db'

UPLOAD_FOLDER = '/var/www/demo/ASM1'
ALLOWED_EXTENSIONS = set(['txt', 'csv'])

# create our little application :)
app = Flask(__name__)
app.config.from_object(__name__)
app.config.from_envvar('DEMO_SETTINGS', silent=True)
app.debug = True
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


def allowed_filename(filename):
    return '.' in filename and filename.rsplit('.',1)[1] in ALLOWED_EXTENSIONS


@app.route('/')
def nindex():
	return render_template('nindex.html')


@app.route('/d')
def d():
        return render_template('d.html')


@app.route('/rozpuszczone')
def rozpuszczone():
        return render_template('rozpuszczone.html')


@app.route('/ponizej')
def ponizej():
        return render_template('ponizej.html')


@app.route('/powyzej')
def powyzej():
        return render_template('powyzej.html')


@app.route('/zawieszone')
def zawieszone():
        return render_template('zawieszone.html')


@app.route('/nsymulacja')
def nsymulacja():
        return render_template('nsymulacja.html')


@app.route('/pobierz', methods=['GET', 'POST'])
def pobierz():
    if request.method == 'POST':
        submitted_file = request.files['file']
        if submitted_file and allowed_filename(submitted_file.filename):
            filename = secure_filename(submitted_file.filename)
            submitted_file.save(os.path.join(app.config['UPLOAD_FOLDER'], 'data.txt'))
            #message = Markup("Plik zapisano")
            #flash(message)
            return redirect(url_for('pobierz', filename=filename))

    return render_template('pobierz.html')


@app.route('/wybor')
def wybor():
        return render_template('wybor.html')


@app.route('/doplyw')
def doplyw():
        return render_template('doplyw.html')


@app.route('/k1')
def k1():
    f = CC1.query.order_by(desc(CC1.id)).limit(1)
    if(f.count() > 0):
        par = [dict(id=r.id,
                    si=r.si,
                    snd=r.snd,
		    snh=r.snh,
                    sno=r.sno,
                    so=r.so,
                    ss=r.ss,
                    xa=r.xa,
                    xh=r.xh,
                    xi=r.xi,
                    xnd=r.xnd,
                    xp=r.xp,
		    xs=r.xs) for r in f]
    else:
        par = [dict(si=0.0,
                    snd=0.0,
                    snh=0.0,
                    sno=0.0,
                    so=0.0,
                    ss=0.0,
                    xa=0.0,
                    xh=0.0,
                    xi=0.0,
                    xnd=0.0,
		    xp=0.0,
		    xs=0.0)]
    return render_template('k1.html', Par=par)


@app.route('/k2')
def k2():
    f = CC2.query.order_by(desc(CC2.id)).limit(1)
    if(f.count() > 0):
        par = [dict(id=r.id,
                    si=r.si,
                    snd=r.snd,
                    snh=r.snh,
                    sno=r.sno,
                    so=r.so,
                    ss=r.ss,
                    xa=r.xa,
                    xh=r.xh,
                    xi=r.xi,
                    xnd=r.xnd,
                    xp=r.xp,
                    xs=r.xs) for r in f]
    else:
        par = [dict(si=0.0,
                    snd=0.0,
                    snh=0.0,
                    sno=0.0,
                    so=0.0,
                    ss=0.0,
                    xa=0.0,
                    xh=0.0,
                    xi=0.0,
                    xnd=0.0,
                    xp=0.0,
                    xs=0.0)]
    return render_template('k2.html', Par=par)


@app.route('/k3')
def k3():
    f = CC3.query.order_by(desc(CC3.id)).limit(1)
    if(f.count() > 0):
        par = [dict(id=r.id,
                    si=r.si,
                    snd=r.snd,
                    snh=r.snh,
                    sno=r.sno,
                    so=r.so,
                    ss=r.ss,
                    xa=r.xa,
                    xh=r.xh,
                    xi=r.xi,
                    xnd=r.xnd,
                    xp=r.xp,
                    xs=r.xs) for r in f]
    else:
        par = [dict(si=0.0,
                    snd=0.0,
                    snh=0.0,
                    sno=0.0,
                    so=0.0,
                    ss=0.0,
                    xa=0.0,
                    xh=0.0,
                    xi=0.0,
                    xnd=0.0,
                    xp=0.0,
                    xs=0.0)]
    return render_template('k3.html', Par=par)


@app.route('/k4')
def k4():
    f = CC4.query.order_by(desc(CC4.id)).limit(1)
    if(f.count() > 0):
        par = [dict(id=r.id,
                    si=r.si,
                    snd=r.snd,
                    snh=r.snh,
                    sno=r.sno,
                    so=r.so,
                    ss=r.ss,
                    xa=r.xa,
                    xh=r.xh,
                    xi=r.xi,
                    xnd=r.xnd,
                    xp=r.xp,
                    xs=r.xs) for r in f]
    else:
        par = [dict(si=0.0,
                    snd=0.0,
                    snh=0.0,
                    sno=0.0,
                    so=0.0,
                    ss=0.0,
                    xa=0.0,
                    xh=0.0,
                    xi=0.0,
                    xnd=0.0,
                    xp=0.0,
                    xs=0.0)]
    return render_template('k4.html', Par=par)


@app.route('/k5')
def k5():
    f = CC5.query.order_by(desc(CC5.id)).limit(1)
    if(f.count() > 0):
        par = [dict(id=r.id,
                    si=r.si,
                    snd=r.snd,
                    snh=r.snh,
                    sno=r.sno,
                    so=r.so,
                    ss=r.ss,
                    xa=r.xa,
                    xh=r.xh,
                    xi=r.xi,
                    xnd=r.xnd,
                    xp=r.xp,
                    xs=r.xs) for r in f]
    else:
        par = [dict(si=0.0,
                    snd=0.0,
                    snh=0.0,
                    sno=0.0,
                    so=0.0,
                    ss=0.0,
                    xa=0.0,
                    xh=0.0,
                    xi=0.0,
                    xnd=0.0,
                    xp=0.0,
                    xs=0.0)]
    return render_template('k5.html', Par=par)


@app.route('/so')
def so():
        a = C1.query.filter(C1.id % 200 == 0)  #jakby cos, to ja wiem, ze nie tak mialo byc,
        Data1 = [dict(id=r.id,                      
                     timestamp=r.timestamp,         
                     qir=r.qir,
                     so=r.so) for r in a]
        b = C2.query.filter(C2.id % 200 == 0)  
        Data2 = [dict(id=r.id,                       
                     timestamp=r.timestamp,         
                     qir=r.qir,
                     so=r.so) for r in b]
        c = C3.query.filter(C3.id % 200 == 0)  
        Data3 = [dict(id=r.id,                      
                     timestamp=r.timestamp,        
                     qir=r.qir,
                     so=r.so) for r in c]
        d = C4.query.filter(C4.id % 200 == 0)
        Data4 = [dict(id=r.id,
                     timestamp=r.timestamp,
                     qir=r.qir,
                     so=r.so) for r in d]
        e = C5.query.filter(C5.id % 200 == 0)
        Data5 = [dict(id=r.id,
                     timestamp=r.timestamp,
                     qir=r.qir,
                     so=r.so) for r in e]

        return render_template('so.html', data1=Data1, data2=Data2, data3=Data3, data4=Data4, data5=Data5)


@app.route('/porownaj')
def porownaj():
        a = C1.query.filter(C1.id % 200 == 0)  #jakby cos, to ja wiem, ze nie tak mialo byc,
        Data1 = [dict(id=r.id,
                     timestamp=r.timestamp,
                     qir=r.qir,
                     so=r.so) for r in a]
        b = C2.query.filter(C2.id % 200 == 0)
        Data2 = [dict(id=r.id,
                     timestamp=r.timestamp,
                     qir=r.qir,
                     so=r.so) for r in b]
        c = C3.query.filter(C3.id % 200 == 0)
        Data3 = [dict(id=r.id,
                     timestamp=r.timestamp,
                     qir=r.qir,
                     so=r.so) for r in c]
        d = C4.query.filter(C4.id % 200 == 0)
        Data4 = [dict(id=r.id,
                     timestamp=r.timestamp,
                     qir=r.qir,
                     so=r.so) for r in d]
        e = C5.query.filter(C5.id % 200 == 0)
        Data5 = [dict(id=r.id,
                     timestamp=r.timestamp,
                     qir=r.qir,
                     so=r.so) for r in e]

        return render_template('porownaj.html', data1=Data1, data2=Data2, data3=Data3, data4=Data4, data5=Data5)


@app.route('/wykres')
def wykres():
#	connect_to_DB = sqlite3.connect(macDb)
#	c=connect_to_DB.cursor()
#	c.execute('SELECT id, qin, qir FROM okon')
#	Data = c.fetchall()
#	connect_to_DB.commit()
#	connect_to_DB.close()
        f = C1.query.filter(C1.timestamp % 3000 == 0) #jakby cos, to ja wiem, ze nie tak mialo byc,
        Data1 = [dict(id=r.id,                       #nie rozgryzlam jeszcze kroku
                    timestamp=r.timestamp,         #a nie chcialam na nim utknac i nic nie miec
                    qir=r.qir,
                    so=r.so) for r in f]

#	f = C1.query.filter(C1.id >=1, C1.id < 100) #jakby cos, to ja wiem, ze nie tak mialo byc,
#	Data = [dict(id=r.id,                       #nie rozgryzlam jeszcze kroku
#		     timestamp=r.timestamp,         #a nie chcialam na nim utknac i nic nie miec
#		     qin=r.qin,
#		     qir=r.qir,
#		     qr=r.qr,
#		     kla=r.kla,
#		     si=r.si,
#		     snd=r.snd,
#		     snh=r.snh,
#		     sno=r.sno,
#		     so=r.so,
#	             ss=r.ss,
#		     xa=r.xa,
#		     xh=r.xh,
#		     xi=r.xi,
#		     xnd=r.xnd,
#		     xp=r.xp,
#		     xs=r.xs) for r in f]
#______________________
#	f = Params.query.filter(Params.id % 2 == 0)
#	Data = [dict(id=r.id,
#                   qin=r.qin,
#                   qir=r.qir,
#                   qr=r.qr,
#                   qe=r.qe,
#                   qw=r.qw,
#                   sosat=r.sosat,
#                   tsim=r.tsim,
#                   kla3=r.kla3,
#                   kla4=r.kla4,
#                   kla5=r.kla5) for r in f]
#______________________________
#	Data = [(1,23,53),(2,34,51),(3,11,34),(4,14,12),(5,32,42)]
	return render_template('wykres.html', data1=Data1)

 
@app.route('/parametry')
def parametry():
    #connect_to_DB = sqlite3.connect(macDb)
    #c = connect_to_DB.cursor()
    #c.execute('SELECT * FROM params WHERE id=(SELECT MAX(id) FROM params)')
    #f = c.fetchall()
    f = Params.query.order_by(desc(Params.id)).limit(1)
    if(f.count() > 0):
        par = [dict(id=r.id,
                    qin=r.qin,
                    qir=r.qir,
                    qr=r.qr,
		    qe=r.qe,
		    qw=r.qw,
                    sosat=r.sosat,
                    tsim=r.tsim,
                    kla3=r.kla3,
                    kla4=r.kla4,
		    kla5=r.kla5) for r in f]
    else:
        par = [dict(qin=0.0,
                    qir=0.0,
                    qr=0.0,
		    qe=0.0,
		    qw=0.0,
                    sosat=0.0,
                    tsim=0.0,
                    kla3=0.0,
		    kla4=0.0,
                    kla5=0.0)]
    #connect_to_DB.close()
    return render_template('parametry.html', Par = par)


@app.route('/wyniki')
def wyniki():
    #connect_to_DB = sqlite3.connect(macDb)
    #c = connect_to_DB.cursor()

    #c.execute('SELECT id, tp, qin, qir, qr, sosat, tsim, cf, kla FROM params')
    f = Params.query.all()
    Pomiary = [dict(id=row.id,
                    qin=row.qin,
                    qir=row.qir,
                    qr=row.qr,
		    qe=row.qe,
		    qw=row.qw,
                    sosat=row.sosat,
                    tsim=row.tsim,
                    kla3=row.kla3,
		    kla4=row.kla4,
                    kla5=row.kla5) for row in f]
    #connect_to_DB.close()
    return render_template('wyniki.html', Pomiary = Pomiary)


@app.route('/add', methods=['POST'])
def add_entry():
#    connect_to_DB = sqlite3.connect(macDb)
#    c = connect_to_DB.cursor()
#    c.execute('INSERT INTO params (tp, qin, qir, qr, sosat, tsim, cf, kla) VALUES (?, ?, ?, ?, ?, ?, ?, ?)',
#              (request.form['tp'], request.form['qin'], request.form['qir'], request.form['qr'],request.form['sosat'],
#               request.form['tsim'], request.form['cf'], request.form['kla']))
#    if request.form['przycisk'] == 'Start':
#        c.execute('UPDATE flags SET start = 1,stop = 0 WHERE id=1')
#    if request.form['przycisk'] == 'Aktualizuj':
#        c.execute('UPDATE flags SET refresh=1 WHERE id=1')
#    connect_to_DB.commit()
#    connect_to_DB.close()
#    flash('Dodano do bazy')
    if request.form['przycisk'] == 'Start':
        #record = Params(tsim=request.form['tsim'], qin=request.form['qin'], qir=request.form['qir'], qr=request.form['qr'], qe=request.form['qe'],
        #                qw=request.form['qw'], sosat=request.form['sosat'], kla3=request.form['kla3'], kla4=request.form['kla4'], kla5=request.form['kla5']) 
        #db.session.add(record)
        #upd = Flags.query.filter_by(id=1).first()
	#upd.start = 1
	#upd.stop = 0
        #db.session.commit()
	subprocess.call(['python','bioTest.py'])
    return redirect(url_for('parametry'))


@app.route('/dodajk1', methods=['POST'])
def dodajk1():
        if request.form['przycisk'] == 'Zapisz':
		record = dbu.session.query(CC1).get(1)
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
                dbu.session.commit()
        return redirect(url_for('k1'))


@app.route('/dodajk2', methods=['POST'])
def dodajk2():
        if request.form['przycisk'] == 'Zapisz':
                record = dbu.session.query(CC2).get(1)
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
                dbu.session.commit()
        return redirect(url_for('k2'))


@app.route('/dodajk3', methods=['POST'])
def dodajk3():
        if request.form['przycisk'] == 'Zapisz':
                record = dbu.session.query(CC3).get(1)
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
                dbu.session.commit()
        return redirect(url_for('k3'))


@app.route('/dodajk4', methods=['POST'])
def dodajk4():
        if request.form['przycisk'] == 'Zapisz':
                record = dbu.session.query(CC4).get(1)
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
                dbu.session.commit()
        return redirect(url_for('k4'))


@app.route('/dodajk5', methods=['POST'])
def dodajk5():
	if request.form['przycisk'] == 'Zapisz':
                record = dbu.session.query(CC5).get(1)
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
                dbu.session.commit()
        return redirect(url_for('k5'))


@app.route('/stop', methods=['POST'])
def stop():
#    connect_to_DB = sqlite3.connect(macDb)
#    c = connect_to_DB.cursor()
#    c.execute('UPDATE flags SET start=0, stop=1 WHERE id=1')
#    connect_to_DB.commit()
#    connect_to_DB.close()
#    flash('Dodano do bazy')
    return redirect(url_for('parametry'))

@app.route('/updateValues', methods=['POST'])
def updateValues():
#    connect_to_DB = sqlite3.connect(macDb)
#    c = connect_to_DB.cursor()
#    c.execute('INSERT INTO params (tp, qin, qir, qr, sosat, tsim, cf, kla) VALUES (?, ?, ?, ?, ?, ?, ?, ?)',
#              (request.form['tp'], request.form['qin'], request.form['qir'], request.form['qr'],request.form['sosat'],
#               request.form['tsim'], request.form['cf'], request.form['kla']))
#    c.execute('UPDATE flags SET refresh=1 WHERE id=1')
#    connect_to_DB.commit()
#    connect_to_DB.close()
#    flash('Dodano do bazy')
    return redirect(url_for('parametry'))

@app.route('/analiza')
def analiza():
    return render_template('analiza.html')

@app.route('/wykres')
def fig():
    return send_file('/Users/Mateusz/Desktop/beaglebone/projekt/wyniki/C5/C5so.png',mimetype='image/png')

if __name__ == '__main__':
    app.run()
