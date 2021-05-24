import mysql.connector

mydb = mysql.connector.connect(
  host="uracme-waitress.useready.com",
  user="root",
  password="Useready1",
  port="3306"
)

cursor = mydb.cursor()
cursor.execute('SELECT * FROM postgres.wb_input')
customers = cursor.fetchall()
print(customers)
# customers = list(cursor.fetchall())
print('We have {} customers'.format(len(customers))) 

mydb.close()

print(mydb)