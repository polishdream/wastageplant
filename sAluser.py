from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////var/www/demo/user.db'
dbu = SQLAlchemy(app)

class inflow(dbu.Model):
        __tablename__ = 'inflow'
        id = dbu.Column('id',dbu.Integer, primary_key = True)
        tsim = dbu.Column('tsim',dbu.Float)
        qin = dbu.Column('qin',dbu.Float)
        qir = dbu.Column('qir',dbu.Float)
        qr = dbu.Column('qr',dbu.Float)
        qe = dbu.Column('qe',dbu.Float)
        qw = dbu.Column('qw',dbu.Float)
        sosat = dbu.Column('sosat',dbu.Float)
        kla3 = dbu.Column('kla3',dbu.Float)
        kla4 = dbu.Column('kla4',dbu.Float)
        kla5 = dbu.Column('kla5',dbu.Float)

        def __init__(self,tsim,qin,qir,qr,qe,qw,sosat,kla3,kla4,kla5):
                self.tsim = tsim
                self.qin = qin
                self.qir = qir
                self.qr = qr
                self.qe = qe
                self.qw = qw
                self.sosat = sosat
                self.kla3 = kla3
                self.kla4 = kla4
                self.kla5 = kla5

class CC1(dbu.Model):
        __tablename__ = 'cc1'
        id = dbu.Column('id',dbu.Integer, primary_key = True)
        si = dbu.Column('si', dbu.Float)
        snd = dbu.Column('snd', dbu.Float)
        snh = dbu.Column('snh', dbu.Float)
        sno = dbu.Column('sno', dbu.Float)
        so = dbu.Column('so', dbu.Float)
        ss = dbu.Column('ss', dbu.Float)
        xa = dbu.Column('xa', dbu.Float)
        xh = dbu.Column('xh', dbu.Float)
        xi = dbu.Column('xi', dbu.Float)
        xnd = dbu.Column('xnd', dbu.Float)
        xp = dbu.Column('xp', dbu.Float)
        xs = dbu.Column('xs', dbu.Float)

        def __init__(self,si,snd,snh,sno,so,ss,xa,xh,xi,xnd,xp,xs):
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

class CC2(dbu.Model):
        __tablename__ = 'cc2'
        id = dbu.Column('id',dbu.Integer, primary_key = True)
        si = dbu.Column('si', dbu.Float)
        snd = dbu.Column('snd', dbu.Float)
        snh = dbu.Column('snh', dbu.Float)
        sno = dbu.Column('sno', dbu.Float)
        so = dbu.Column('so', dbu.Float)
        ss = dbu.Column('ss', dbu.Float)
        xa = dbu.Column('xa', dbu.Float)
        xh = dbu.Column('xh', dbu.Float)
        xi = dbu.Column('xi', dbu.Float)
        xnd = dbu.Column('xnd', dbu.Float)
        xp = dbu.Column('xp', dbu.Float)
        xs = dbu.Column('xs', dbu.Float)

        def __init__(self,si,snd,snh,sno,so,ss,xa,xh,xi,xnd,xp,xs):
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

class CC3(dbu.Model):
        __tablename__ = 'cc3'
        id = dbu.Column('id',dbu.Integer, primary_key = True)
        si = dbu.Column('si', dbu.Float)
        snd = dbu.Column('snd', dbu.Float)
        snh = dbu.Column('snh', dbu.Float)
        sno = dbu.Column('sno', dbu.Float)
        so = dbu.Column('so', dbu.Float)
        ss = dbu.Column('ss', dbu.Float)
        xa = dbu.Column('xa', dbu.Float)
        xh = dbu.Column('xh', dbu.Float)
        xi = dbu.Column('xi', dbu.Float)
        xnd = dbu.Column('xnd', dbu.Float)
        xp = dbu.Column('xp', dbu.Float)
        xs = dbu.Column('xs', dbu.Float)

        def __init__(self,si,snd,snh,sno,so,ss,xa,xh,xi,xnd,xp,xs):
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

class CC4(dbu.Model):
        __tablename__ = 'cc4'
        id = dbu.Column('id',dbu.Integer, primary_key = True)
        si = dbu.Column('si', dbu.Float)
        snd = dbu.Column('snd', dbu.Float)
        snh = dbu.Column('snh', dbu.Float)
        sno = dbu.Column('sno', dbu.Float)
        so = dbu.Column('so', dbu.Float)
        ss = dbu.Column('ss', dbu.Float)
        xa = dbu.Column('xa', dbu.Float)
        xh = dbu.Column('xh', dbu.Float)
        xi = dbu.Column('xi', dbu.Float)
        xnd = dbu.Column('xnd', dbu.Float)
        xp = dbu.Column('xp', dbu.Float)
        xs = dbu.Column('xs', dbu.Float)

        def __init__(self,si,snd,snh,sno,so,ss,xa,xh,xi,xnd,xp,xs):
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

class CC5(dbu.Model):
        __tablename__ = 'cc5'
        id = dbu.Column('id',dbu.Integer, primary_key = True)
        si = dbu.Column('si', dbu.Float)
        snd = dbu.Column('snd', dbu.Float)
        snh = dbu.Column('snh', dbu.Float)
        sno = dbu.Column('sno', dbu.Float)
        so = dbu.Column('so', dbu.Float)
        ss = dbu.Column('ss', dbu.Float)
        xa = dbu.Column('xa', dbu.Float)
        xh = dbu.Column('xh', dbu.Float)
        xi = dbu.Column('xi', dbu.Float)
        xnd = dbu.Column('xnd', dbu.Float)
        xp = dbu.Column('xp', dbu.Float)
        xs = dbu.Column('xs', dbu.Float)

        def __init__(self,si,snd,snh,sno,so,ss,xa,xh,xi,xnd,xp,xs):
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






