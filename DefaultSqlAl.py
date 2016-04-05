from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////media/sdcard/default.db'
dbDef = SQLAlchemy(app)

class DefaultParams(dbDef.Model):
        __tablename__ = 'params'
        id = dbDef.Column('id',dbDef.Integer, primary_key = True)
        tsim = dbDef.Column('tsim',dbDef.Float)
        timestamp = dbDef.Column('timestamp',dbDef.Text)
        qin = dbDef.Column('qin',dbDef.Float)
        qw = dbDef.Column('qw',dbDef.Float)
        qir = dbDef.Column('qir',dbDef.Float)
        qr = dbDef.Column('qr',dbDef.Float)
        kla1 = dbDef.Column('kla1',dbDef.Float)
        kla2 = dbDef.Column('kla2',dbDef.Float)
        kla3 = dbDef.Column('kla3',dbDef.Float)
        kla4 = dbDef.Column('kla4',dbDef.Float)
        kla5 = dbDef.Column('kla5',dbDef.Float)

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

class DefaultCin(dbDef.Model):
        __tablename__ = 'Cin'
        id = dbDef.Column('id',dbDef.Integer, primary_key = True)
        timestamp = dbDef.Column('timestamp', dbDef.Text)
        si = dbDef.Column('si', dbDef.Float)
        snd = dbDef.Column('snd', dbDef.Float)
        snh = dbDef.Column('snh', dbDef.Float)
        sno = dbDef.Column('sno', dbDef.Float)
        so = dbDef.Column('so', dbDef.Float)
        ss = dbDef.Column('ss', dbDef.Float)
        xa = dbDef.Column('xa', dbDef.Float)
        xh = dbDef.Column('xh', dbDef.Float)
        xi = dbDef.Column('xi', dbDef.Float)
        xnd = dbDef.Column('xnd', dbDef.Float)
        xp = dbDef.Column('xp', dbDef.Float)
        xs = dbDef.Column('xs', dbDef.Float)

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

class DefaultC1(dbDef.Model):
        __tablename__ = 'C1'
        id = dbDef.Column('id',dbDef.Integer, primary_key = True)
        timestamp = dbDef.Column('timestamp', dbDef.Text)
        si = dbDef.Column('si', dbDef.Float)
        snd = dbDef.Column('snd', dbDef.Float)
        snh = dbDef.Column('snh', dbDef.Float)
        sno = dbDef.Column('sno', dbDef.Float)
        so = dbDef.Column('so', dbDef.Float)
        ss = dbDef.Column('ss', dbDef.Float)
        xa = dbDef.Column('xa', dbDef.Float)
        xh = dbDef.Column('xh', dbDef.Float)
        xi = dbDef.Column('xi', dbDef.Float)
        xnd = dbDef.Column('xnd', dbDef.Float)
        xp = dbDef.Column('xp', dbDef.Float)
        xs = dbDef.Column('xs', dbDef.Float)

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

class DefaultBioParams(dbDef.Model):
        __tablename__ = 'bioParams'
        id = dbDef.Column('id',dbDef.Integer, primary_key = True)
        timetsamp = dbDef.Column('timestamp',dbDef.Text)
        ya = dbDef.Column('ya',dbDef.Float)
        yh = dbDef.Column('yh',dbDef.Float)
        fp = dbDef.Column('fp',dbDef.Float)
        ixb = dbDef.Column('ixb',dbDef.Float)
        ixp = dbDef.Column('ixp',dbDef.Float)
        mih = dbDef.Column('mih',dbDef.Float)
        ks = dbDef.Column('ks',dbDef.Float)
        koh = dbDef.Column('koh',dbDef.Float)
        kno = dbDef.Column('kno',dbDef.Float)
        bh = dbDef.Column('bh',dbDef.Float)
        ng = dbDef.Column('ng',dbDef.Float)
        nh = dbDef.Column('nh',dbDef.Float)
        kh = dbDef.Column('kh',dbDef.Float)
        kx = dbDef.Column('kx',dbDef.Float)
        mia = dbDef.Column('mia',dbDef.Float)
        knh = dbDef.Column('knh',dbDef.Float)
        ba = dbDef.Column('ba',dbDef.Float)
        koa = dbDef.Column('koa',dbDef.Float)
        ka = dbDef.Column('ka',dbDef.Float)
        sosat = dbDef.Column('sosat',dbDef.Float)

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

class DefaultSettler(dbDef.Model):
        __tablename__ = 'settler'
        id = dbDef.Column('id',dbDef.Integer, primary_key = True)
        timetsamp = dbDef.Column('timestamp',dbDef.Text)
        x1 = dbDef.Column('x1',dbDef.Float)
        x2 = dbDef.Column('x2',dbDef.Float)
        x3 = dbDef.Column('x3',dbDef.Float)
        x4 = dbDef.Column('x4',dbDef.Float)
        x5 = dbDef.Column('x5',dbDef.Float)
        x6 = dbDef.Column('x6',dbDef.Float)
        x7 = dbDef.Column('x7',dbDef.Float)
        x8 = dbDef.Column('x8',dbDef.Float)
        x9 = dbDef.Column('x9',dbDef.Float)
        x10 = dbDef.Column('x10',dbDef.Float)

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

class DefaultSettlerParams(dbDef.Model):
        __tablename__ = 'settlerParams'
        id = dbDef.Column('id',dbDef.Integer, primary_key = True)
        timetsamp = dbDef.Column('timestamp',dbDef.Text)
        v10 = dbDef.Column('v10',dbDef.Float)
        v0 = dbDef.Column('v0',dbDef.Float)
        rh = dbDef.Column('rh',dbDef.Float)
        rp = dbDef.Column('rp',dbDef.Float)
        fns = dbDef.Column('fns',dbDef.Float)

        def __init__(self, timestamp, v10, v0, rh, rp, fns):
                self.timestamp = timestamp
                self.v10 = v10
                self.v0 = v0
                self.rh = rh
                self.rp = rp
                self.fns = fns
