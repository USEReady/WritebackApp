# This is a main Python script.
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
# Use a breakpoint in the code line below to debug your script.
# Press Ctrl+F8 to toggle the breakpoint.

# import all neccessary packages 
import postgre_conn_api
from update_db_data import run
import json
import itertools
import logging
import os
import simplejson as json
from datetime import date
import ssl
from configparser import ConfigParser
from flask import Flask, jsonify, make_response, abort, request, Response, render_template
from waitress import serve
from datetime import datetime


#Create and load config file 
config = ConfigParser()
config.read(os.path.join(os.path.dirname(__file__), 'config.ini'))
# file = r'C:\Users\Admin\Desktop\azure\python\python\FlaskPrototype\config.ini'
# config = ConfigParser()
# config.read(file)
# print(config.sections())

#Logging path and app name define 
app = Flask(__name__)
example = config.get("PATHS", "example_file", raw=True)
logging.basicConfig(filename=example, level=logging.DEBUG)
# logging.basicConfig(filename='example.log', level=logging.DEBUG)


#Azure Query Execute here
myselect = config.get("AZUREQUERY", "select", raw=True)
# for line in myselect.split("\n"):
#     print (":%s:" % (line))


#Define 2 types of Error 404 & 400 
@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'custom_error': 'Method with this signature not found'}), 404)

@app.errorhandler(400)
def not_found(error):
    return make_response(jsonify({'custom_error': 'Input parameter not correct.'}), 400)


#Define all Routes with extension /tableauextensions/writeback/api
@app.route("/")
def main():
    logging.info(request)
    return "Hello world. Welcome to flask!"

#Index Route End point
@app.route("/tableauextensions/writeback/api/index", methods=['GET', 'POST', 'PUT'])
def index():
    logging.info(request)
    return "Welcome to Flask!This is the index method."

#Insert Data Endpoint
@app.route("/tableauextensions/writeback/api/insertdata", methods = ['GET', 'POST', 'PUT'])
def insert_data():
    Json_Primarykey = config.get("JSON", "Json_Primarykey", raw=True)
    logging.info(request)
    try:
        _json = request.json
        for rec in _json:
            config.set('DATABASE TABLE COLUMNS INFORMATION',
                       'Table_1_col9', rec[Json_Primarykey])
            Table_1_col9 = config.get(
                'DATABASE TABLE COLUMNS INFORMATION', 'Table_1_col9')
            from insert_db_data import run
            t = run(Table_1_col9)
        return jsonify(t)
    except Exception as e:
        return jsonify (e, 'Row_id not found')       


#Get User Role Endpoint
@app.route("/tableauextensions/writeback/api/getuserrole", methods = ['GET', 'POST', 'PUT'])
def get_user_role():
    logging.info(request)
    username = request.json.get('username', 'appadmin_interactor')
    logging.info('username to be parsed')
    logging.info(username)
    if '_' in username:
        u = username.split('_')[1]
        t = {"role": u}
    else:
        t = {"role": "interactor"}

    return jsonify(t)


#Update data Endpoint value fetch in config file
@app.route("/tableauextensions/writeback/api/updatedata", methods = ['GET', 'POST', 'PUT'])
def update_data():
    logging.info(request)
    Json_Writebackvalue = config.get("JSON", "Json_Writebackvalue", raw=True)
    Json_Primarykey = config.get("JSON", "Json_Primarykey", raw=True)   
    try:
        _json = request.json
        for rec in _json:
            config.set('DATABASE TABLE COLUMNS INFORMATION', 'Table_1_Primarykey', rec[Json_Primarykey])
            config.set('DATABASE TABLE COLUMNS INFORMATION', 'Table_1_col6', rec[Json_Writebackvalue])
            Table_1_Primarykey = config.get('DATABASE TABLE COLUMNS INFORMATION', 'Table_1_Primarykey')
            Table_1_col6 = config.get('DATABASE TABLE COLUMNS INFORMATION', 'Table_1_col6')
            t = run(Table_1_col6,Table_1_Primarykey)
        return jsonify("Update table successful!")
    except Exception as e:
        return jsonify (e, 'Row_id not found')        


#Get Data End point 
@app.route("/tableauextensions/writeback/api/getdata", methods = ['GET','POST', 'PUT'])
def get_data():
    logging.info(request)
    conn = postgre_conn_api.get_connection_obj_azure()
    t = postgre_conn_api.execute_query(conn, myselect)
    return jsonify(t)

