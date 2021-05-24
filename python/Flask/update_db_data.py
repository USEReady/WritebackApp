from configparser import ConfigParser
import os
import logging
config = ConfigParser()
config.read(os.path.join(os.path.dirname(__file__), 'config.ini'))

#Update data api Azure Query 
logging.info("this is update data ")
Table_1 = config.get("DATABASE TABLE INFORMATION", "Table_1", raw=True)
Table_1_WriteBack = config.get("DATABASE TABLE COLUMNS INFORMATION", "Table_1_WriteBack", raw=True)
Table_1_Primarykey = config.get("DATABASE TABLE COLUMNS INFORMATION", "Table_1_Primarykey", raw=True)
Table_1_Dashboard = config.get("DATABASE TABLE COLUMNS INFORMATION", "Table_1_Dashboard", raw=True)
table_1_comment = config.get("DATABASE TABLE COLUMNS INFORMATION", "table_1_comment", raw=True)
table_2 = config.get("DATABASE TABLE INFORMATION", "table_2", raw=True)
dashboardname = config.get("SERVERCONFIG ONE DASHBOARD", "dashboardname", raw=True)

Tableau_WB_Value = 'Tableau_WB_Value'
Tableau_WB_Key = 'Tableau_WB_Key'
Tableau_WB_Dashboard = 'Tableau_WB_Dashboard'
Tableau_WB_Comment = 'Tableau_WB_Comment'

#Below are the azure query 
UPDATE_DB_SCRIPT_AZURE = 'begin tran' + ('\n')+'if exists' + '('+'select '+ '* ' +  'from ' + table_2 + ' with ' + '('+'updlock'+','+'serializable'+') ' + 'where ' + '"'+Table_1_Dashboard+'" = '+'\'{'+Tableau_WB_Dashboard+'}\''+' and ActiveFlag = 1)'+ ('\n')+'if exists' + '('+'select '+ '* ' +  'from ' + Table_1+ ' with ' + '('+'updlock'+','+'serializable'+') ' + 'where ' '"'+Table_1_Primarykey+'" = '+'\'{'+Tableau_WB_Key+'}\''+ 'and '+ '"'+Table_1_Dashboard+'" = '+'\'{'+Tableau_WB_Dashboard+'}\''+')'+ ('\n')+ 'begin'+ ('\n')+ 'UPDATE ' + Table_1 + ' set ' + '"' +Table_1_WriteBack+ '" = '+'\'{'+Tableau_WB_Value+'}\'' + ',' + ('\n')+ '"' +table_1_comment+ '" = '+'\'{'+Tableau_WB_Comment+'}\'' + ('\n')+ 'where ' + '"'+Table_1_Primarykey+'" = '+'\'{'+Tableau_WB_Key+'}\''+'and ' +'"' +Table_1_Dashboard+ '" = '+'\'{'+Tableau_WB_Dashboard+'}\'' + ('\n')+ 'end' + ('\n')+ 'else' + ('\n')+ 'begin' + ('\n')+ 'insert into ' + Table_1 + '('+Table_1_Primarykey+ ',' +Table_1_WriteBack+ ',' + Table_1_Dashboard+ ',' +table_1_comment+ ')' + ('\n')+ 'values' + '('+'\'{'+Tableau_WB_Key+'}\''+ ',' +'\'{'+Tableau_WB_Value+'}\''+ ',' +'\'{'+Tableau_WB_Dashboard+'}\''+ ',' +'\'{'+Tableau_WB_Comment+'}\''+ ')' + ('\n')+ 'end' + ('\n')+ 'else' + ('\n')+ 'begin' + ('\n')+ 'insert into ' + Table_1 + '('+Table_1_Primarykey+ ',' +Table_1_WriteBack+ ',' + Table_1_Dashboard+ ')' + ('\n')+ 'values'+ '('+ "'123'" + ',' + "'Error'" + ',' + "'Demo 4'" + ')'+ ('\n')+'end'+ ('\n')+ 'commit tran'

#below are the postgres query 
# UPDATE_DB_SCRIPT_AZURE = 'DO'+ ('\n')+ '$do$'+ ('\n')+ 'BEGIN' + ('\n')+ 'IF EXISTS' + '('+'select '+ '* ' +  'from ' + '"'+table_2+'"'  + ' where ' + '"'+Table_1_Dashboard+'" = '+'\'{'+Tableau_WB_Dashboard+'}\''+' and '+ '\"ActiveFlag\"'+ ' = ' + '\'1\'' + ')'+ ' THEN ' + ('\n')+ 'IF EXISTS' + '('+'select '+ '* ' +  'from ' + '"'+Table_1+'"' + ' where ' '"'+Table_1_Primarykey+'" = '+'\'{'+Tableau_WB_Key+'}\''+ 'and '+ '"'+Table_1_Dashboard+'" = '+'\'{'+Tableau_WB_Dashboard+'}\''+')'+ ' THEN ' + ('\n')+  'UPDATE ' + '"'+Table_1+'"' + ' set ' + '"' +Table_1_WriteBack+ '" = '+'\'{'+Tableau_WB_Value+'}\'' + ',' + ('\n')+ '"' +table_1_comment+ '" = '+'\'{'+Tableau_WB_Comment+'}\'' + ('\n')+ 'where ' + '"'+Table_1_Primarykey+'" = '+'\'{'+Tableau_WB_Key+'}\''+'and ' +'"' +Table_1_Dashboard+ '" = '+'\'{'+Tableau_WB_Dashboard+'}\''+ ';' + ('\n')+ 'ELSE' + ('\n')+ 'insert into ' + '"'+Table_1+'"' + '('+Table_1_Primarykey+ ',' +Table_1_WriteBack+ ',' + Table_1_Dashboard+ ',' +table_1_comment+ ')' + ('\n')+ 'values' + '('+'\'{'+Tableau_WB_Key+'}\''+ ',' +'\'{'+Tableau_WB_Value+'}\''+ ',' +'\'{'+Tableau_WB_Dashboard+'}\''+ ',' +'\'{'+Tableau_WB_Comment+'}\''+ ')' + ';' + ('\n')+ 'END IF'+ ';' + ('\n')+ 'END IF'+ ';' + ('\n')+ 'END' + ('\n')+ '$do$' 

