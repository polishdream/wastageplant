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

