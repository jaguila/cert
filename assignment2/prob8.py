import sqlite3
conn=sqlite3.connect('reuters.db');

c = conn.cursor();

c.execute(''' SELECT similarity
FROM(
    SELECT  F1.docid as docid1, 
            F2.docid as docid2, 
            SUM(F1.count * F2.count) as similarity 
    FROM Frequency as F1, Frequency as F2
    WHERE F1.term = F2.term AND
          F1.docid = '10080_txt_crude' AND 
          F2.docid = '17035_txt_earn'
   GROUP BY F1.docid, F2.docid);''')
p=c.fetchall()
conn.commit()
#print p
print p[0][0]
