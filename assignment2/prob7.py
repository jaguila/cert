import sqlite3
conn=sqlite3.connect('matrix.db');

c = conn.cursor();

c.execute(''' SELECT value 
FROM(
    SELECT A.row_num                as row_num, 
           B.col_num                as col_num, 
           SUM(A.value * B.value)   as value
    FROM A, B
    WHERE A.col_num = B.row_num
    GROUP BY A.row_num, B.col_num)
WHERE row_num = 2 AND col_num = 3;''')
p=c.fetchall()
conn.commit()
#print p
print p[0][0]
