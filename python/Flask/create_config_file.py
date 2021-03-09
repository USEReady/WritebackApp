#Create config file and config object for postgres database 
def run():
    from configparser import ConfigParser
    #Get the configparser object
    config_object = ConfigParser()
    #craete config object
    config_object["SERVERCONFIG"] = {
        "host": "localhost",
        "database": "postgres",
        "port": "5433",
        "user": "postgres",
        "password": "Useready1"
    }
    
    #Write the above sections to config.ini file
    with open('config.ini', 'w') as conf:
        config_object.write(conf)

#define read function
def read_config():
    from configparser import ConfigParser
    # Read config.ini file
    config_object = ConfigParser()
    config_object.read('config.ini')
    serverinfo = config_object["SERVERCONFIG"]
    #print("host is {}".format(serverinfo["host"]))
    print (serverinfo)
    return serverinfo