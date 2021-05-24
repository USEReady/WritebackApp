# This is a main Python script.


# import all neccessary packages 
import database_conn_api
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

#Logging path and app name define 
app = Flask(__name__)
example = config.get("PATHS", "example_file", raw=True)
logging.basicConfig(format='%(asctime)s %(message)s',filename=example, level=logging.DEBUG)


#Azure Query Execute here
myselect = config.get("AZUREQUERY", "select", raw=True)


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

     
#UpdateData Api Endpoint
@app.route("/tableauextensions/writeback/api/updatedata", methods = ['GET', 'POST', 'PUT'])
def update_data():
    logging.info(request)
    Json_Writebackvalue = config.get("JSON", "Json_Writebackvalue", raw=True)
    Json_Primarykey = config.get("JSON", "Json_Primarykey", raw=True)
    json_writebackdashboard = config.get("JSON", "json_writebackdashboard", raw=True)
    json_comment = config.get("JSON", "json_comment", raw=True) 
    try:
        _json = request.json
        for rec in _json:
            config.set('DATABASE TABLE COLUMNS INFORMATION', 'Table_1_Primarykey', rec[Json_Primarykey])
            config.set('DATABASE TABLE COLUMNS INFORMATION', 'Table_1_WriteBack', rec[Json_Writebackvalue])
            config.set('DATABASE TABLE COLUMNS INFORMATION', 'Table_1_Dashboard', rec[json_writebackdashboard])
            config.set('DATABASE TABLE COLUMNS INFORMATION', 'table_1_comment', rec[json_comment])
            Table_1_Primarykey = config.get('DATABASE TABLE COLUMNS INFORMATION', 'Table_1_Primarykey')
            Table_1_WriteBack = config.get('DATABASE TABLE COLUMNS INFORMATION', 'Table_1_WriteBack')
            Table_1_Dashboard = config.get('DATABASE TABLE COLUMNS INFORMATION', 'Table_1_Dashboard')
            table_1_comment = config.get('DATABASE TABLE COLUMNS INFORMATION', 'table_1_comment')
            t = run(Table_1_WriteBack,Table_1_Primarykey,Table_1_Dashboard,table_1_comment)
        return jsonify("Update table successful!")
    except Exception as e:
        return jsonify (e, 'Row_id not found')       


#Get Data Api Endpoint 
@app.route("/tableauextensions/writeback/api/getdata", methods = ['GET','POST', 'PUT'])
def get_data():
    logging.info(request)
    try:
        conn = database_conn_api.get_connection_obj_azure()
        t = database_conn_api.execute_query(conn, myselect)
        return jsonify(t)
    except Exception as e:
            print(e)    


# Insert Multiple or Single Columns values in Audit Table
@app.route("/tableauextensions/writeback/api/audittable", methods = ['POST'])
def audit_table():
        logging.info(request)
        table_audit = config.get("DATABASE TABLE INFORMATION", "table_audit",raw=True)
        Audit_col1 = config.get("AUDIT TABLE COLUMNS INFORMATION", "Audit_col1",raw=True)
        Audit_col2 = config.get("AUDIT TABLE COLUMNS INFORMATION", "Audit_col2",raw=True)
        Audit_col3 = config.get("AUDIT TABLE COLUMNS INFORMATION", "Audit_col3",raw=True)
        Audit_col4 = config.get("AUDIT TABLE COLUMNS INFORMATION", "Audit_col4",raw=True)
        Audit_col5 = config.get("AUDIT TABLE COLUMNS INFORMATION", "Audit_col5",raw=True)
        dashboardname = config.get("SERVERCONFIG ONE DASHBOARD", "dashboardname", raw=True)
        try:
            _json = request.json
            # conn = database_conn_api.get_connection_obj()
            for rec in _json:
                _Audit_col1 = rec[Audit_col1]
                _Audit_col2=  rec[Audit_col2]
                _Audit_col3 = rec[Audit_col3]
                _Audit_col4 = rec[Audit_col4]
                _Audit_col5 = datetime.now()
                # print(_Audit_col2,'line no 147')
                if _Audit_col2 in dashboardname:
                    conn = database_conn_api.get_connection_obj_azure()
                else:
                    conn = database_conn_api.get_connection_obj_azure1()    
                
                cursor = conn.cursor()
                # query = ('INSERT INTO '  + '"'+table_audit+'"' + '('+'"'+Audit_col1+'"'+','+'"'+Audit_col2+'"'+','+'"'+Audit_col3+'"'+','+'"'+Audit_col4+'"'+')'+ ' VALUES'+'('+'\'?\''+','+'\'?\''+','+'\'?\''+','+'\'?\''+')'+ ';' + _Audit_col1,_Audit_col2,_Audit_col3,_Audit_col4)

                #below are the azure query    
                #query = ('INSERT INTO ' + '"'+table_audit+'"' + '('+'"'+Audit_col1+'"'+','+'"'+Audit_col2+'"'+','+'"'+Audit_col3+'"'+','+'"'+Audit_col4+'"'+','+'"'+Audit_col5+'"'+')'+ ' VALUES'+'('+'%s'+','+'%s'+','+'%s'+','+'%s'+','+'%s'+')')
                query = ('INSERT INTO ' + table_audit + '('+Audit_col1+','+Audit_col2+','+Audit_col3+','+Audit_col4+','+Audit_col5+')'+ ' VALUES'+'('+'?'+','+'?'+','+'?'+','+'?'+','+'?'+')')
                data = (_Audit_col1,_Audit_col2,_Audit_col3,_Audit_col4,_Audit_col5)

                #below are the postgres query 
                # query = ('INSERT INTO ' + '"'+table_audit+'"' + '('+'"'+Audit_col1+'"'+','+'"'+Audit_col2+'"'+','+'"'+Audit_col3+'"'+','+'"'+Audit_col4+'"'+','+'"'+Audit_col5+'"'+')'+ ' VALUES'+'('+'%s'+','+'%s'+','+'%s'+','+'%s'+','+'%s'+')')
                # data = (_Audit_col1,_Audit_col2,_Audit_col3,_Audit_col4,_Audit_col5)

                #below are the mysql query 
                # query = ('INSERT INTO ' + '`'+table_audit+'`' + '('+'`'+Audit_col1+'`'+','+'`'+Audit_col2+'`'+','+'`'+Audit_col3+'`'+','+'`'+Audit_col4+'`'+','+'`'+Audit_col5+'`'+')'+ ' VALUES'+'('+'%s'+','+'%s'+','+'%s'+','+'%s'+','+'%s'+')')
                # data = (_Audit_col1,_Audit_col2,_Audit_col3,_Audit_col4,_Audit_col5)
                cursor.execute(query,data)
                print(query)
               
            
                conn.commit()
            resp = jsonify('User added successfully!')
            resp.status_code = 200
            return resp
        except Exception as e:
            print(e)