# #Insert Multiple or Single Columns values 
@app.route("/tableauextensions/writeback/api/audittable", methods = ['POST'])
def audit_table():
        logging.info(request)
        Table_3 = config.get("DATABASE TABLE INFORMATION", "Table_3",raw=True)
        Table_3_col1 = config.get("AUDIT TABLE COLUMNS INFORMATION", "Table_3_col1",raw=True)
        Table_3_col2 = config.get("AUDIT TABLE COLUMNS INFORMATION", "Table_3_col2",raw=True)
        Table_3_col3 = config.get("AUDIT TABLE COLUMNS INFORMATION", "Table_3_col3",raw=True)
        Table_3_col4 = config.get("AUDIT TABLE COLUMNS INFORMATION", "Table_3_col4",raw=True)
        Table_3_col5 = config.get("AUDIT TABLE COLUMNS INFORMATION", "Table_3_col5",raw=True)
        Table_3_col6 = config.get("AUDIT TABLE COLUMNS INFORMATION", "Table_3_col6",raw=True)
        Table_3_col7 = config.get("AUDIT TABLE COLUMNS INFORMATION", "Table_3_col7",raw=True)
        Table_3_col8 = config.get("AUDIT TABLE COLUMNS INFORMATION", "Table_3_col8",raw=True)
        try:
            _json = request.json
            conn = postgre_conn_api.get_connection_obj_azure()
            for rec in _json:
                _Table_3_col1 = rec[Table_3_col1]
                _Table_3_col2= rec[Table_3_col2]
                _Table_3_col3 = rec[Table_3_col3]
                _Table_3_col4 = rec[Table_3_col4]
                _Table_3_col5 = rec[Table_3_col5]
                _Table_3_col6 = rec[Table_3_col6]
                _Table_3_col7 = rec[Table_3_col7]
                _Table_3_col8 = datetime.now()    
                
                cursor = conn.cursor()
                
                query = ('INSERT INTO ' + Table_3 + '('+Table_3_col1+','+Table_3_col2+','+Table_3_col3+','+Table_3_col4+','+Table_3_col5+','+Table_3_col6+','+Table_3_col7+','+Table_3_col8+')'+ ' VALUES'+'('+'?'+','+'?'+','+'?'+','+'?'+','+'?'+','+'?'+','+'?'+','+'?'+')')
                data = (_Table_3_col1,_Table_3_col2,_Table_3_col3, _Table_3_col4, _Table_3_col5, _Table_3_col6, _Table_3_col7, _Table_3_col8)
                cursor.execute(query,data)
            
                conn.commit()
            resp = jsonify('User added successfully!')
            resp.status_code = 200
            return resp
        except Exception as e:
            print(e)


# Insert Single row values 
# @app.route("/tableauextensions/writeback/api/audittable", methods = ['POST'])
# def audit_table():
#     try:    
#         _json = request.json

#         _WB_User = _json['WB_User']
#         _WB_Dashboard_name = _json['WB_Dashboard_name']
#         _WB_Primary_key_name = _json['WB_Primary_key_name']
#         _WB_Primary_key_value = _json['WB_Primary_key_value']
#         _WB_Column_name = _json['WB_Column_name']
#         _WB_Table_name = _json['WB_Table_name']
#         _WB_Value = _json['WB_Value']
#         _WB_date_time = datetime.now()
        

#         conn = postgre_conn_api.get_connection_obj_azure()
#         cursor = conn.cursor()

#         cursor.execute("INSERT INTO WB_Audit(WB_User,WB_Dashboard_name,WB_Primary_key_name,WB_Primary_key_value,WB_Column_name,WB_Table_name,WB_Value,WB_date_time) VALUES(?,?,?,?,?,?,?,?)",(_WB_User,_WB_Dashboard_name,_WB_Primary_key_name,_WB_Primary_key_value,_WB_Column_name,_WB_Table_name,_WB_Value,_WB_date_time))

#         conn.commit()
#         resp = jsonify('User added successfully!')
#         resp.status_code = 200
#         return resp
#     except Exception as e:
#         print(e)


#Update single row End point       
@app.route("/tableauextensions/writeback/api/updatedatarow/<int:Tableau_col10>", methods = ['GET', 'POST', 'PUT'])
def update_data_row(Tableau_col10):
    logging.info(request)
    if len(str(Tableau_col10)) == 0:
        abort(404)
    if not request.json:
        abort(400)
    Tableau_col11 = config.get("TABLEAU DATA", "Tableau_col11", raw=True)
    Tableau_col8 = config.get("TABLEAU DATA", "Tableau_col8", raw=True)   
    Tableau_col9 = config.get("TABLEAU DATA", "Tableau_col9", raw=True)
    Tableau_col7 = config.get("TABLEAU DATA", "Tableau_col7", raw=True)
    try:
        _json = request.json
        for rec in _json:
            config.set('DATABASE TABLE COLUMNS INFORMATION', 'Table_1_Primarykey', rec[Tableau_col7])
            config.set('DATABASE TABLE COLUMNS INFORMATION', 'Table_1_col1', rec[Tableau_col11])
            config.set('DATABASE TABLE COLUMNS INFORMATION', 'Table_1_col5', rec[Tableau_col8])
            config.set('DATABASE TABLE COLUMNS INFORMATION', 'Table_1_col3', rec[Tableau_col9])
            Table_1_col1 = config.get('DATABASE TABLE COLUMNS INFORMATION', 'Table_1_col1')
            Table_1_col5 = config.get('DATABASE TABLE COLUMNS INFORMATION', 'Table_1_col5')
            Table_1_col3 = config.get('DATABASE TABLE COLUMNS INFORMATION', 'Table_1_col3')
            Table_1_Primarykey = config.get('DATABASE TABLE COLUMNS INFORMATION', 'Table_1_Primarykey')
            t = run(Table_1_Primarykey,Table_1_col1,Table_1_col5,Table_1_col3)
        return jsonify("Update table successful!")
    except Exception as e:
        return jsonify (e, 'Row_id not found')     


#Logging request info added here
@app.after_request
def after_request(response):
    logging.info('after_request method called..')
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
    logging.info('response to the request getting printed..')
    logging.info(response)
    return response

#Define Main function with SSL Configration file
if __name__ == "__main__":
    host = config.get("WAITRESS", "host", raw=True)
    port = config.get("WAITRESS", "port", raw=True)
    serve(app, host=host, port=port)
    #app.run()
    #context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
    #context.load_verify_locations(API_CA_T)
    #context.verify_mode = ssl.CERT_NONE
    #context.load_cert_chain(API_CRT, API_KEY)
    # app.run(host=API_HOST, port=API_PORT, debug=DEBUG_ENABLED, ssl_context=context)
