#Define Logging and Database Connection info
import logging
import psycopg2
from psycopg2 import Error
import pyodbc
import os
import mysql.connector
from pyodbc import Error
from datetime import date
from configparser import ConfigParser
from cryptography.fernet import Fernet
config = ConfigParser()
config.read(os.path.join(os.path.dirname(__file__), 'config.ini'))
example = config.get("PATHS", "example_file", raw=True)
logging.basicConfig(format='%(asctime)s %(message)s',filename=example, level=logging.DEBUG)


#Mysql connection
def get_connection_obj():
    conn = None
    try:
        logging.info("PostgreSQL server information...")
        from create_config_file import read_config
        db_cred_obj = read_config()
        conn = mysql.connector.connect(
            host=db_cred_obj["host"],
            port =db_cred_obj["port"],
            database=db_cred_obj["database"],
            user=db_cred_obj["user"],
            password=db_cred_obj["password"])
        return conn

    except (Exception, Error) as error:
        logging.error("Error while connecting to PostgreSQL", error)

# #Postgres connection
# def get_connection_obj():
#     conn = None
#     try:
#         logging.info("PostgreSQL server information...")
#         from create_config_file import read_config
#         db_cred_obj = read_config()
#         conn = psycopg2.connect(
#             host=db_cred_obj["host"],
#             port =db_cred_obj["port"],
#             database=db_cred_obj["database"],
#             user=db_cred_obj["user"],
#             password=db_cred_obj["password"])
#         return conn

#     except (Exception, Error) as error:
#         logging.error("Error while connecting to PostgreSQL", error)


#Get Username & password using decrypted function  
def GetAuthDetails():
    key = config.get('KEY', 'key', raw=True).encode("utf-8")
    cipher_suite = Fernet(key)
    encrypted_username = config.get('DEFAULT SERVERCONFIG', 'user', raw=True).encode("utf-8")
    encrypted_password = config.get('DEFAULT SERVERCONFIG', 'password', raw=True).encode("utf-8")
    decrypted_username = cipher_suite.decrypt(encrypted_username).decode("utf-8")
    decrypted_password = cipher_suite.decrypt(encrypted_password).decode("utf-8")
    # print(decrypted_username,decrypted_password,'line no 25')
    return decrypted_username, decrypted_password

#this is decrypted function  
def GetAuthDetails1():
    key1 = config.get('KEY1', 'key1', raw=True).encode("utf-8")
    cipher_suite = Fernet(key1)
    encrypted_username = config.get('SERVERCONFIG ONE', 'user', raw=True).encode("utf-8")
    encrypted_password = config.get('SERVERCONFIG ONE', 'password', raw=True).encode("utf-8")
    decrypted_username = cipher_suite.decrypt(encrypted_username).decode("utf-8")
    decrypted_password = cipher_suite.decrypt(encrypted_password).decode("utf-8")
    # print(decrypted_username,decrypted_password,'line no 36')
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
        print(user_id,password_)
        conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server_+';DATABASE='+database_+';UID='+user_id+';PWD='+password_)
        
        return conn
        
#Error Occur when Connection not established 
    except (Exception, Error) as error:
        logging.error("Error while connecting to Azure SQL server", error)

#Define Azure Database connection string 
def get_connection_obj_azure1():
    conn = None
    try:
        logging.info("Azure server information...")
        server_ = config.get('SERVERCONFIG ONE','server')
        database_ = config.get('SERVERCONFIG ONE','database')
        # user_id = config.get('SERVERCONFIG1','user')
        # password_ = config.get('SERVERCONFIG1','password')
        user_id, password_ = GetAuthDetails1()
        # print(user_id,password_)
        conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server_+';DATABASE='+database_+';UID='+user_id+';PWD='+password_)
        
        return conn
        
#Error Occur when Connection not established 
    except (Exception, Error) as error:
        logging.error("Error while connecting to Azure SQL server", error)        

#Define Connection cursor 
def acquire_cursor(conn):
    cursor = conn.cursor()
    return cursor

#Define execute dml query  
def execute_dml(conn,query):
    cur = acquire_cursor(conn)
    cur.execute(query)
    logging.info('Query executed successfully!!')
    # Close the cursor and connection to so the server can allocate
    # bandwidth to other requests
    cur.close()
    conn.commit()
    conn.close()


#Define execute query  
def execute_query(conn,query):
    cur = acquire_cursor(conn)
    cur.execute(query)
    query_results = cur.fetchall()
    logging.info(query_results)
    logging.info('Total records returned is %s' % (len(query_results)))
    # Close the cursor and connection to so the server can allocate
    # bandwidth to other requests
    cur.close()
    conn.commit()
    conn.close()

    # need to convert to array 
    data = []
    for row in query_results:
        data.append(list(row))
     
    return data
