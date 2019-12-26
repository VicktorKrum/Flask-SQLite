import sqlite3

conn = sqlite3.connect('database1.db')
#print "Opened database successfully";

conn.execute('CREATE TABLE Contact (f_name TEXT, l_name TEXT, email TEXT, phone integer)')
conn.commit()
print ("Table created successfully");
conn.close()
