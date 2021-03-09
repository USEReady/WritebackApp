#Delete the db table mentioned here
# for postgres sales 
# DROP_TABLE_QUERY_SALES = '''
# drop table public."Sales";
# '''
# # for postgres forecast
# DROP_TABLE_QUERY_FORECAST = '''
# drop table public."Forecast";
# '''
# # for postgres forecast
# TRUNCATE_TABLE_QUERY_FORECAST = '''
# truncate table public."Forecast";
# '''
# # for azure foreacst
# TRUNCATE_TABLE_QUERY_FORECAST_AZURE = '''
# truncate table "Forecast";
# '''

# # for azure sales
# TRUNCATE_TABLE_QUERY_SALES_AZURE = '''
# truncate table "Sales";
# '''

from configparser import ConfigParser
import os

config = ConfigParser()
config.read(os.path.join(os.path.dirname(__file__), 'config.ini'))

# file = r'C:\Users\Admin\Desktop\azure\python\python\FlaskPrototype\config.ini'
# config = ConfigParser()
# config.read(file)

Table_1 = config.get("DATABASE TABLE INFORMATION", "Table_1", raw=True)
TRUNCATE_TABLE_QUERY_FORECAST_AZURE = 'truncate '+ 'table ' + '"'+Table_1+'"'


#function execute and run the query 
def run():
    import postgre_conn_api
    conn = postgre_conn_api.get_connection_obj_azure()
    postgre_conn_api.execute_dml(conn, TRUNCATE_TABLE_QUERY_FORECAST_AZURE)

# def run():
#     import postgre_conn_api
#     conn = postgre_conn_api.get_connection_obj()
#     postgre_conn_api.execute_dml(conn, TRUNCATE_TABLE_QUERY_FORECAST)