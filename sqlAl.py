from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////media/sdcard/userParams.db'
db = SQLAlchemy(app)

class Params(db.Model):
	__tablename__ = 'params'
	id = db.Column('id',db.Integer, primary_key = True)
	tsim = db.Column('tsim',db.Float)
	timestamp = db.Column('timestamp',db.Text)
	qin = db.Column('qin',db.Float)
	qw = db.Column('qw',db.Float)
	qir = db.Column('qir',db.Float)
	qr = db.Column('qr',db.Float)
	kla1 = db.Column('kla1',db.Float)
	kla2 = db.Column('kla2',db.Float)
	kla3 = db.Column('kla3',db.Float)
	kla4 = db.Column('kla4',db.Float)
	kla5 = db.Column('kla5',db.Float)

	def __init__(self,timestamp,tsim,qin,qir,qr,qe,qw,sosat,kla3,kla4,kla5):
		self.timestamp = timestamp
		self.tsim = tsim
		self.qin = qin
		self.qw = qw
		self.qir = qir
		self.qr = qr
		self.kla1 = kla1
		self.kla2 = kla2
		self.kla3 = kla3
		self.kla4 = kla4
		self.kla5 = kla5

class C1(db.Model):
	__tablename__ = 'c1'
	id = db.Column('id',db.Integer, primary_key = True)
	timestamp = db.Column('timestamp', db.Text)
	qin = db.Column('qin', db.Float)
	qir = db.Column('qir', db.Float)
	qr = db.Column('qr', db.Float)
	kla = db.Column('kla', db.Float)
	si = db.Column('si', db.Float)
	snd = db.Column('snd', db.Float)
	snh = db.Column('snh', db.Float)
	sno = db.Column('sno', db.Float)
	so = db.Column('so', db.Float)
	ss = db.Column('ss', db.Float)
	xa = db.Column('xa', db.Float)
	xh = db.Column('xh', db.Float)
	xi = db.Column('xi', db.Float)
	xnd = db.Column('xnd', db.Float)
	xp = db.Column('xp', db.Float)
	xs = db.Column('xs', db.Float)

        def __init__(self,timestamp,qin,qir,qr,kla,si,snd,snh,sno,so,ss,xa,xh,xi,xnd,xp,xs):
                self.timestamp = timestamp 
                self.qin = qin
                self.qir = qir
                self.qr = qr
                self.kla = kla 
                self.si = si
                self.snd = snd
                self.snh = snh
                self.sno = sno
                self.so = so
		self.ss = ss
		self.xa = xa
		self.xh = xh
		self.xi = xi
		self.xnd = xnd
		self.xp = xp
		self.xs = xs

class C2(db.Model):
        __tablename__ = 'c2'
        id = db.Column('id',db.Integer, primary_key = True)
        timestamp = db.Column('timestamp', db.Text)
        qin = db.Column('qin', db.Float)
        qir = db.Column('qir', db.Float)
        qr = db.Column('qr', db.Float)
        kla = db.Column('kla', db.Float)
        si = db.Column('si', db.Float)
        snd = db.Column('snd', db.Float)
        snh = db.Column('snh', db.Float)
        sno = db.Column('sno', db.Float)
        so = db.Column('so', db.Float)
        ss = db.Column('ss', db.Float)
        xa = db.Column('xa', db.Float)
        xh = db.Column('xh', db.Float)
        xi = db.Column('xi', db.Float)
        xnd = db.Column('xnd', db.Float)
        xp = db.Column('xp', db.Float)
        xs = db.Column('xs', db.Float)

        def __init__(self,timestamp,qin,qir,qr,kla,si,snd,snh,sno,so,ss,xa,xh,xi,xnd,xp,xs):
                self.timestamp = timestamp
                self.qin = qin
                self.qir = qir
                self.qr = qr
                self.kla = kla
                self.si = si
                self.snd = snd
                self.snh = snh
                self.sno = sno
                self.so = so
                self.ss = ss
                self.xa = xa
                self.xh = xh
                self.xi = xi
                self.xnd = xnd
                self.xp = xp
                self.xs = xs

