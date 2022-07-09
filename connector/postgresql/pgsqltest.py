import psycopg2
import datetime
# 连接数据库
conn = psycopg2.connect(database='postgres', user='postgres', password='123456', host='127.0.0.1', port='5432')

curs = conn.cursor()
curs.execute("BEGIN;")

now_time=datetime.datetime.now()


for _ in range(0,1000000):

    sql = 'INSERT INTO ad_expense_checksum(ad_expense_unique_id, hash,create_date) VALUES(1,1,\'{}\');'
    sql2 = 'INSERT INTO ad_monetization_checksum(ad_monetization_unique_id, hash,create_date) VALUES(1,1,\'{}\');'

    now_time=now_time+datetime.timedelta(seconds=1)

    curs.execute(sql.format(now_time))
    curs.execute(sql2.format(now_time))


curs.execute("COMMIT;")


print("OVER")

curs.close()
conn.close()