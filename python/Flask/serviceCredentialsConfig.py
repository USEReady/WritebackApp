from cryptography.fernet import Fernet
from configparser import ConfigParser
import os

config = ConfigParser()
config.read(os.path.join(os.path.dirname(__file__), 'config.ini'))


def encrypt(username,password):
    key = Fernet.generate_key() #this is your "password"
    cipher_suite = Fernet(key)
    encoded_username = cipher_suite.encrypt(username.encode())
    encoded_password = cipher_suite.encrypt(password.encode())
    config.set('DEFAULT SERVERCONFIG', 'user', encoded_username.decode("utf-8"))
    config.set('DEFAULT SERVERCONFIG', 'password', encoded_password.decode("utf-8"))
    # config.set('SERVERCONFIG1', 'user', encoded_username.decode("utf-8"))
    # config.set('SERVERCONFIG1', 'password', encoded_password.decode("utf-8"))
    config.set('KEY', 'key', key.decode("utf-8"))

    with open("config.ini", 'w') as conf:
        config.write(conf)


def encrypt1(username,password):
    key1 = Fernet.generate_key() #this is your "password"
    cipher_suite = Fernet(key1)
    encoded_username = cipher_suite.encrypt(username.encode())
    encoded_password = cipher_suite.encrypt(password.encode())
    config.set('SERVERCONFIG ONE', 'user', encoded_username.decode("utf-8"))
    config.set('SERVERCONFIG ONE', 'password', encoded_password.decode("utf-8"))
    config.set('KEY1', 'key1', key1.decode("utf-8"))

    with open("config.ini", 'w') as conf:
        config.write(conf)
            
    

# encrypt('user', 'hello')



