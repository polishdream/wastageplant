#=================================================
__author__ = 'Ariel ANTONOWICZ'
__version__ = '14.11.2015'
__contact__ = 'ariel.antonowicz@gmail.com'
#=================================================


import sqlite3
import sys
import hashlib
sqlite_file = '/var/www/app/database/DB_Users.db'    # name of the sqlite database file

# Connecting to the database file
conn = sqlite3.connect(sqlite_file)
c = conn.cursor()

# Add new user

v1 = ''
v2 = ''
v3 = ''
v4 = ''
v5 = ''

print 'Add user script START'
v1 = raw_input('Give me your name: ')
v2 = raw_input('Give me your surname: ')
v3 = raw_input('Give me your nick: ')

v4 = hashlib.md5()
v4.update("Administrator")
v4 = v4.hexdigest()
v5_pass = raw_input('Give me your password: ')
v5 = hashlib.md5()
v5.update(v5_pass)
v5 = v5.hexdigest()

user_data = [v1,v2,v3,v4,v5]



c.execute('INSERT INTO users (NAME, SURNAME, NICK,  RANGE, PASSWORD) VALUES (?,?,?,?,?);', user_data)





# Committing changes and closing the connection to the database file
conn.commit()
conn.close()
