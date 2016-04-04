import database as db

db.connect('/Users/Mateusz/Desktop/beaglebone/projekt/baza.db')
db.cur.execute('delete from params')
db.cur.execute("delete from sqlite_sequence where name = 'params'")
db.commitChanges()
db.closeConn()