class C3(db.Model):
        __tablename__ = 'c3'
        id = db.Column('id',db.Integer, primary_key = True)
        timestamp = db.Column('timestamp', db.Text)
        qin = db.Column('qin', db.Float)
        qir = db.Column('qir', db.Float)
        qr = db.Column('qr', db.Float)
        kla = db.Column('kla', db.Float)
        si = db.Column('si', db.Float)
        snd = db.Column('snd', db.Float)
        snh = db.Column('snh', db.Float)
        sno = db.Column('sno', db.Float)
        so = db.Column('so', db.Float)
        ss = db.Column('ss', db.Float)
        xa = db.Column('xa', db.Float)
        xh = db.Column('xh', db.Float)
        xi = db.Column('xi', db.Float)
        xnd = db.Column('xnd', db.Float)
        xp = db.Column('xp', db.Float)
        xs = db.Column('xs', db.Float)

        def __init__(self,timestamp,qin,qir,qr,kla,si,snd,snh,sno,so,ss,xa,xh,xi,xnd,xp,xs):
                self.timestamp = timestamp
                self.qin = qin
                self.qir = qir
                self.qr = qr
                self.kla = kla
                self.si = si
                self.snd = snd
                self.snh = snh
                self.sno = sno
                self.so = so
                self.ss = ss
                self.xa = xa
                self.xh = xh
                self.xi = xi
                self.xnd = xnd
                self.xp = xp
                self.xs = xs

class C4(db.Model):
        __tablename__ = 'c4'
        id = db.Column('id',db.Integer, primary_key = True)
        timestamp = db.Column('timestamp', db.Text)
        qin = db.Column('qin', db.Float)
        qir = db.Column('qir', db.Float)
        qr = db.Column('qr', db.Float)
        kla = db.Column('kla', db.Float)
        si = db.Column('si', db.Float)
        snd = db.Column('snd', db.Float)
        snh = db.Column('snh', db.Float)
        sno = db.Column('sno', db.Float)
        so = db.Column('so', db.Float)
        ss = db.Column('ss', db.Float)
        xa = db.Column('xa', db.Float)
        xh = db.Column('xh', db.Float)
        xi = db.Column('xi', db.Float)
        xnd = db.Column('xnd', db.Float)
        xp = db.Column('xp', db.Float)
        xs = db.Column('xs', db.Float)

        def __init__(self,timestamp,qin,qir,qr,kla,si,snd,snh,sno,so,ss,xa,xh,xi,xnd,xp,xs):
                self.timestamp = timestamp
                self.qin = qin
                self.qir = qir
                self.qr = qr
                self.kla = kla
                self.si = si
                self.snd = snd
                self.snh = snh
                self.sno = sno
                self.so = so
                self.ss = ss
                self.xa = xa
                self.xh = xh
                self.xi = xi
                self.xnd = xnd
                self.xp = xp
                self.xs = xs

class C5(db.Model):
        __tablename__ = 'c5'
        id = db.Column('id',db.Integer, primary_key = True)
        timestamp = db.Column('timestamp', db.Text)
        qin = db.Column('qin', db.Float)
        qir = db.Column('qir', db.Float)
        qr = db.Column('qr', db.Float)
        kla = db.Column('kla', db.Float)
        si = db.Column('si', db.Float)
        snd = db.Column('snd', db.Float)
        snh = db.Column('snh', db.Float)
        sno = db.Column('sno', db.Float)
        so = db.Column('so', db.Float)
        ss = db.Column('ss', db.Float)
        xa = db.Column('xa', db.Float)
        xh = db.Column('xh', db.Float)
        xi = db.Column('xi', db.Float)
        xnd = db.Column('xnd', db.Float)
        xp = db.Column('xp', db.Float)
        xs = db.Column('xs', db.Float)

        def __init__(self,timestamp,qin,qir,qr,kla,si,snd,snh,sno,so,ss,xa,xh,xi,xnd,xp,xs):
                self.timestamp = timestamp
                self.qin = qin
                self.qir = qir
                self.qr = qr
                self.kla = kla
                self.si = si
                self.snd = snd
                self.snh = snh
                self.sno = sno
                self.so = so
                self.ss = ss
                self.xa = xa
                self.xh = xh
                self.xi = xi
                self.xnd = xnd
                self.xp = xp
                self.xs = xs

class Flags(db.Model):
	__tablename__ = 'flags'
	id = db.Column('id',db.Integer, primary_key = True)
	start = db.Column('start',db.Integer)
	stop = db.Column('stop',db.Integer)
	refresh = db.Column('refresh',db.Integer)

	def __init__(self,start,stop):
		self.start = start
		self.stop = stop
