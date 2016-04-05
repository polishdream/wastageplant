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

class Cin(db.Model):
        __tablename__ = 'Cin'
        id = db.Column('id',db.Integer, primary_key = True)
        timestamp = db.Column('timestamp', db.Text)
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

        def __init__(self,timestamp,si,snd,snh,sno,so,ss,xa,xh,xi,xnd,xp,xs):
                self.timestamp = timestamp
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

class C1(db.Model):
	__tablename__ = 'C1'
	id = db.Column('id',db.Integer, primary_key = True)
	timestamp = db.Column('timestamp', db.Text)
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

        def __init__(self,timestamp,si,snd,snh,sno,so,ss,xa,xh,xi,xnd,xp,xs):
                self.timestamp = timestamp
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
        __tablename__ = 'C2'
        id = db.Column('id',db.Integer, primary_key = True)
        timestamp = db.Column('timestamp', db.Text)
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

        def __init__(self,timestamp,si,snd,snh,sno,so,ss,xa,xh,xi,xnd,xp,xs):
                self.timestamp = timestamp
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

class BioParams(db.Model):
	__tablename__ = 'bioParams'
	id = db.Column('id',db.Integer, primary_key = True)
	timetsamp = db.Column('timestamp',db.Text)
	ya = db.Column('ya',db.Float)
	yh = db.Column('yh',db.Float)
	fp = db.Column('fp',db.Float)
	ixb = db.Column('ixb',db.Float)
	ixp = db.Column('ixp',db.Float)
	mih = db.Column('mih',db.Float)
	ks = db.Column('ks',db.Float)
	koh = db.Column('koh',db.Float)
	kno = db.Column('kno',db.Float)
	bh = db.Column('bh',db.Float)
	ng = db.Column('ng',db.Float)
	nh = db.Column('nh',db.Float)
	kh = db.Column('kh',db.Float)
	kx = db.Column('kx',db.Float)
	mia = db.Column('mia',db.Float)
	knh = db.Column('knh',db.Float)
	ba = db.Column('ba',db.Float)
	koa = db.Column('koa',db.Float)
	ka = db.Column('ka',db.Float)
	sosat = db.Column('sosat',db.Float)

	def __init__(self,timetsamp, ya, yh, fp, ixb, ixp, mih, ks, koh, kno, bh, ng, nh, kh, kx, mia, knh, ba, koa, ka, sosat):
		self.timetsamp = timetsamp 
		self.ya = ya
		self.yh = yh
		self.fp = fp
		self.ixb = ixb
		self.ixp = ixp
		self.mih = mih
		self.ks = ks
		self.koh = koh
		self.kno = kno
		self.bh = bh
		self.ng = ng
		self.nh = nh
		self.kh = kh
		self.kx = kx
		self.mia = mia
		self.knh = knh
		self.ba = ba
		self.koa = koa
		self.ka = ka
		self.sosat = sosat

class Settler(db.Model):
        __tablename__ = 'settler'
        id = db.Column('id',db.Integer, primary_key = True)
        timetsamp = db.Column('timestamp',db.Text)
        x1 = db.Column('x1',db.Float)
        x2 = db.Column('x2',db.Float)
        x3 = db.Column('x3',db.Float)
        x4 = db.Column('x4',db.Float)
        x5 = db.Column('x5',db.Float)
        x6 = db.Column('x6',db.Float)
        x7 = db.Column('x7',db.Float)
        x8 = db.Column('x8',db.Float)
        x9 = db.Column('x9',db.Float)
        x10 = db.Column('x10',db.Float)
	
	def __init__(self, timestamp, x1, x2, x3, x4, x5, x6, x7, x8, x9, x10):
		self.timestamp = timestamp
		self.x1 = x1
		self.x2 = x2
		self.x3 = x3
		self.x4 = x4
		self.x5 = x5
		self.x6 = x6
		self.x7 = x7
		self.x8 = x8
		self.x9 = x9
		self.x10 = x10

class SettlerParams(db.Model):
        __tablename__ = 'settlerParams'
        id = db.Column('id',db.Integer, primary_key = True)
        timetsamp = db.Column('timestamp',db.Text)
        v10 = db.Column('v10',db.Float)
        v0 = db.Column('v0',db.Float)
        rh = db.Column('rh',db.Float)
        rp = db.Column('rp',db.Float)
        fns = db.Column('fns',db.Float)

        def __init__(self, timestamp, v10, v0, rh, rp, fns):
                self.timestamp = timestamp
                self.v10 = v10
                self.v0 = v0
                self.rh = rh
                self.rp = rp
                self.fns = fns
