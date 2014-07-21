import sqlite3
conn=sqlite3.connect('reuters.db');

c = conn.cursor();

c.execute('''select count(term) from frequency where docid="10398_txt_earn" and count=1 ''')
p=c.fetchall()
conn.commit()
print p[0][0]
