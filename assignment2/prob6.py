import sqlite3
conn=sqlite3.connect('reuters.db');

c = conn.cursor();

c.execute(''' select count(*) from (select docid as docid1 from frequency where term="transactions") inner join (select docid as docid2 from frequency where term="world") on docid1=docid2''')
p=c.fetchall()
conn.commit()
#print p
print p[0][0]
