#Define Logging and Database Connection 
import logging
import psycopg2
from psycopg2 import Error
from create_config_file import read_config
import pyodbc
import os
from pyodbc import Error
from configparser import ConfigParser
config = ConfigParser()
config.read(os.path.join(os.path.dirname(__file__), 'config.ini'))
example = config.get("PATHS", "example_file", raw=True)
logging.basicConfig(filename=example, level=logging.DEBUG)
# logging.basicConfig(filename=r'C:\Users\Admin\Desktop\azure\python\python\FlaskPrototype\example.log', level=logging.DEBUG)

#load and read config file
# config = ConfigParser()
# config.read(os.path.join(os.path.dirname(__file__), 'config.ini'))
# file = r'C:\Users\Admin\Desktop\azure\python\python\FlaskPrototype\config.ini'
# config = ConfigParser()
# config.read(file)

#Get Postgres Connection Object
def get_connection_obj():
    conn = None
    try:
        logging.info("PostgreSQL server information...")
        from create_config_file import read_config
        #create Connection object
        db_cred_obj = read_config()
        conn = psycopg2.connect(
            host=db_cred_obj["host"],
            port =db_cred_obj["port"],
            database=db_cred_obj["database"],
            user=db_cred_obj["user"],
            password=db_cred_obj["password"])
        return conn

#Error Occur when Connection not established 
    except (Exception, Error) as error:
        logging.error("Error while connecting to PostgreSQL", error)
        
#Define Azure Database connection string 
def get_connection_obj_azure():
    conn = None
    try:
        logging.info("Azure server information...")
        server_ = config.get('SERVERCONFIG','server')
        database_ = config.get('SERVERCONFIG','database')
        user_id = config.get('SERVERCONFIG','user')
        password_ = config.get('SERVERCONFIG','password')
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