import sqlite3
conn=sqlite3.connect('reuters.db');

c = conn.cursor();

c.execute(''' 
CREATE VIEW Frequency_with_query AS
SELECT * FROM Frequency
UNION
SELECT 'q' as docid, 'washington' as term, 1 as count 
UNION
SELECT 'q' as docid, 'taxes' as term, 1 as count
UNION 
SELECT 'q' as docid, 'treasury' as term, 1 as count;



''')
c.execute('''SELECT MAX(similarity)
FROM(
    SELECT F2.docid as docid, SUM(F1.count * F2.count) as similarity 
    FROM Frequency_with_query as F1, Frequency_with_query as F2
    WHERE F1.term = F2.term AND
          F1.docid = 'q' 
    GROUP BY F1.docid, F2.docid);''')
p=c.fetchall()
conn.commit()
#print p
print p[0][0]
