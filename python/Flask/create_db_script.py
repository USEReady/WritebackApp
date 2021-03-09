#create db table mentioned here
# for postgres forecast only  
# CREATE_TABLE_QUERY_TEST = '''
# CREATE TABLE public."TableauForecastingWb"
# (
#     "Sales_Team" text,
#     "Sales_Leader" text,
#     "Regional_Head_of_Sales" text,
#     "Forecast_Period" text,
#     "Forecast" bigint,
#     "Contract_Date" date NOT NULL,
#     "COA_Product_Name" text,
#     "COA_Product_Id" bigint,
#     "Account_Name" text NOT NULL,
#     "Account_ID" bigint NOT NULL,
#     "ID" bigint NOT NULL,
#     CONSTRAINT "TabID" PRIMARY KEY ("ID"),
#     CONSTRAINT "TabID" UNIQUE ("ID")
# );
# ALTER TABLE public."TableauForecastingWb"
#     OWNER to postgres;
# '''
# # for postgres sales only  
# CREATE_TABLE_QUERY_SALES = '''
# CREATE TABLE public."Sales"
# (
# "Row ID"	bigint NOT NULL
# ,"Order ID"	text
# ,"Order Date"	date
# ,"Ship Date"	date
# ,"Ship Mode"	text
# ,"Customer ID"	text
# ,"Customer Name"	text
# ,"Segment"	text
# ,"Country/Region"	text
# ,"City"	text
# ,"State"	text
# ,"Postal Code"	bigint
# ,"Region"	text
# ,"Product ID"	text
# ,"Category"	text
# ,"Sub-Category"	text
# ,"Sales"	double precision
# ,"Quantity"	bigint
# ,"Discount"	double precision
# ,"Profit"	double precision
# , CONSTRAINT "Sales_pkey" PRIMARY KEY ("Row ID")
# );
# ALTER TABLE public."Sales"
#     OWNER to postgres;
# '''
# # for postgres forecast only  
# CREATE_TABLE_QUERY_FORECAST = '''
# CREATE TABLE public."Forecast"
# (
#     "Row ID" bigint NOT NULL,
#     "Order ID" text COLLATE pg_catalog."default",
#     "Order Date" date,
#     "Ship Date" date,
#     "Ship Mode" text COLLATE pg_catalog."default",
#     "Customer ID" text COLLATE pg_catalog."default",
#     "Customer Name" text COLLATE pg_catalog."default",
#     "Segment" text COLLATE pg_catalog."default",
#     "Country/Region" text COLLATE pg_catalog."default",
#     "City" text COLLATE pg_catalog."default",
#     "State" text COLLATE pg_catalog."default",
#     "Postal Code" bigint,
#     "Region" text COLLATE pg_catalog."default",
#     "Product ID" text COLLATE pg_catalog."default",
#     "Category" text COLLATE pg_catalog."default",
#     "Sub-Category" text COLLATE pg_catalog."default",
#     "Sales" double precision,
#     "Quantity" bigint,
#     "Discount" double precision,
#     "Profit" double precision,
#     CONSTRAINT "Forecast_pkey" PRIMARY KEY ("Row ID")
# );
# ALTER TABLE public."Forecast"
#     OWNER to postgres;
    
# '''
# # for postgres forecast only  
# CREATE_TABLE_QUERY = '''
# CREATE TABLE public."Forecast"
# (
#     "Row ID" bigint NOT NULL,
#     "Order Date" date,
#     "Ship Date" date,
#     "Customer ID" text COLLATE pg_catalog."default",
#     "Customer Name" text COLLATE pg_catalog."default",
#     "Category" text COLLATE pg_catalog."default",
#     "Sales" double precision,
#     "Profit" double precision,
# 	"Forecast_Amount" double precision,
#     CONSTRAINT "Forecast_pkey" PRIMARY KEY ("Row ID")
# );
# ALTER TABLE public."Forecast"
#     OWNER to postgres;
# '''
# #for azure sales only
# CREATE_TABLE_QUERY_AZURE1 = '''
# SET ANSI_NULLS ON
# GO
# SET QUOTED_IDENTIFIER ON
# GO
# CREATE TABLE [dbo].[sales](
# 	[Category] [nvarchar](500) NULL,
# 	[City] [nvarchar](500) NULL,
# 	[Country_Region] [nvarchar](500) NULL,
# 	[Customer_ID] [nvarchar](500) NULL,
# 	[Customer_Name] [nvarchar](500) NULL,
# 	[Order_ID] [nvarchar](500) NULL,
# 	[Product_ID] [nvarchar](500) NULL,
# 	[Region] [nvarchar](500) NULL,
# 	[Segment] [nvarchar](500) NULL,
# 	[Ship_Mode] [nvarchar](500) NULL,
# 	[State] [nvarchar](500) NULL,
# 	[Sub_Category] [nvarchar](500) NULL,
# 	[Row_ID] [int] NOT NULL,
# 	[Postal_Code] [nvarchar](500) NULL,
# 	[Sales] [decimal](18, 10) NULL,
# 	[Discount] [decimal](18, 10) NULL,
# 	[Quantity] [int] NULL,
# 	[Profit] [decimal](18, 10) NULL,
# 	[Contract_Date] [date] NULL,
# 	[Ship_Date] [date] NULL
# ) ON [PRIMARY]
# GO
# ALTER TABLE [dbo].[sales] ADD  CONSTRAINT [PK_sales_2] PRIMARY KEY CLUSTERED 
# (
# 	[Row_ID] ASC
# )WITH (STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ONLINE = OFF, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
# GO

