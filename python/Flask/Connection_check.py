import pyodbc
import os
from configparser import ConfigParser
from cryptography.fernet import Fernet
import mysql.connector
from pyodbc import Error
import logging
import psycopg2
from psycopg2 import Error
import pyodbc
import os

config = ConfigParser()
config.read(os.path.join(os.path.dirname(__file__), 'config.ini'))

def GetAuthDetails():
    key = config.get('KEY', 'key', raw=True).encode("utf-8")
    cipher_suite = Fernet(key)
    encrypted_username = config.get('DEFAULT SERVERCONFIG', 'user', raw=True).encode("utf-8")
    encrypted_password = config.get('DEFAULT SERVERCONFIG', 'password', raw=True).encode("utf-8")
    decrypted_username = cipher_suite.decrypt(encrypted_username).decode("utf-8")
    decrypted_password = cipher_suite.decrypt(encrypted_password).decode("utf-8")
    # print(decrypted_username,decrypted_password,'line no 25')
    return decrypted_username, decrypted_password


#Define Azure Database connection string 
def get_connection_obj_azure():
    conn = None
    try:
        logging.info("Azure server information...")
        server_ = config.get('DEFAULT SERVERCONFIG','server')
        database_ = config.get('DEFAULT SERVERCONFIG','database')
        # user_id = config.get('SERVERCONFIG','user')
        # password_ = config.get('SERVERCONFIG','password')
        user_id, password_ = GetAuthDetails()
        print("Decrypted username is " ,user_id," Decrypted password is ", password_)
        conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server_+';DATABASE='+database_+';UID='+user_id+';PWD='+password_)
        
        return conn
        
#Error Occur when Connection not established 
    except (Exception, Error) as error:
        print("Error while connecting to Azure SQL server", error)

conn = get_connection_obj_azure()
data = []
cursor = conn.cursor()
cursor.execute("SELECT top 1 *  FROM WB_Admin")
row = cursor.fetchall()
print("First row of the table ")
print(row)
print("Database connection successfully eztablished")
