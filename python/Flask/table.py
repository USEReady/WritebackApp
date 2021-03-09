from configparser import ConfigParser

file = 'config.ini'
config = ConfigParser()
config.read(file)
Table_1 = config.get("DATABASE TABLE INFORMATION", "Table_1", raw=True)
Table_1_col6 = config.get("DATABASE TABLE COLUMNS INFORMATION", "Table_1_col6", raw=True)
Table_1_Primarykey = config.get("DATABASE TABLE COLUMNS INFORMATION", "Table_1_Primarykey", raw=True)
Tableau_col6 = config.get("TABLEAU DATA", "Tableau_col6", raw=True)
Tableau_col7 = config.get("TABLEAU DATA", "Tableau_col7", raw=True)
UPDATE_DB_SCRIPT_AZURE = 'UPDATE '+ '"'+Table_1+'"'+" set "+ '"' +Table_1_col6+ '" = ' + '{'+Tableau_col6+'}' +' where '+'"'+Table_1_Primarykey+'" = ' + '{'+Tableau_col7+'}'
print(UPDATE_DB_SCRIPT_AZURE)
print(Table_1)
