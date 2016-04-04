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
