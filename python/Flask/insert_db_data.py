#insert data into table mentioned here 
#for tableau data table
# INSERT_DB_SCRIPT_1 = '''
# INSERT INTO public."ForecastingWb"(
# 	"Sales_Team", 
# 	"Sales_Leader", 
# 	"Regional_Head_of_Sales", 
# 	"Forecast_Period", 
# 	"Forecast", 
# 	"Contract_Date", 
# 	"COA_Product_Name", 
# 	"COA_Product_Id", 
# 	"Account_Name", 
# 	"Account_ID", 
# 	"ID")
# 	VALUES 
# 	('Engineering Team 2', 
# 	'Tim Cook', 
# 	'Lionel Wa', 
# 	'Oct-Dec 2021', 
# 	6120076, 
# 	TO_DATE('{Contract_Date}','YYYY-MM-DD'), 
# 	'Tableau Desktop', 
# 	3345899, 
# 	'DataAnalytics', 
# 	12345666, 
# 	{rowid});
# '''
# #for postgres data table
# INSERT_DB_SCRIPT = '''
# insert into public."Forecast"
# SELECT "Row ID", 
#        "Order Date", 
#        "Ship Date", "Customer ID", 
#        "Customer Name", "Category", 
#        "Sales", "Profit", 0
# 	FROM public."Sales";
# '''

#for azure data table
# INSERT_DB_SCRIPT_AZURE = '''
# insert into "Forecast"
# SELECT "Row_ID", 
#        "Contract_Date", 
#        "Ship_Date", "Customer_ID", 
#        "Customer_Name", "Category", 
#        "Sales", "Profit", 0
# 	FROM "sales";
# '''
from configparser import ConfigParser
import os

config = ConfigParser()
config.read(os.path.join(os.path.dirname(__file__), 'config.ini'))

# file = r'C:\Users\Admin\Desktop\azure\python\python\FlaskPrototype\config.ini'
# config = ConfigParser()
# config.read(file)

Table_1 = config.get("DATABASE TABLE INFORMATION", "Table_1", raw=True)
Table_1_Primarykey = config.get("DATABASE TABLE COLUMNS INFORMATION", "Table_1_Primarykey", raw=True)
Table_2_col1 = config.get("DATABASE TABLE COLUMNS INFORMATION", "Table_2_col1", raw=True)
Table_1_col7 = config.get("DATABASE TABLE COLUMNS INFORMATION", "Table_1_col7", raw=True)
Table_1_col4 = config.get("DATABASE TABLE COLUMNS INFORMATION", "Table_1_col4", raw=True)
Table_1_col2 = config.get("DATABASE TABLE COLUMNS INFORMATION", "Table_1_col2", raw=True)
Table_1_col1 = config.get("DATABASE TABLE COLUMNS INFORMATION", "Table_1_col1", raw=True)
Table_1_col3 = config.get("DATABASE TABLE COLUMNS INFORMATION", "Table_1_col3", raw=True)
Table_1_col5 = config.get("DATABASE TABLE COLUMNS INFORMATION", "Table_1_col5", raw=True)
Table_2 = config.get("DATABASE TABLE INFORMATION", "Table_2", raw=True)
INSERT_DB_SCRIPT_AZURE = 'insert '+ 'into ' + '"'+Table_1+'"' + ' SELECT '+  '"'+Table_1_Primarykey+'"' + ',' + '"'+Table_2_col1+'"' +',' + '"'+Table_1_col7+'"' +',' + '"'+Table_1_col4+'"' + ',' + '"'+Table_1_col2+'"' +',' + '"'+Table_1_col1+'"' + ','+ '"'+Table_1_col3+'"' +',' + '"'+Table_1_col5+'"'  +   'FROM ' +  '"'+Table_2+'"'
print(INSERT_DB_SCRIPT_AZURE)

#define connection and execute the insert azure query 
def run():
    import postgre_conn_api
    import datetime
    conn = postgre_conn_api.get_connection_obj_azure()
    postgre_conn_api.execute_dml(conn, INSERT_DB_SCRIPT_AZURE)
    return {"success": "Insert into table successful!"}

#this is for postgres query 
# def run(rowid=1001):
#     import postgre_conn_api
#     import datetime
#     conn = postgre_conn_api.get_connection_obj()
#     #postgre_conn_api.execute_dml(conn, INSERT_DB_SCRIPT.format(Contract_Date=datetime.date(2020, 10, 15), rowid=rowid))
#     postgre_conn_api.execute_dml(conn, INSERT_DB_SCRIPT)
#     return {"success": "Insert into table successful!"}
