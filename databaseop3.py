import sqlite3

conn = sqlite3.connect('database1.db')
#print "Opened database successfully";

cur = conn.cursor()
cur.execute("INSERT INTO Contact(f_name,l_name,email,phone) VALUES('Neal','Caffry','neilcon@hotmail.com','873543666');")

conn.commit()
msg = "Record successfully added"
conn.close()