#Below are the Mysql query 
# UPDATE_DB_SCRIPT_AZURE = 'BEGIN ' +('\n')+'SELECT '+ '*' +('\n')+ 'FROM '+ '`'+table_2+'`'+ ('\n')+ 'WHERE EXISTS ' + '('+'SELECT' + ' * '+ ('\n')+'FROM'+ '`'+table_2+'`'+ ('\n')+'WHERE ' + '`'+Table_1_Dashboard+'` = '+'"'+Tableau_WB_Dashboard+'"' + 'and '+ '`ActiveFlag`'+ ' = ' + '\'1\''+ ')'+'; ' +('\n')+'SELECT '+ '* ' +('\n')+ 'FROM '+ '`'+Table_1+'`' +('\n')+' WHERE EXISTS ' + '('+'SELECT ' + '* '+ ('\n')+'FROM '+ '`'+Table_1+'`' +('\n')+' WHERE ' + '`'+Table_1_Primarykey+'`= '+'"'+Tableau_WB_Key+'"' + 'and '+ '`'+Table_1_Dashboard+'` = '+'"'+Tableau_WB_Dashboard+'"'+')'+';' + ('\n')+'UPDATE ' + '`'+Table_1+'`' + ' SET ' + '`'+Table_1_WriteBack+'` = '+'"'+Tableau_WB_Value+'"' + ',' + '`'+table_1_comment+'` = '+'"'+Tableau_WB_Comment+'"' + ('\n')+'WHERE ' + '`'+Table_1_Primarykey+'` = '+'"'+Tableau_WB_Key+'"'+'AND ' + '`'+Table_1_Dashboard+'` = '+'"'+Tableau_WB_Dashboard+'"'+ ';'+ ('\n')+'END'+' ; '

# UPDATE_DB_SCRIPT_AZURE = 'START TRANSACTION '+ ';' +('\n')+ 'SELECT '+ '*' +('\n')+ 'FROM '+ '`postgres`' + '.'+ '`'+table_2+'`'+ ('\n')+ 'WHERE EXISTS ' + '('+'SELECT' + ' * '+ ('\n')+'FROM '+ '`postgres`' + '.'+'`'+table_2+'`'+ ('\n')+'WHERE ' + '`'+Table_1_Dashboard+'` = '+'"'+Tableau_WB_Dashboard+'"' + 'and '+ '`ActiveFlag`'+ ' = ' + '\"1\"'+ ')'+'; ' +('\n')+'SELECT '+ '* ' +('\n')+ 'FROM '+ '`postgres`' + '.'+'`'+Table_1+'`' +('\n')+' WHERE EXISTS ' + '('+'SELECT ' + '* '+ ('\n')+'FROM '+ '`postgres`' + '.'+ '`'+Table_1+'`' +('\n')+' WHERE ' + '`'+Table_1_Primarykey+'`= '+'"'+Tableau_WB_Key+'"' + 'and '+ '`'+Table_1_Dashboard+'` = '+'"'+Tableau_WB_Dashboard+'"'+')'+';' + ('\n')+ 'UPDATE ' + '`postgres`' + '.'+'`'+Table_1+'`' + ' SET ' + '`'+Table_1_WriteBack+'` = '+'"'+Tableau_WB_Value+'"' + ',' + '`'+table_1_comment+'` = '+'"'+Tableau_WB_Comment+'"' + ('\n')+'WHERE ' + '`'+Table_1_Primarykey+'` = '+'"'+Tableau_WB_Key+'"'+ ' AND ' + '`'+Table_1_Dashboard+'` = '+'"'+Tableau_WB_Dashboard+'"'+ ';' +('\n')+ 'COMMIT' + ';'

