import sqlite3 as sq

#c = False
#try:
#	conn = sq.connect('/var/www/demo/baza.db')
#	cur = conn.cursor()
#	c = True
#except:
#	print 'nie udalo sie polaczyc z baza.'
#else:
#	print 'Polaczono z baza.'

#if c:

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
cur.execute('VACUUM')
conn.commit()

print 'baza jest pusta'
#conn.close()
