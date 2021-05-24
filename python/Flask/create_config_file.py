import os


# def run():
#     from configparser import ConfigParser
#     #Get the configparser object
#     config_object = ConfigParser()

#     config_object["SERVERCONFIG POSTGRES"] = {
#         "host": "localhost",
#         "database": "postgres",
#         "port": "5433",
#         "user": "postgres",
#         "password": "Useready1"
#     }

#     #Write the above sections to config.ini file
#     with open("config.ini", 'w') as conf:
#         config_object.write(conf)

def read_config():
    from configparser import ConfigParser
    # Read config.ini file
    config = ConfigParser()
    config.read(os.path.join(os.path.dirname(__file__), 'config.ini'))
    # config_object = ConfigParser()
    # config_object.read(r'C:\Users\rohitk\Desktop\Mydesktopcode\NewServerCode\flask\config.ini')
    serverinfo = config["SERVERCONFIG POSTGRES"]
    #print("host is {}".format(serverinfo["host"]))
    print (serverinfo)
    return serverinfo