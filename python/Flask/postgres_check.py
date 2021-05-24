import psycopg2

connection = psycopg2.connect(
    host='uracme-waitress.useready.com',  # host on which the database is running
    database='postgres',  # name of the database to connect to
    user='postgres',  # username to connect with
    password='Useready1',  # password associated with your username
    port = '5432'
)

cursor = connection.cursor()
cursor.execute('SELECT * FROM "WB_Input"')
customers = cursor.fetchall()
print(customers)
# customers = list(cursor.fetchall())
print('We have {} customers'.format(len(customers))) 

connection.close()