# UPDATE_DB_SCRIPT_AZURE = 'begin tran' + ('\n')+'if exists' + '('+'select '+ '* ' +  'from ' + table_2 + ' with ' + '('+'updlock'+','+'serializable'+') ' + 'where ' + '"'+Table_1_Dashboard+'" = '+'\'{'+Tableau_WB_Dashboard+'}\''+' and ActiveFlag = 1)'+ ('\n')+'if exists' + '('+'select '+ '* ' +  'from ' + Table_1+ ' with ' + '('+'updlock'+','+'serializable'+') ' + 'where ' '"'+Table_1_Primarykey+'" = '+'\'{'+Tableau_WB_Key+'}\''+ 'and '+ '"'+Table_1_Dashboard+'" = '+'\'{'+Tableau_WB_Dashboard+'}\''+')'+ ('\n')+ 'begin'+ ('\n')+ 'UPDATE ' + Table_1 + ' set ' + '"' +Table_1_WriteBack+ '" = '+'\'{'+Tableau_WB_Value+'}\''  + ('\n')+ 'where ' + '"'+Table_1_Primarykey+'" = '+'\'{'+Tableau_WB_Key+'}\''+'and ' +'"' +Table_1_Dashboard+ '" = '+'\'{'+Tableau_WB_Dashboard+'}\'' + ('\n')+ 'end' + ('\n')+ 'else' + ('\n')+ 'begin' + ('\n')+ 'insert into ' + Table_1 + '('+Table_1_Primarykey+ ',' +Table_1_WriteBack+ ',' + Table_1_Dashboard+ ')' + ('\n')+ 'values' + '('+'\'{'+Tableau_WB_Key+'}\''+ ',' +'\'{'+Tableau_WB_Value+'}\''+ ',' +'\'{'+Tableau_WB_Dashboard+'}\''+ ')' + ('\n')+ 'end' + ('\n')+ 'else' + ('\n')+ 'begin' + ('\n')+ 'insert into ' + Table_1 + '('+Table_1_Primarykey+ ',' +Table_1_WriteBack+ ',' + Table_1_Dashboard+ ')' + ('\n')+ 'values'+ '('+ "'123'" + ',' + "'Error'" + ',' + "'Demo 4'" + ')'+ ('\n')+'end'+ ('\n')+ 'commit tran'
# UPDATE_DB_SCRIPT_AZURE  = 'begin tran' + ('\n')+'if exists' + '('+'select '+ '* ' +  'from ' + table_2 + ' with ' + '('+'updlock'+','+'serializable'+') ' + 'where ' + '"'+Table_1_Dashboard+'" = '+'\'{'+Tableau_WB_Dashboard+'}\''+')'+ ('\n')+'if exists' + '('+'select '+ '* ' +  'from ' + Table_1+ ' with ' + '('+'updlock'+','+'serializable'+') ' + 'where ' '"'+Table_1_Primarykey+'" = '+'\'{'+Tableau_WB_Key+'}\''+ 'and '+ '"'+Table_1_Dashboard+'" = '+'\'{'+Tableau_WB_Dashboard+'}\''+')'+ ('\n')+ 'begin'+ ('\n')+ 'UPDATE ' + Table_1 + ' set ' + '"' +Table_1_WriteBack+ '" = '+'\'{'+Tableau_WB_Value+'}\''  + ('\n')+ 'where ' + '"'+Table_1_Primarykey+'" = '+'\'{'+Tableau_WB_Key+'}\''+'and ' +'"' +Table_1_Dashboard+ '" = '+'\'{'+Tableau_WB_Dashboard+'}\'' + ('\n')+ 'end' + ('\n')+ 'else' + ('\n')+ 'begin' + ('\n')+ 'insert into ' + Table_1 + '('+Table_1_Primarykey+ ',' +Table_1_WriteBack+ ',' + Table_1_Dashboard+ ')' + ('\n')+ 'values' + '('+'\'{'+Tableau_WB_Key+'}\''+ ',' +'\'{'+Tableau_WB_Value+'}\''+ ',' +'\'{'+Tableau_WB_Dashboard+'}\''+ ')' + ('\n')+ 'end' + ('\n')+ 'else' + ('\n')+ 'begin' + ('\n')+ 'insert into ' + Table_1 + '('+Table_1_Primarykey+ ',' +Table_1_WriteBack+ ',' + Table_1_Dashboard+ ')' + ('\n')+ 'values'+ '('+ "'123'" + ',' + "'Error'" + ',' + "'Demo 4'" + ')'+ ('\n')+'end'+ ('\n')+ 'commit tran'
# print(UPDATE_DB_SCRIPT_AZURE)

#Define connection and execute the update query 
def run(WB_Value,WB_Key,WB_Dashboard,WB_Comment):
    import database_conn_api
    import datetime
    if WB_Dashboard in dashboardname:
        conn = database_conn_api.get_connection_obj_azure()
    else:
        conn = database_conn_api.get_connection_obj_azure1()
    # conn = database_conn_api.get_connection_obj_azure()
    logging.info(UPDATE_DB_SCRIPT_AZURE)
    database_conn_api.execute_dml(conn, UPDATE_DB_SCRIPT_AZURE.format(Tableau_WB_Value = WB_Value, Tableau_WB_Key = WB_Key, Tableau_WB_Dashboard = WB_Dashboard, Tableau_WB_Comment=WB_Comment))
    return {"success": "Update table successful!"}
    


