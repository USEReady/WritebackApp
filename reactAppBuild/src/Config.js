var Config = {
/*Rest API Server */
//host:'uracme.useready.com',
//port:'9443',
/*SERVERCONFIG*/
//server:'localhost',
//database:'postgres',
//user:'postgres',
//password:'Useready1',
//connection_string:'',
/*DATABASE TABLE INFORMATION */
//schema:'',
Table_1:'forecast',
//Table_2:'',
/*DATABASE TABLE COLUMNS INFORMATION*/
Table_1_Primarykey:'Row_ID',
Table_1_col1:'Category',
Table_1_col2:'Customer_Name',
Table_1_col3:'Sales',
Table_1_col4:'Customer_ID',
Table_1_col5:'Profit',
Table_1_col6:'Ship_Date',
Table_1_col7:'Order_Date',
Table_WriteBack:'Forecast_Amount',
//Table_2_Primarykey:'Row_ID',
//Table_2_col1:'',
//Table_2_col2:'',
//Table_2_col3:'',
/*TABLEAU DATA*/
Tableau_Primarykey:'Row ID',
Tableau_col1:'MY(Contract Date)',
Tableau_col2:'username', 
Tableau_col3:'Category',
Tableau_col4:'Measure Names',
Tableau_col5:'Measure Values',
Tableau_col6:'Revenue Budget',
Tableau_col7:'Sales',
Tableau_WriteBack:'Adjust_Forecast',
sheet1:'Extension Input',
/*Column Measure Calculation*/
Tableau_writeBack_Calculation:'Calculation_1454662740677197828',
Tableau_writeBack_Calculation_preview:'Calculation_5806265832391512066',
Calculation1:'Calculation_1454662740669812737',
Calculation2:'Sales',
Tableau_WriteBack_column_sequence:5,
/*TABLEAU LABEL*/
lablel1:'Contract Date',
/*Paths*/
//log_file:'',
/*User Role*/
ReadOnlyRole1:'Viewer',
ReadOnlyRole2:'viewer',
/*Audit table*/
WB_User: 'WB_User',
WB_Dashboard_name:'WB_Dashboard_name',
WB_Primary_key_name:'WB_Primary_key_name',
WB_Primary_key_value:'WB_Primary_key_value',
WB_Column_name:'WB_Column_name',
WB_Table_name:'WB_Table_name',
WB_Value:'WB_Value',

   
/*Rest Server Url*/
rest_server_url:'https://uracme-waitress.useready.com:9443/server/tableauextensions/writeback/api/'
}
module.exports = {Config};