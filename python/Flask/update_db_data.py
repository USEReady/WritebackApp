# define Update query here inculding postgres and azure 
# # for postgres  
# UPDATE_DB_SCRIPT_1 = '''
# UPDATE public."ForecastingWb" set "Forecast_Period" = {forecast_period_str}, 
#  "Forecast" = {forecast_number}	where "Row ID" = {key};
# '''
# # for postgres  
# UPDATE_DB_SCRIPT_2 = '''
# UPDATE public."Forecast" set "Profit" = {profit}, 
#  "Sales" = {sales}	where "Row ID" = {key} and "Category" = '{category}';
# '''
# #for postgrres 
#UPDATE_DB_SCRIPT_2 replace to new script in azure 
# Table_1 = config.get("DATABASE TABLE INFORMATION", "Table_1", raw=True)
# Table_1_col5 = config.get("DATABASE TABLE COLUMNS INFORMATION", "Table_1_col5", raw=True)
# Table_1_col3 = config.get("DATABASE TABLE COLUMNS INFORMATION", "Table_1_col3", raw=True)
# Table_1_Primarykey = config.get("DATABASE TABLE COLUMNS INFORMATION", "Table_1_Primarykey", raw=True)
# Table_1_col1 = config.get("DATABASE TABLE COLUMNS INFORMATION", "Table_1_col1", raw=True)
# Tableau_col8 = config.get("TABLEAU DATA", "Tableau_col8", raw=True)
# Tableau_col9 = config.get("TABLEAU DATA", "Tableau_col9", raw=True)
# Tableau_col10 = config.get("TABLEAU DATA", "Tableau_col10", raw=True)
# Tableau_col11 = config.get("TABLEAU DATA", "Tableau_col11", raw=True)
# UPDATE_DB_SCRIPT_AZURE4 = 'UPDATE '+ '"'+Table_1+'"'+" set "+ '"' +Table_1_col5+ '" = ' + '{'+Tableau_col8+'}'+',' + '"'+Table_1_col3+'" = ' + '{'+Tableau_col9+'}' + 'where ' + '"'+Table_1_Primarykey+'" = ' + '{'+Tableau_col10+'}'+ 'and ' + '"'+Table_1_col1+'" = ' + '{'+Tableau_col11+'}'

# # for postgres  
# UPDATE_DB_SCRIPT_3 = '''
# UPDATE public."ForecastingWb" set "Forecast" = {forecast}
#  where "Account_ID" = {accountid} and "Forecast_Period" = '{forecastperiod}';
# '''
# # for postgres  
# UPDATE_DB_SCRIPT = '''
# UPDATE public."Forecast" set "Forecast Amount" = {forecast}
#  where "Row ID" = {rowid};
# '''
# # # for azure
# # UPDATE_DB_SCRIPT_AZURE = '''
# # UPDATE "forecast" set "Forecast_Amount" = {forecast}
# #  where "Row_ID" = {rowid};
# # '''

from configparser import ConfigParser
import os

config = ConfigParser()
config.read(os.path.join(os.path.dirname(__file__), 'config.ini'))

# file = r'C:\Users\Admin\Desktop\azure\python\python\FlaskPrototype\config.ini'
# config = ConfigParser()
# config.read(file)
Table_1 = config.get("DATABASE TABLE INFORMATION", "Table_1", raw=True)
Table_1_col6 = config.get("DATABASE TABLE COLUMNS INFORMATION", "Table_1_col6", raw=True)
Table_1_Primarykey = config.get("DATABASE TABLE COLUMNS INFORMATION", "Table_1_Primarykey", raw=True)
Tableau_col6 = config.get("TABLEAU DATA", "Tableau_col6", raw=True)
Tableau_col7 = config.get("TABLEAU DATA", "Tableau_col7", raw=True)
UPDATE_DB_SCRIPT_AZURE = 'UPDATE '+ '"'+Table_1+'"'+" set "+ '"' +Table_1_col6+ '" = ' + '{'+Tableau_col6+'}' +' where '+'"'+Table_1_Primarykey+'" = ' + '{'+Tableau_col7+'}'
# print(UPDATE_DB_SCRIPT_AZURE)

#Define connection and execute the update quuery 
def run(Tableau_col6, Tableau_col7):
    import postgre_conn_api
    import datetime
    conn = postgre_conn_api.get_connection_obj_azure()
    postgre_conn_api.execute_dml(conn, UPDATE_DB_SCRIPT_AZURE.format(forecast=Tableau_col6, rowid=Tableau_col7))
    # postgre_conn_api.execute_dml(conn, UPDATE_DB_SCRIPT.format(forecast=forecast, rowid=rowid))
    #postgre_conn_api.execute_dml(conn, UPDATE_DB_SCRIPT.format(forecast=forecast, accountid=accountid, forecastperiod=forecastperiod))
    #postgre_conn_api.execute_dml(conn, UPDATE_DB_SCRIPT.format(profit=profit, sales=sales, key=keyid, category=category))
    #postgre_conn_api.execute_dml(conn, UPDATE_DB_SCRIPT.format(forecast_period_str="'Jan-Jun2018'",forecast_number=9008930, key=keyId))
    #postgre_conn_api.execute_dml(conn, UPDATE_DB_SCRIPT.format(forecast_number=4659893, key=keyId))
    return {"success": "Update table successful!"}
    


