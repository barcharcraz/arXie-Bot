import json
import os

LOGIN_DB_FILENAME = "logins.json"
LOGIN_DB = os.path.join(os.dirname(__file__), LOGIN_DB_FILENAME)

def create_db():
    raise NotImplementedError

def erase_db():
    raise NotImplementedError

def add_user(