#Insert Multiple or Single Columns values in Audit Table
# @app.route("/tableauextensions/writeback/api/audittable", methods = ['POST'])
# def audit_table():
#         logging.info(request)
#         table_audit = config.get("DATABASE TABLE INFORMATION", "table_audit",raw=True)
#         Audit_col1 = config.get("AUDIT TABLE COLUMNS INFORMATION", "Audit_col1",raw=True)
#         Audit_col2 = config.get("AUDIT TABLE COLUMNS INFORMATION", "Audit_col2",raw=True)
#         Audit_col3 = config.get("AUDIT TABLE COLUMNS INFORMATION", "Audit_col3",raw=True)
#         Audit_col4 = config.get("AUDIT TABLE COLUMNS INFORMATION", "Audit_col4",raw=True)
#         Audit_col5 = config.get("AUDIT TABLE COLUMNS INFORMATION", "Audit_col5",raw=True)
#         dashboardname = config.get("SERVERCONFIG ONE DASHBOARD", "dashboardname", raw=True)
#         try:
#             _json = request.json
#             # conn = database_conn_api.get_connection_obj()
#             for rec in _json:
#                 _Audit_col1 = rec[Audit_col1]
#                 _Audit_col2=  rec[Audit_col2]
#                 _Audit_col3 = rec[Audit_col3]
#                 _Audit_col4 = rec[Audit_col4]
#                 _Audit_col5 = datetime.now()
#                 if _Audit_col2 in dashboardname:
#                     conn = database_conn_api.get_connection_obj()
#                 else:
#                     conn = database_conn_api.get_connection_obj_azure()     
                
#                 cursor = conn.cursor()
#                 #below are the azure query 
#                 # query = ('INSERT INTO ' + table_audit + '('+Audit_col1+','+Audit_col2+','+Audit_col3+','+Audit_col4+','+Audit_col5+')'+ ' VALUES'+'('+'?'+','+'?'+','+'?'+','+'?'+','+'?'+')')
#                 # data = (_Audit_col1,_Audit_col2,_Audit_col3,_Audit_col4,_Audit_col5)

#                 #below are the postgres query 
#                 # query = ('INSERT INTO ' + '"'+table_audit+'"' + '('+'"'+Audit_col1+'"'+','+'"'+Audit_col2+'"'+','+'"'+Audit_col3+'"'+','+'"'+Audit_col4+'"'+','+'"'+Audit_col5+'"'+')'+ ' VALUES'+'('+'%s'+','+'%s'+','+'%s'+','+'%s'+','+'%s'+')')
#                 # data = (_Audit_col1,_Audit_col2,_Audit_col3,_Audit_col4,_Audit_col5)

#                 #below are the Mysql query 
#                 query = ('INSERT INTO ' + '`'+table_audit+'`' + '('+'`'+Audit_col1+'`'+','+'`'+Audit_col2+'`'+','+'`'+Audit_col3+'`'+','+'`'+Audit_col4+'`'+','+'`'+Audit_col5+'`'+')'+ ' VALUES'+'('+'%s'+','+'%s'+','+'%s'+','+'%s'+','+'%s'+')')
#                 data = (_Audit_col1,_Audit_col2,_Audit_col3,_Audit_col4,_Audit_col5)
#                 cursor.execute(query,data)
#                 print(query)
            
#                 conn.commit()
#             resp = jsonify('User added successfully!')
#             resp.status_code = 200
#             return resp
#         except Exception as e:
#             print(e)
            

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
