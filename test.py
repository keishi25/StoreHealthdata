import psycopg2


# connect postgreSQL
users = 'postgres'  # initial user
dbname = 'postgres'
passwords = '180408436hk'
conn = psycopg2.connect(" user=" + users +" dbname=" + dbname +" password=" + passwords)

# excexute sql
cur = conn.cursor()
cur.execute('SELECT * FROM mybook;')
results = cur.fetchall()

print(results)

# end connect
cur.close()
conn.close()

