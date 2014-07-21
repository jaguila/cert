import sqlite3
conn=sqlite3.connect('reuters.db');

c = conn.cursor();

c.execute(''' select count(*) from frequency where term like "parliament" ''')
p=c.fetchall()
conn.commit()
#print p
print p[0][0]
