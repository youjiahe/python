import pymysql
conn = pymysql.connect(
    host='139.159.193.210',
    port=3306,
    user='student',
    password='123456',
    db='bbs',
    charset='utf8'
)

cur = conn.cursor()
select1 = "select * from mark"
desc1="desc mark"

cur.execute(desc1)
desc1=cur.fetchall()

for desc in desc1:
    print(desc[0],end=' ')
print()
# insert1='insert mark values(%s,%s,%s,%s,%s)'
# insert1_data=['youjiahe',80,100,99,85]
# cur.execute(insert1,insert1_data)
# conn.commit()
cur.execute(select1)
all=cur.fetchall()
for mark in all:
    print(mark)
delete1='delete from mark where name=%s'
cur.execute(delete1,'youjiahe')
conn.commit()
cur.close()
conn.close()
