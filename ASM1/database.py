import sqlite3 as sq
import datetime


def connect(path): #path - string
	global cur
	global conn
	try:
		conn = sq.connect(path)
		cur = conn.cursor()
	except:
		print 'nie udalo sie polaczyc z baza.'
	else:
		print 'Polaczono z baza.'

def insert(table, record): #nazwa tabeli, rekord danych (moze byc string => (parametry))
	cur.execute('INSERT INTO ' + table + ' (timestamp,qin,qir,qr,kla,so,sno,snd,snh,ss,si,xh,xa,xs,xnd,xp,xi) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)', record)

def insertSettler(table,x):
	cur.execute('INSERT INTO ' + table + ' (timestamp, x1, x2, x3, x4, x5, x6, x7, x8, x9, x10) VALUES (?,?,?,?,?,?,?,?,?,?,?)', (datetime.datetime.now(),x[0],x[1],x[2],x[3],x[4],x[5],x[6],x[7],x[8],x[9]))

def stop():
	cur.execute('UPDATE flags SET start=0,stop=1,refresh=0')

def selectFraction(table,fraction):
	cur.execute('SELECT ' + fraction + ' FROM ' + table)
	return cur.fetchall()

def selectFraction(table,fraction,id):
	cur.execute('SELECT ' + fraction + ' FROM ' + table + ' WHERE id = ' + id)
	return cur.fetchone()[0]

def selectLast(table,column):
	cur.execute('SELECT ' + column + ' FROM ' + table + ' WHERE id = (SELECT MAX(id) FROM ' + table + ')')
	return cur.fetchone()[0]

def commitChanges():
	conn.commit()

def closeConn():
	conn.close()

def delFirst(table):
	cur.execute('DELETE FROM ' + table + ' WHERE id = (SELECT MIN(id) FROM ' + table + ')')
#			select * from C1 where id = (select MAX(id) from C1);
#			delete from C1 where id = (select MIN(id) from C1)

def clearDb():
	print 'Czyszczenie bazy'
        cur.execute('DELETE FROM C1')
        cur.execute("DELETE FROM sqlite_sequence WHERE name = 'C1'")
        cur.execute('DELETE FROM C2')
        cur.execute("DELETE FROM sqlite_sequence WHERE name = 'C2'")
        cur.execute('DELETE FROM C3')
        cur.execute("DELETE FROM sqlite_sequence WHERE name = 'C3'")
        cur.execute('DELETE FROM C4')
        cur.execute("DELETE FROM sqlite_sequence WHERE name = 'C4'")

        cur.execute('DELETE FROM C5')
        cur.execute("DELETE FROM sqlite_sequence WHERE name = 'C5'")

        cur.execute('DELETE FROM internal_recycle')
        cur.execute("DELETE FROM sqlite_sequence WHERE name = 'internal_recycle'")

        cur.execute('DELETE FROM external_recycle')
        cur.execute("DELETE FROM sqlite_sequence WHERE name = 'external_recycle'")

	cur.execute('DELETE FROM settler')
        cur.execute("DELETE FROM sqlite_sequence WHERE name = 'settler'")
	print 'baza jest pusta'

def vacuumDb():
	cur.execute('VACUUM')