# '''
#for azure forecast only 
# CREATE_TABLE_QUERY_AZURE = '''
# SET ANSI_NULLS ON
# GO
# SET QUOTED_IDENTIFIER ON
# GO
# CREATE TABLE [dbo].[forecast](
# 	[Category] [nvarchar](500) NOT NULL,
# 	[Customer_Name] [nvarchar](500) NOT NULL,
# 	[Sales] [decimal](18, 10) NOT NULL,
# 	[Customer_ID] [nvarchar](500) NOT NULL,
# 	[Profit] [float] NOT NULL,
# 	[Row_ID] [int] NOT NULL,
# 	[Forecast_Amount] [decimal](18, 10) NOT NULL,
# 	[Ship_Date] [date] NOT NULL,
# 	[Order_Date] [date] NOT NULL
# ) ON [PRIMARY]
# GO
# ALTER TABLE [dbo].[forecast] ADD  CONSTRAINT [PK_forecast_1] PRIMARY KEY CLUSTERED 
# (
# 	[Row_ID] ASC
# )WITH (STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ONLINE = OFF, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
# GO
# '''

#for azure forecast only 
from configparser import ConfigParser
import os

config = ConfigParser()
config.read(os.path.join(os.path.dirname(__file__), 'config.ini'))

# file = r'C:\Users\Admin\Desktop\azure\python\python\FlaskPrototype\config.ini'
# config = ConfigParser()
# config.read(file)

Table_1 = config.get("DATABASE TABLE INFORMATION", "Table_1", raw=True)
Table_1_col1 = config.get("DATABASE TABLE COLUMNS INFORMATION", "Table_1_col1", raw=True)
Table_1_col2 = config.get("DATABASE TABLE COLUMNS INFORMATION", "Table_1_col2", raw=True)
Table_1_col3 = config.get("DATABASE TABLE COLUMNS INFORMATION", "Table_1_col3", raw=True)
Table_1_col4 = config.get("DATABASE TABLE COLUMNS INFORMATION", "Table_1_col4", raw=True)
Table_1_col5 = config.get("DATABASE TABLE COLUMNS INFORMATION", "Table_1_col5", raw=True)
Table_1_Primarykey = config.get("DATABASE TABLE COLUMNS INFORMATION", "Table_1_Primarykey", raw=True)
Table_1_col6 = config.get("DATABASE TABLE COLUMNS INFORMATION", "Table_1_col6", raw=True)
Table_1_col7 = config.get("DATABASE TABLE COLUMNS INFORMATION", "Table_1_col7", raw=True)
Table_1_col8 = config.get("DATABASE TABLE COLUMNS INFORMATION", "Table_1_col8", raw=True)

CREATE_TABLE_QUERY_AZURE = 'SET ' + 'ANSI_NULLS ' + 'ON ' + ('\n')+ 'GO ' + 'SET ' + 'QUOTED_IDENTIFIER ' + 'ON ' + ('\n')+ 'GO ' + 'CREATE TABLE ' + '['+ 'dbo'+']'+ '.'+ '['+Table_1+']'+ '('+ '['+Table_1_col1+']'+ '['+'nvarchar'+']'+ '('+'500'+')'+ 'NOT NULL '+ ','+  '['+Table_1_col2+']'+ '['+'nvarchar'+']'+ '('+'500'+')'+ 'NOT NULL '+ ','+  '['+Table_1_col3+']'+ '['+'decimal'+']'+ '('+'18'+','+'10'+')'+ 'NOT NULL '+ ','+ '['+Table_1_col4+']'+ '['+'nvarchar'+']'+ '('+'500'+')'+ 'NOT NULL '+ ','+  '['+Table_1_col5+']'+ '['+'float'+']'+ 'NOT NULL '+ ','+  '['+Table_1_Primarykey+']'+ '['+'int'+']'+ 'NOT NULL '+ ','+  '['+Table_1_col6+']'+ '['+'decimal'+']'+ '('+'18'+','+'10'+')'+ 'NOT NULL '+ ','+  '['+Table_1_col7+']'+ '['+'date'+']'+ 'NOT NULL '+ ','+  '['+Table_1_col8+']'+ '['+'date'+']'+ 'NOT NULL '+ ')' + 'ON ' + '['+'PRIMARY'+']' + ('\n')+'GO ' + 'ALTER TABLE ' + '['+'dbo'+']'+ '.'+'['+Table_1+'] '+ 'ADD ' + 'CONSTRAINT '+ '['+'PK_forecast_1'+']'+ 'PRIMARY KEY CLUSTERED '+'('+   '['+Table_1_Primarykey+']'+ 'ASC ' + ')'+'WITH '+'('+'STATISTICS_NORECOMPUTE ' + '= ' + 'OFF '+ ',' + 'IGNORE_DUP_KEY ' + '= '+'OFF '+ ',' + 'ONLINE '+ '= '+ 'OFF '+ ')' + 'ON ' + '['+'PRIMARY '+']'+('\n')+'GO '
print(CREATE_TABLE_QUERY_AZURE)
#function to execute the craete table query
def run():
    import postgre_conn_api
    conn = postgre_conn_api.get_connection_obj_azure()
    postgre_conn_api.execute_dml(conn, CREATE_TABLE_QUERY_AZURE)

# def run():
#     import postgre_conn_api
#     conn = postgre_conn_api.get_connection_obj()
#     postgre_conn_api.execute_dml(conn, CREATE_TABLE_QUERY)