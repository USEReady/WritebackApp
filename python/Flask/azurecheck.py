import pyodbc

data = []
conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=writeback9.database.windows.net;DATABASE=postgress;UID=postgres;PWD=Useready1')
cursor = conn.cursor()
cursor.execute("SELECT * FROM WB_Input")
row = cursor.fetchall()
print(row)
while row:
    print (str(row[0]) + " " + str(row[1]))
    row = cursor.fetchall()