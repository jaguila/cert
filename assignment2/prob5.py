import sqlite3
conn=sqlite3.connect('reuters.db');

c = conn.cursor();

c.execute(''' select count(docid) from (select sum(count) as term_count, docid from frequency group by docid) where term_count>300 ''')
p=c.fetchall()
conn.commit()
#print p
print p[0][0]
